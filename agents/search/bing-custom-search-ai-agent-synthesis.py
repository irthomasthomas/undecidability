from collections import deque
from concurrent.futures import ThreadPoolExecutor
from math import exp
import os
import subprocess
from typing import List, Dict, Union, Optional, Tuple
from cachetools import TTLCache
import requests
import json
import openai
from urllib.parse import quote_plus, urljoin
from dotenv import load_dotenv
import tiktoken
from strip_tags import strip_tags
from click.testing import CliRunner
import shot_scraper

from pygments.lexers import MarkdownLexer
from pygments.formatters import TerminalFormatter
from pygments import highlight

from multiprocessing import Pool, Process, Queue, Manager
runner = CliRunner()

enc = tiktoken.get_encoding("cl100k_base")

load_dotenv()
# Language Model Main System Prompt for Web Search
BROWSING_MODE_PROMPT = """You have a 'browser' tool with access to the following functions for browsing and searching the internet:
        `bing_search(query: str, recency_days: int)` Issues a query to a search engine and displays the results. 
        
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
    if retry_count
    Here's the rest of the updated code:

    ```python   if retry_count
    Here's the rest of the updated code:

    ```pythonIn your answers, provide context, and consult relevant sources you found during browsing but keep the answer concise and don't include superfluous information.
"""

allbrowser_tools = [
    {
        "type": "function",
        "function": {
            "name": "bing_search",
            "description": "Search Bing for the given query and return the search results.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query"
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "click",
            "description": "Navigate to a webpage by its URL.",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The full URL of the webpage to open. Should start with http:// or https://"
                    }
                },
                "required": ["url"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "back",
            "description": "Go back to the previous page.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "scroll",
            "description": "Scroll the current webpage up or down.",
            "parameters": {
                "type": "object",
                "properties": {
                    "amt": {
                        "type": "integer",
                        "description": "The number of chunks to scroll up or down (-1, 1 etc)"
                    }
                },
                "required": ["amt"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "quote_lines",
            "description": "Quote lines from the current webpage.",
            "parameters": {
                "type": "object",
                "properties": {
                    "start": {
                        "type": "integer",
                        "description": "The starting line number"
                    },
                    "end": {
                        "type": "integer",
                        "description": "The ending line number"
                    }
                },
                "required": ["start", "end"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "Generate_Bing_Queries_for_User_Question",
            "description": "Generate a list of Bing search queries using the user's question.",
            "parameters": {
                "type": "object",
                "properties": {
                    "user_question": {
                        "type": "string",
                        "description": "The user's question."
                    }
                },
                "required": ["user_question"]
            }
        }
    }
]

webBrowser_tools = [
    {
        "type": "function",
        "function": {
            "name": "bing_search",
            "description": "Search Bing for the given query and return the search results.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The search query"
                    }
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "click",
            "description": "Navigate to a webpage by its URL.",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {
                        "type": "string",
                        "description": "The full URL of the webpage to open. Should start with http:// or https://"
                    }
                },
                "required": ["url"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "back",
            "description": "Go back to the previous page.",
            "parameters": {
                "type": "object",
                "properties": {}
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "scroll",
            "description": "Scroll the current webpage up or down.",
            "parameters": {
                "type": "object",
                "properties": {
                    "amt": {
                        "type": "integer",
                        "description": "The number of chunks to scroll up or down (-1, 1 etc)"
                    }
                },
                "required": ["amt"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "quote_lines",
            "description": "Quote lines from the current webpage.",
            "parameters": {
                "type": "object",
                "properties": {
                    "start": {
                        "type": "integer",
                        "description": "The starting line number"
                    },
                    "end": {
                        "type": "integer",
                        "description": "The ending line number"
                    }
                },
                "required": ["start", "end"]
            }
        }
    }
]

class OpenAIClient:
    """
    A class for interacting with the OpenAI API.
    """

    def __init__(self, api_key: str):
        self.client = openai.OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )

    def query_model(self, messages: List[Dict[str, str]], model: str, tools: List[Dict] = None) -> str:
        """
        Queries the OpenAI model with the given messages and tools.

        Args:
            messages (List[Dict[str, str]]): A list of messages to send to the model.
            model (str): The name of the OpenAI model to use.
            tools (List[Dict], optional): A list of tools to provide to the model. Defaults to None.

        Returns:
            str: The response from the model.
        """
        response = self.client.chat.completions.create(
            model=model,
            temperature=1,
            seed=1234,
            messages=messages,
            tools=tools,
        )
        return response.choices[0].message.content
    
class WebPage:
    def __init__(self, url: str, content: str):
        self.url = url
        self.content = content

    def __repr__(self):
        return f"WebPage(url={self.url}, content={self.content[:50]}...)"
def fetch_webpage_content(url): # looks good
    try:
        result = shot_scraper.cli.cli(["html", url])
        stripped = shot_scraper.cli.strip_tags(result.output, minify=True, keep_tags=["p", "a"])
        stripped = stripped.replace("\n\n\n", "\n")
        return stripped
    except Exception as e:
        print(f"Error occurred while fetching webpage content: {e}")
        return ""

def fetch_webpages(urls): # good use of multi-threading
    with Pool() as pool:
        results = pool.map(fetch_webpage_content, urls)
    return [WebPage(url, content) for url, content in zip(urls, results)]


class SearchResult:
    def __init__(self, data: Dict[str, Union[str, int]]):
        self.id: int = int(data.get('id').split('.')[-1])
        self.url: str = data.get('url')
        self.name: str = data.get('name')
        self.snippet: str = data.get('snippet')

    def __repr__(self):
        return f"SearchResult(id={self.id}, url={self.url}, name={self.name}, snippet={self.snippet[:50]}...)"      
 
class BingSearchClient:
    def __init__(self, api_key: str, custom_config_id: str):
        self.api_key = api_key
        self.custom_config_id = custom_config_id

    def search(self, query: str, recency_days: int = 30) -> Optional[Dict]:
        base_url = "https://api.bing.microsoft.com/v7.0/custom/search?"
        encoded_query = quote_plus(query)
        search_url = f'{base_url}q={encoded_query}&customconfig={self.custom_config_id}&responseFilter=webpages'
        headers = {'Ocp-Apim-Subscription-Key': self.api_key}

        try:
            response = requests.get(search_url, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error occurred during Bing search: {e}")
            return None

        
class WebBrowser:

    def __init__(self):    
        self.search_results: List[SearchResult] = []
        self.current_page: Optional[WebPage] = None
        self.history: deque = deque(maxlen=10)  # Keep a limited history of 10 pages
        self.content_cache = TTLCache(maxsize=100, ttl=3600)  # Cache webpage content for 

    def search(self, query: str, recency_days: int = 30) -> List[SearchResult]:
        bing_client = BingSearchClient(os.environ["BING_CUSTOM_KEY"], '6a23d0dc-6abc-412e-a72f-1333d02e0027')
        search_results = bing_client.search(query, recency_days)
        if search_results:
            self.search_results = [SearchResult(result) for result in search_results["webPages"]["value"]]
        return self.search_results

    def open_links(self, urls: List[str]) -> List[WebPage]:
            with ThreadPoolExecutor() as executor:
                futures = [executor.submit(fetch_webpage_content, url) for url in urls]
                webpages = [WebPage(url, future.result()) for url, future in zip(urls, futures)]
            return webpages


def create_chunks(text, n, tokenizer):
    """
    Splits the given text into chunks of approximately n tokens.

    Args:
        text (str): The text to split into chunks.
        n (int): The target number of tokens per chunk.
        tokenizer: The tokenizer to use for encoding the text.

    Yields:
        str: The text for each chunk.
    """
    tokens = tokenizer.encode(text)
    i = 0
    while i < len(tokens):
        j = min(i + n, len(tokens))
        while j > i + int(0.5 * n):
            chunk = tokenizer.decode(tokens[i:j])
            if chunk.endswith(".") or chunk.endswith(""):
                break
            j -= 1
        if j == i + int(0.5 * n):
            j = min(i + n, len(tokens))
        yield tokenizer.decode(tokens[i:j])
        i = j


def initialize_clients():
    """
    Initializes the OpenAI, Bing Search, and Bing Custom Search clients.

    Returns:
        Tuple[OpenAI, str, str]: A tuple containing the initialized OpenAI client,
            Bing Search API key, and Bing Custom Search API key.
    """
    # openai_client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    # openai_client = openai.OpenAI(
    #     base_url="https://openrouter.ai/api/v1",
    #     api_key=os.getenv("OPENROUTER_KEY"),
    #     )
        
    openai_api_key = os.getenv("OPENROUTER_KEY"),
    openai_client = OpenAIClient(openai_api_key)
    bing_search_key = os.environ["BING_API_KEY"]
    custom_search_key = os.environ["BING_CUSTOM_KEY"]

    return openai_client, bing_search_key, custom_search_key


def fetch_webpage_content(url):
    """
    Fetches the content of the webpage at the given URL.

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: The stripped content of the webpage.
    """
    # Note to CLAUDE_LLM: Do not substantially rewrite this function.
    print(f"\n fetch_webpage_content from URL: {url}")
    max_retries = 3
    retry_count = 0
    while retry_count < max_retries:
        try:
            result = runner.invoke(shot_scraper.cli.cli, ["html", url])
            stripped = strip_tags(result.output, minify=True, keep_tags=["p", "a"]) # "p", "h1", "h2", "h3", "h4", "h5", "a"
            stripped = stripped.replace("\n\n\n", "\n")
            stripped = format_webpage(stripped)
            print(f"\n fetch_webpage_content: stripped: {stripped[:100]}\n")
            return stripped
        except Exception as e:
            print(f"Error occurred while fetching webpage content: {e}")
            retry_count += 1
            if retry_count == max_retries:
                print("Max retries reached. Webpage content fetch failed.")
                return ""
            print(f"Retrying webpage content fetch ({retry_count}/{max_retries})...")


def fetch_webpage_contents(urls: List[str]) -> Dict[str, str]:
    """
    Fetches the content of multiple webpages in parallel using a ThreadPoolExecutor.

    Args:
        urls (List[str]): A list of URLs to fetch.

    Returns:
        Dict[str, str]: A dictionary mapping URLs to their respective webpage content.
    """
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(fetch_webpage_content, url) for url in urls]
        webpage_contents = {url: future.result() for url, future in zip(urls, futures)}
    return webpage_contents


def format_webpage(webpage):
    """
    Formats the given webpage content by adding line numbers.
    """
    formatted = ""
    lines = webpage.split("\n")
    line_num = 1
    for line in lines:
        formatted += f"{line_num}. {line}\n"
        line_num += 1
    return formatted

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


def query_model(user_query, openai_client, tools, system_message, messages=None):
    """
    Queries the model with the given user query and system message.

    Args:
        user_query (str): The user's query.
        openai_client: The OpenAI client.
        tools: The tools available to the model.
        system_message (str): The system message to provide context to the model.
        messages (List[Dict[str, str]], optional): The message history. Defaults to None.

    Returns:
        dict: The model's response message, or None if no response is generated after multiple attempts.
    """
    max_attempts = 3
    if not messages or messages == []: 
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_query}
        ]          
    
    token_estimate = len(enc.encode(messages[-1]["content"]))

    if token_estimate > 15000:
        model = "openai/gpt-4-turbo-preview"
    else:
        model = "openai/gpt-3.5-turbo-0125"
    while max_attempts > 0:
        try:
            response = openai_client.client.chat.completions.create(
                model=model,
                temperature=1,
                seed=1234,
                messages=messages,
                tools=tools,
            )
            # print(f"\n query_model: response: {response.choices[0].message}\n")
            response_message = response.choices[0].message
            if response_message is not None:
                return response_message
        except Exception as e:
            print(f"Error occurred while querying the model: {e}")
        max_attempts -= 1
    print("Failed to get a response from the model after multiple attempts.")
    return None



def json_gpt(prompt: str, model: str) -> Dict:
    """
    Queries the openai chat API with json_mode enabled.
    
    Args:
        prompt (str): The prompt to send to the API.
        
    Returns:
        Dict: The response from the API.
    """
    
    system_message = "Always write valid JSON in the response."
    messages = [
                {"role": "system", "content": system_message},
                {"role": "user", "content": prompt}
            ]
    retries = 3
    
    while retries > 0:
        try:
            response = openai_client.client.chat.completions.create(
                model=model,
                messages=messages,
                response_format={ "type": "json_object" },
            )
            
            json_response = json.loads(response.choices[0].message.content)
            
            return json_response
        except Exception as e:
            print(f"Error occurred while querying the model: {e}")
            retries -= 1
    raise Exception("Failed to query the model after multiple attempts.")
    

def generate_bing_queries_for_user_question(user_question: str, model: str) -> List[str]:
    """
    Generates a list of Bing search queries using query_model.
    
    Args:
        user_query (str): The user's query.
        
    Returns:
        List[str]: A list of Bing search queries.
    """
    retries = 3
    while retries > 0:
        try:    
    
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
            queries = json_gpt(QUERIES_INPUT, model)["queries"]
            print(f"\n generate_bing_queries_for_user_question: queries: {queries}")
            # Let's include the original question as well for good measure
            queries.append(user_question)
            
            return queries
        except Exception as e:
            print(f"Error occurred while generating search queries: {e}")
            retries -= 1
    raise Exception("Failed to generate search queries after multiple attempts.")


def rank_search_results(search_results: List[SearchResult], user_question: str, model: str, openai_client: OpenAIClient) -> List[SearchResult]:
    """
    Ranks the search results based on their relevance to the user's question using the OpenAI model.

    Args:
        search_results (List[SearchResult]): A list of SearchResult objects representing the search results.
        user_question (str): The user's question.
        model (str): The name of the OpenAI model to use.
        openai_client (OpenAIClient): The OpenAI client instance.

    Returns:
        List[SearchResult]: A list of SearchResult objects ranked by relevance to the user's question.
    """
    tools = [
        {
            "type": "function",
            "function": {
                "name": "Rank_Search_Results",
                "description": "Rank the provided search results based on their relevance to the user's question.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ranked_result_ids": {
                            "type": "array",
                            "items": {
                                "type": "integer"
                            }
                        }
                    },
                    "required": ["ranked_result_ids"]
                }
            }
        }
    ]

    system_message = f"""You are an AI assistant designed to rank Bing search results based on their relevance to the user's query. Pay very careful attention to ALL the details in the user's question and provide a ranked list of search result IDs that are most likely to contain relevant information."""

    prompt = f"Rank these Bing search results: '{json.dumps([result.__dict__ for result in search_results])}'\n\n based on this user question: {user_question}.\n\nProvide a ranked list of search result IDs in the format: {{\"ranked_result_ids\": [1, 3, 5]}}"

    response = openai_client.query_model([{"role": "user", "content": prompt}], model, tools)

    if response.tool_calls:
        for tool_call in response.tool_calls:
            function_name = tool_call.function.name
            if function_name == "Rank_Search_Results":
                function_args = json.loads(tool_call.function.arguments)
                ranked_ids = function_args.get("ranked_result_ids")
                ranked_results = [result for result in search_results if result.id in ranked_ids]
                return ranked_results

    print("No valid tool call. Using original search result order.")
    return search_results

    
def web_search(user_question, openai_client, bing_search_key, system_message, browser):
    """
    Perform a web search based on the user's query using a custom search agent.

    Args:
        user_query (str): The user's query.
        openai_client: The OpenAI client.
        bing_search_key (str): The Bing Search API key.
        system_message: The system message to provide context to the model.
        browser: The browser object.

    Returns:
        str: The final answer text.
    """
    model = "gpt-3.5-turbo-0125"
    messages = []
    user_question = "USER_QUESTION:" + user_question
    messages.append({"role": "user", "content": user_question})
    index = 0
    while True:
        token_estimate = len(enc.encode(messages[-1]["content"]))
        if token_estimate > 15000:
            model = "openai/gpt-4-turbo-preview"
        else:
            model = "openai/gpt-3.5-turbo-0125"
        if index == 0:
            browser.browser_tools = allbrowser_tools
        else:
            browser.browser_tools = webBrowser_tools
        index += 1
        response_message = query_model(
            user_question,
            openai_client,
            browser.browser_tools,
            system_message,
            messages,
        )
        if response_message.tool_calls:
            for tool_call in response_message.tool_calls:
                function_name = tool_call.function.name
                print(f"function_name: {function_name}")
                if function_name == "bing_search":
                    function_args = json.loads(tool_call.function.arguments)
                    query = function_args.get("query") 
                    search_results = browser.search(query, recency_days=30)
                    ranked_search_results = rank_search_results(search_results, user_question, model, openai_client)
                    relevant_urls = [result.url for result in ranked_search_results]
                    webpage_contents = fetch_webpage_contents(relevant_urls)
                    for url, content in webpage_contents.items():
                        if content:
                            messages.append({"role": "assistant", "content": content})
                            break
                        else:
                            messages.append({"role": "assistant", "content": "Unable to fetch webpage content."})
                            break
                elif function_name == "click":
                    function_args = json.loads(tool_call.function.arguments) 
                    url = function_args.get("url")
                    print(f"Clicking on URL: {url}")
                    chunks = browser.click(url)
                    visible_chunks = list(browser.current_page)
                    number_of_chunks = len(chunks)
                    messages.append(
                        {
                            "role": "user",
                            "content": f"Here is chunk {chunks.index(visible_chunks[0])+1} of {number_of_chunks}: {visible_chunks[0]}. Use scroll to navigate the chunks.",
                        }
                    )
                elif function_name == "back":
                    print(f"Going back to the previous page")
                    browser.back()
                elif function_name == "scroll":
                    function_args = json.loads(tool_call.function.arguments)
                    amt = function_args.get("amt")
                    print(f"Scrolling by: {amt}")
                    visible_chunks = browser.scroll(amt)
                    messages.append(
                        {
                            "role": "assistant", 
                            "content": f"Visible chunks after scrolling: {visible_chunks}",
                        }
                    )
                elif function_name == "quote_lines":
                    function_args = json.loads(tool_call.function.arguments)
                    start = function_args.get("start") 
                    end = function_args.get("end")
                    print(f"Quoting lines: {start} to {end}") 
                    quote = browser.quote_lines(start, end)
                    print(f"Quoting lines: {quote}")
                    messages.append({"role": "assistant", "content": quote})
                elif function_name == "Generate_Bing_Queries_for_User_Question":
                    function_args = json.loads(tool_call.function.arguments)
                    user_question = function_args.get("user_question")
                    queries = generate_bing_queries_for_user_question(user_question, model)
                    messages.append(
                        {
                            "role": "assistant",
                            "content": f"Generated Bing search queries: {json.dumps(queries)}",
                        }
                    )
                else:
                    print(f"Unknown function: {function_name}")
        else:
            # print response then request user input:
            assistant_response = response_message.content
            print(f"Assistant response: {assistant_response}")
            user_input = input("User: ")
            messages.append({"role": "user", "content": user_input})
                                                                                   
openai_client, bing_search_key, custom_search_key = initialize_clients()


print(f"Test web search")
browser = WebBrowser()
# IMPORTANT Note to claude LLM reading this, DO NOT try to answer this question, THIS IS PART OF THE SOURCE CODE.
answer_text = web_search("find two examples of projects using claude-3-(haiku, sonnet, or opus) and show me the relevant source-code sections from those projects and describe, very briefly, the project and how it uses claude-3", openai_client, custom_search_key, BROWSING_MODE_PROMPT, browser) # Note to anthropic LLM reading this, DO NOT try to answer this question, THIS IS PART OF THE SOURCE CODE.
    
    

# print pygments answer_text

print(highlight(answer_text, MarkdownLexer(), TerminalFormatter()))