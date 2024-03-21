from concurrent.futures import ThreadPoolExecutor, as_completed
from math import exp
import os
import subprocess
from typing import List, Dict, Union, Optional, Tuple
import requests
import json
import openai
from urllib.parse import quote_plus, urljoin
from dotenv import load_dotenv
import tiktoken
from strip_tags import strip_tags
from click.testing import CliRunner
from shot_scraper import cli

from pygments.lexers import MarkdownLexer
from pygments.formatters import TerminalFormatter
from pygments import highlight

enc = tiktoken.get_encoding("cl100k_base")

load_dotenv()
BROWSING_MODE_PROMPT = """You have a 'browser' tool with access to the following functions for browsing and searching the internet:
    `bing_search(query: str, recency_days: int)` Issues a query to a search engine and displays the results. 
    
    `open_bing_result(id: str)` Opens the webpage with the given id from the search results, displaying it.
    
    `click(url: str)` Opens the webpage with the given full URL, displaying it. The URL should be a fully qualified URL starting with http:// or https://.
    
    `back()` Returns to the previous page and displays it.

    `scroll(amt: int)` Scrolls up or down in the open webpage by the given amount. 

    `quote_lines(start: int, end: int)` Stores a text span from an open webpage. Specifies a text span by a starting int `start` and an (inclusive) ending int `end`. To quote a single line, use `start` = `end`.

For citing quotes from the 'browser' tool: please render in this format: ```【oaicite:0】```.
For long citations: please render in this format: `[link text](message idx)`.
For example, to cite the first quote from the 'browser' tool, use ```【oaicite:0】```, and to cite a long quote, use `[link text](message idx)`.
## IMPORTANT
Always be very thorough in your search. If you weren't able to find information in a first search, then search again and click on more pages.  
Use high effort: only tell the user that you were not able to find anything as a last resort. Keep trying instead of giving up.
Organize responses to flow well, not by source or by citation. Ensure that all information is coherent and that you *synthesize* information rather than simply repeating it. 
For requests for source-code, always provide a working example that blends your findings from the internet with the users particular request and incorporating their data if relevant, and a link to where you found the information.
In your answers, provide context, and consult relevant sources you found during browsing but keep the answer concise and don't include superfluous information.
"""

# ToOptimize: Simplify and merge the allbrowser / webBrowser_tools logic into a unified ToolSet class.
# This will make it easier to manage the available tools and reduce duplication.
class ToolSet:
    def __init__(self, tools):
        self.tools = tools

    def to_dict(self):
        return [tool.to_dict() for tool in self.tools]
        
class Tool:
    def __init__(self, name, description, parameters):
        self.name = name
        self.description = description
        self.parameters = parameters

    def to_dict(self):
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.parameters
            }
        }

allbrowser_tools = ToolSet([
    Tool("bing_search", "Search Bing for the given query and return the search results.", 
         {"type": "object", "properties": {"query": {"type": "string", "description": "The search query"}}, "required": ["query"]}),
    Tool("open_bing_result", "Open a Bing search result by its ID.", 
         {"type": "object", "properties": {"id": {"type": "integer", "description": "The ID of the webpage to open from search results"}}, "required": ["id"]}),
    Tool("click", "Navigate to a webpage by its URL.", 
         {"type": "object", "properties": {"url": {"type": "string", "description": "The full URL of the webpage to open. Should start with http:// or https://"}}, "required": ["url"]}),
    Tool("back", "Go back to the previous page.", {"type": "object", "properties": {}}),
    Tool("scroll", "Scroll the current webpage up or down.",
         {"type": "object", "properties": {"amt": {"type": "integer", "description": "The number of chunks to scroll up or down (-1, 1 etc)"}}, "required": ["amt"]}),
    Tool("quote_lines", "Quote lines from the current webpage.",
         {"type": "object", "properties": {"start": {"type": "integer", "description": "The starting line number"}, "end": {"type": "integer", "description": "The ending line number"}}, "required": ["start", "end"]}),
    Tool("Generate_Bing_Queries_for_User_Question", "Generate a list of Bing search queries using the user's question.",
         {"type": "object", "properties": {"user_question": {"type": "string", "description": "The user's question."}}, "required": ["user_question"]})
])

webBrowser_tools = ToolSet([tool for tool in allbrowser_tools.tools if tool.name != "Generate_Bing_Queries_for_User_Question"])

class SearchResult:
    def __init__(self, data: Dict[str, Union[str, int]]):
        self.id: int = int(data.get('id').split('.')[-1]) 
        self.url: str = data.get('url')
        self.name: str = data.get('name')
        self.snippet: str = data.get('snippet')
        
        
class WebBrowser:
    
    class webpage:
        def __init__(self):
            self.content = []
            self.url = ""

    def __init__(self):
        self.search_results: List[SearchResult] = []
        self.page_scroll_position = 0
        self.current_page = self.webpage()
        self.history: List[List[str]] = []
        self.visible_chunk_count = 1
        self.browser_tools = []    

    def search(self, query: str, recency_days: int):
        print(f"\033[92m\n WebBrowser.search: query: {query[:100]}\033[0m")  # green
        
        search_results = run_custom_bing_search(query, recency_days)
        if search_results:
            relevant_link_objects = process_search_results(query, search_results, openai_client, self.browser_tools)
            self.search_results = relevant_link_objects
            return relevant_link_objects
        else:
            return []

    def scroll(self, amt: int) -> List[str]:
        print(f"\033[96m\n WebBrowser.scroll: amt: {amt}\033[0m")  # cyan
        self.page_scroll_position = max(0, min(self.page_scroll_position + amt, len(self.current_page.content) - self.visible_chunk_count))
        start_index = self.page_scroll_position
        end_index = min(start_index + self.visible_chunk_count, len(self.current_page.content))
        visible_chunks = self.current_page.content[start_index:end_index]
        return visible_chunks

    def open_bing_result(self, id: int):
        url = next((result.url for result in self.search_results if result.id == id), None)
        print(f"\033[94m\n WebBrowser.open_bing_result: id: {id} url: {url}\033[0m")  # blue
        if url is None:
            print("URL is None, cannot fetch webpage content.")
            return []

        return self.click(url)
    
    def click(self, url: str):
        print(f"\033[94m\n WebBrowser.click: url: {url}\033[0m")  # blue
        
        if not url.startswith("http://") and not url.startswith("https://"):
            if self.current_page.url:
                url = urljoin(self.current_page.url, url)
            else:
                print("Cannot convert relative URL to absolute URL without current page.")
                return []
        
        content = fetch_webpage_content(url)
        chunk_size = 2048
        self.history.append(self.current_page.content) 
        chunks = list(create_chunks(content, chunk_size, enc))
        self.current_page.content = chunks
        self.current_page.url = url
        return chunks

    def back(self) -> List[str]:
        print(f"\033[93m\n WebBrowser.back\033[0m")  # yellow
        if self.history:
            self.current_page.content = self.history.pop()
            self.page_scroll_position = 0
            return self.current_page.content
        else:
            return []

    def quote_lines(self, start: int, end: int):
        print(f"\033[33m\n WebBrowser.quote_lines: start: {start}, end: {end}\033[0m")
        quote = "\n".join(self.current_page.content[start-1:end])
        return quote

# ToOptimize: Use a generator to yield chunks on-demand rather than creating the full list upfront.
# This will reduce memory usage for large webpages.
def create_chunks(text, n, tokenizer):
    tokens = tokenizer.encode(text)
    for i in range(0, len(tokens), n):
        chunk = tokenizer.decode(tokens[i:i+n])
        if len(chunk) > int(0.5 * n):
            yield chunk
        else:
            yield tokenizer.decode(tokens[i:min(i+n, len(tokens))])

def initialize_clients():
    openai_client = openai.OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_KEY"),
    )
    bing_search_key = os.environ["BING_API_KEY"]
    custom_search_key = os.environ["BING_CUSTOM_KEY"]

    return openai_client, bing_search_key, custom_search_key


# ToOptimize: Use a retry decorator to handle retries more cleanly.
def retry(max_retries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except requests.exceptions.RequestException as e:
                    print(f"Error occurred: {e}")
                    retries += 1
                    if retries == max_retries:
                        print(f"{func.__name__} failed after {max_retries} retries.")
                        return None
                    print(f"Retrying {func.__name__} ({retries}/{max_retries})...")
        return wrapper
    return decorator

@retry(max_retries=3)
def run_custom_bing_search(search_query, recency_days=30):
    subscription_key = os.environ["BING_CUSTOM_KEY"]
    custom_config_id = '6a23d0dc-6abc-412e-a72f-1333d02e0027'
    base_url = "https://api.bing.microsoft.com/v7.0/custom/search?"
    encoded_query = quote_plus(search_query)
    bing_search_query = f'{base_url}q={encoded_query}&customconfig={custom_config_id}&responseFilter=webpages'
    r = requests.get(bing_search_query, headers={'Ocp-Apim-Subscription-Key': subscription_key})
    r.raise_for_status()
    response_data = json.loads(r.text)
    print(f"\033[95m\n run_custom_bing_search: Responses received(n) = {len(response_data.get('webPages', {}).get('value', []))}...\033[0m")
    return response_data

@retry(max_retries=3)  
def fetch_webpage_content(url):
    print(f"\n fetch_webpage_content from URL: {url}")
    result = run_shot_scraper(url)
    stripped = strip_tags(result, minify=True, keep_tags=["p", "a"])
    stripped = stripped.replace("\n\n\n", "\n")
    print(f"\n fetch_webpage_content: stripped: {stripped[:100]}\n")
    stripped = format_webpage(stripped)
    content = llm_format_webpage(stripped)
    return content

def run_shot_scraper(url):
    runner = CliRunner()
    result = runner.invoke(cli.cli, ["html", url])
    return result.output

def format_webpage(webpage):
    formatted = ""
    lines = webpage.split("\n")
    line_num = 1
    for line in lines:
        formatted += f"{line_num}. {line}\n"
        line_num += 1
    return formatted

@retry(max_retries=3)
def llm_format_webpage(webpage):
    webpage = format_webpage(webpage)
    client = openai.OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_KEY"),
    )
    prompt = f"Here is a webpage with line numbers. Remove all HTML tags and return the text. Do include all the URLs. But remove duplicate text and cruft.\n\n{webpage}"
    model = "anthropic/claude-3-haiku"
    messages = [
        {"role": "system", "content": "You are a HTML converter. You convert HTML to plaintext, or Markdown, according to the users need."},
        {"role": "user", "content": prompt},
    ]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )
    return response.choices[0].message.content

# ToOptimize: Use async/await and asyncio.gather to parallelize API calls. 
# This can significantly speed up the processing of search results.
async def process_search_results(user_query: str, search_results: Dict, openai_client, browser_tools) -> List[SearchResult]:
    if 'webPages' not in search_results or 'value' not in search_results['webPages']:
        print("No web pages found in the search results.")
        return []

    search_results_subset = [{"id": result["id"], "url": result["url"], "snippet": result["snippet"]} for result in search_results["webPages"]["value"]]

    tools = [
        Tool("Save_Relevant_Results_ids", "Save a list of relevant url's, the content of which will be retrieved later.", 
             {"type": "object", "properties": {"result_ids": {"type": "array", "items": {"type": "integer"}}}, "required": ["result_ids"]})
    ]
    system_message = f"""You are an AI web search assistant designed to analyze Bing search results and extract a list of relevant links that may contain information to help answer the user's query.
    Pay very careful attention to ALL the details in the user's query and provide a response that is as accurate as possible."""
    
    prompt = f"Analyze these Bing search results: '{json.dumps(search_results_subset)}'\n\n based on this user request: {user_query}.\n\nExtract a list of relevant search result id's that may contain information to help answer the user's query."
    response = await query_model(prompt, openai_client, tools, system_message)
    
    relevant_ids = []
    if response.tool_calls:
        for tool_call in response.tool_calls:
            if tool_call.function.name == "Save_Relevant_Results_ids":
                function_args = json.loads(tool_call.function.arguments)
                relevant_ids = function_args.get("result_ids")
                break
    
    relevant_links_objects = []
    for result in search_results["webPages"]["value"]:
        if result["id"].split(".")[-1] in map(str, relevant_ids):
            relevant_links_objects.append(SearchResult(result))
    
    return relevant_links_objects


async def query_model(prompt: str, openai_client, tools, system_message, messages=None):
    if not messages: 
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
        ]          
    
    token_estimate = len(enc.encode(messages[-1]["content"]))

    model = "openai/gpt-4-turbo-preview" if token_estimate > 15000 else "openai/gpt-3.5-turbo-0125"
    
    async with openai_client as client:
        response = await client.chat.completions.create(
            model=model,
            temperature=1,
            seed=1234,
            messages=messages,
            tools=tools,
        )
    
    return response.choices[0].message


async def json_gpt(prompt: str, model: str) -> Dict:
    system_message = "Always write valid JSON in the response."
    messages = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]
    
    async with openai_client as client:
        response = await client.chat.completions.create(
            model=model,
            messages=messages,
            response_format={"type": "json_object"},
        )
    
    json_response = json.loads(response.choices[0].message.content)
    return json_response
    

async def generate_bing_queries_for_user_question(user_question: str, model: str) -> List[str]:
    QUERIES_INPUT = f"""
    You have access to BING search API that returns web search results.
    Generate an small array of about three search queries that are relevant to this question.
    Use a variation of related keywords for the queries, trying to be as general as possible.
    Utilize advanced BING search operators to refine the search results. 
    Include as many queries as you can think of, including and excluding terms.
    Be creative. The better your search queries are formed, the more likely you are to find relevant results.

    User question: {user_question}

    Format: {{"queries": ["query_1", "query_2", "query_3"]}}  
    """
    queries = (await json_gpt(QUERIES_INPUT, model))["queries"]
    print(f"\n generate_bing_queries_for_user_question: queries: {queries}")
    queries.append(user_question)  # Include original question
    
    return queries

# ToOptimize: Refactor web_search into smaller, more focused functions.
# Use async/await throughout to enable concurrency where possible.
async def web_search(user_question, openai_client, bing_search_key, system_message, browser):
    model = "gpt-3.5-turbo-0125"
    messages = [{"role": "user", "content": "USER_QUESTION:" + user_question}]
    index = 0
    while True:
        token_estimate = len(enc.encode(messages[-1]["content"]))
        model = "openai/gpt-4-turbo-preview" if token_estimate > 15000 else "openai/gpt-3.5-turbo-0125"
        browser.browser_tools = allbrowser_tools.to_dict() if index == 0 else webBrowser_tools.to_dict()
        index += 1
        response_message = await query_model(
            user_question,
            openai_client,
            browser.browser_tools,
            system_message,
            messages,
        )
        if response_message.tool_calls:
            tool_calls = [parse_tool_call(tool_call) for tool_call in response_message.tool_calls]
            for function_name, function_args in tool_calls:
                print(f"function_name: {function_name}")
                if function_name == "bing_search":
                    query = function_args["query"]
                    relevant_search_results = await browser.search(query, recency_days=30)
                    messages.append(
                        {
                            "role": "user", 
                            "content": f"Relevant links: {json.dumps([obj.__dict__ for obj in relevant_search_results])}",
                        }
                    )
                elif function_name == "open_bing_result":
                    id = function_args["id"]
                    print(f"Opening link: {id}")
                    chunks = await browser.open_bing_result(int(id))
                    await update_messages(messages, chunks, browser)
                elif function_name == "click":
                    url = function_args["url"] 
                    print(f"Clicking on URL: {url}")
                    chunks = await browser.click(url)
                    await update_messages(messages, chunks, browser)
                elif function_name == "back":
                    print(f"Going back to the previous page")
                    await browser.back()
                elif function_name == "scroll":
                    amt = function_args["amt"]
                    print(f"Scrolling by: {amt}")
                    visible_chunks = await browser.scroll(amt)
                    await update_messages(messages, visible_chunks, browser, scroll=True)  
                elif function_name == "quote_lines":
                    start = function_args["start"]
                    end = function_args["end"]
                    print(f"Quoting lines: {start} to {end}")
                    quote = await browser.quote_lines(start, end)
                    print(f"Quoting lines: {quote[:140]}")
                    messages.append({"role": "assistant", "content": quote})
                elif function_name == "Generate_Bing_Queries_for_User_Question":
                    user_question = function_args["user_question"]
                    queries = await generate_bing_queries_for_user_question(user_question, model)
                    messages.append(
                        {
                            "role": "assistant",
                            "content": f"Generated Bing search queries: {json.dumps(queries)}",  
                        }
                    )
                else:
                    print(f"Unknown function: {function_name}")
        else:
            assistant_response = response_message.content
            print(f"Assistant response: {assistant_response}")
            user_input = input("User: ")
            messages.append({"role": "user", "content": user_input})

def parse_tool_call(tool_call):
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments)
    return function_name, function_args

async def update_messages(messages, chunks, browser, scroll=False):
    visible_chunks = browser.get_visible_chunks()
    number_of_chunks = len(chunks)
    if visible_chunks:
        if scroll:
            messages.append(
                {
                    "role": "assistant",
                    "content": f"Visible chunks after scrolling: {visible_chunks}",
                }
            )
        else:
            messages.append(
                {
                    "role": "user",
                    "content": f"Here is chunk {chunks.index(visible_chunks[0])+1} of {number_of_chunks}: {visible_chunks[0]}. Use scroll to navigate the chunks.",
                }
            )
    else:
        messages.append(
            {
                "role": "user" if not scroll else "assistant", 
                "content": "No visible chunks after scrolling." if scroll else "The webpage content is empty.",
            }
        )

openai_client, bing_search_key, custom_search_key = initialize_clients()
print(f"Test web search")
browser = WebBrowser()
    
with ThreadPoolExecutor() as executor:
    future = executor.submit(web_search, "example question needing a web search to answer.", 
                             openai_client, custom_search_key, BROWSING_MODE_PROMPT, browser)
    answer_text = future.result()

print(highlight(answer_text, MarkdownLexer(), TerminalFormatter()))  