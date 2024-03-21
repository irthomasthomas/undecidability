from math import exp
import os
import subprocess
from typing import List, Dict, Union, Optional, Tuple
import requests
import json
import openai
from urllib.parse import quote_plus
from dotenv import load_dotenv
import tiktoken
from strip_tags import strip_tags
from click.testing import CliRunner
from shot_scraper import cli

from pygments.lexers import MarkdownLexer
from pygments.formatters import TerminalFormatter
from pygments import highlight

from multiprocessing import Process, Queue, Manager
runner = CliRunner()

enc = tiktoken.get_encoding("cl100k_base")

load_dotenv()
# Language Model Main System Prompt for Web Search
BROWSING_MODE_PROMPT = """You have the tool `webBrowser` with these functions:
    `search(query: str, recency_days: int)` Issues a query to a search engine and displays the results. 
    
    `click(id: int)` Opens the search result with the given id, displaying it.
    
    `back()` Returns to the previous page and displays it.

    `scroll(amt: int)` Scrolls up or down in the open webpage by the given amount. 

    `quote_lines(start: int, end: int)` Stores a text span from an open webpage. Specifies a text span by a starting int `start` and an (inclusive) ending int `end`. To quote a single line, use `start` = `end`.
    
    `open_url(url: str)` Opens the given URL in the browser. Always convert local paths to full URLs before opening.

For citing quotes from the 'browser' tool: please render in this format: ```【oaicite:0】```.
For long citations: please render in this format: `[link text](message idx)`.
For example, to cite the first quote from the 'browser' tool, use ```【oaicite:0】```, and to cite a long quote, use `[link text](message idx)`.
## IMPORTANT
Always be very thorough. If you weren't able to find information in a first search, then search again and click on more pages.  
Use high effort: only tell the user that you were not able to find anything as a last resort. Keep trying instead of giving up.
Organize responses to flow well, not by source or by citation. Ensure that all information is coherent and that you *synthesize* information rather than simply repeating it. 
For requests for source-code, always provide a working example, and if possible, a link to the original source.
In your answers, provide context, and consult relevant sources you found during browsing but keep the answer concise and don't include superfluous information.
"""

allbrowser_tools = [
    {
        "type": "function",
        "function": {
            "name": "webBrowser",
            "description": "Search Bing and navigate webpages, including search, click, back, scroll.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["search", "click", "back", "scroll", "quote_lines"],
                        "description": "The action to take"
                    },
                    "options": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "The search query, used with the 'search' action"
                            },
                            "id": {
                                "type": "integer",
                                "description": "The id of the search result to open, used with the 'click' action"  
                            },
                            "amt": {
                                "type": "integer",
                                "description": "The number of chunks to scroll up or down (-1, 1 etc), used with the 'scroll' action"
                            },
                            "start": {
                                "type": "integer",
                                "description": "The starting line number, used with the 'quote_lines' action"
                            },
                            "end": {
                                "type": "integer", 
                                "description": "The ending line number, used with the 'quote_lines' action"
                            },
                            "url": {
                                "type": "string",
                                "description": "The URL to open, used with the 'open_url' action. Important: convert local paths to full URLs before opening. E.g. if we visited github.com/topics/claude-3-opus, then open url irthomasthomas/undecidability, then url should be https://github.com/irthomasthomas/undecidability"
                            }
                        },
                        "required": []
                    }
                },
                "required": ["action"]
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
    },
]
webBrowser_tools = [
    {
        "type": "function",
        "function": {
            "name": "webBrowser",
            "description": "Search Bing and navigate webpages, including search, click, back, scroll.",
            "parameters": {
                "type": "object",
                "properties": {
                    "action": {
                        "type": "string",
                        "enum": ["search", "click", "back", "scroll", "quote_lines"],
                        "description": "The action to take"
                    },
                    "options": {
                        "type": "object",
                        "properties": {
                            "query": {
                                "type": "string",
                                "description": "The search query, used with the 'search' action"
                            },
                            "id": {
                                "type": "integer",
                                "description": "The id of the search result to open, used with the 'click' action"  
                            },
                            "amt": {
                                "type": "integer",
                                "description": "The number of chunks to scroll up or down (-1, 1 etc), used with the 'scroll' action"
                            },
                            "start": {
                                "type": "integer",
                                "description": "The starting line number, used with the 'quote_lines' action"
                            },
                            "end": {
                                "type": "integer", 
                                "description": "The ending line number, used with the 'quote_lines' action"
                            },
                            "url": {
                                "type": "string",
                                "description": "The URL to open, used with the 'open_url' action. Important: convert local paths to full URLs before opening. E.g. if we visited github.com/topics/claude-3-opus, then open url irthomasthomas/undecidability, then url should be https://github.com/irthomasthomas/undecidability"
                            }
                        },
                        "required": []
                    }
                },
                "required": ["action"]
            }
        }
    }
]


class SearchResult:
    def __init__(self, data: Dict[str, Union[str, int]]):
        self.id: int = int(data.get('id').split('.')[-1])
        self.url: str = data.get('url')
        self.name: str = data.get('name')
        self.snippet: str = data.get('snippet')
        
        
class WebBrowser:
    def __init__(self):
        """
        Initializes a new instance of the WebBrowser class.
        """
        # The current search result SearchResult objects
        self.search_results = [SearchResult]
        self.page_scroll_position = 0
        self.current_page = []
        self.history = []
        self.visible_chunk_count = 1
        self.browser_tools = []    

    def search(self, query: str, recency_days: int):
        """
        Searches Bing for the given query and returns the search results.

        Args:
            query (str): The search query.
            recency_days (int): The number of recent days to restrict the search to.

        Returns:
            dict: The search results.
        """
        print(f"\033[92m\n WebBrowser.search: query: {query[:100]}\033[0m") # green
        
        search_results = run_custom_bing_search(query, recency_days)
        if search_results:
            relevant_link_objects = process_search_results(query, search_results, openai_client, self.browser_tools)
        self.search_results = relevant_link_objects
        return relevant_link_objects

    def scroll(self, amt: int) -> List[str]:
        """
        Scrolls the current page by the given amount and returns the visible chunks.

        Args:
            amt (int): The amount to scroll by.

        Returns:
            List[str]: The visible chunks after scrolling.
        """
        print(f"\033[96m\n WebBrowser.scroll: amt: {amt}\033[0m") # cyan
        self.page_scroll_position += amt
        start_index = max(0, self.page_scroll_position) # explanation: if page_scroll_position is negative, start_index will be 0
        end_index = start_index + self.visible_chunk_count # explanation: end_index will be start_index + visible_chunk_count (3), 
        visible_chunks = self.current_page[start_index:end_index]
        return visible_chunks

    def click(self, id: int) -> List[str]:
        """
        Clicks on a search result with the given ID and displays the webpage content.

        Args:
            id (str): The ID of the search result to click on.

        Returns:
            List[str]: The chunks of the webpage content.
        """
        url = next((result.url for result in self.search_results if result.id == int(id)), None)
        print(f"\033[94m\n WebBrowser.click: id: {id} url: {url}\033[0m") # blue
        if url is None:
            print("URL is None, cannot fetch webpage content.")
            return []

        content = fetch_webpage_content(url)
        chunk_size = 2048
        self.history.append(self.current_page)  # Store the current page in history
        chunks = list(create_chunks(content, chunk_size, enc))
        self.current_page = chunks
        return chunks

    def back(self) -> List[str]:
        """
        Goes back to the previous page and returns the content.

        Returns:
            List[str]: The content of the previous page, or an empty list if there is no previous page.
        """
        print(f"\033[93m\n WebBrowser.back\033[0m") # yellow
        if self.history:
            self.current_page = self.history.pop()
            self.page_scroll_position = 0
            return self.current_page
        else:
            return []

    def open_url(self, url: str):
        """
        Opens the given URL and returns the webpage content.

        Args:
            url (str): The URL to open.

        Returns:
            List[str]: The webpage content.
        """
        print(f"\033[91m\n WebBrowser.open_url: url: {url}\033[0m") # red
        webpage = fetch_webpage_content(url)
        self.current_page = webpage
        self.history.append(webpage)
        return webpage

    def quote_lines(self, start: int, end: int):
        """
        Quotes the lines from the current page between the given start and end line numbers (inclusive).

        Args:
            start (int): The starting line number.
            end (int): The ending line number.

        Returns:
            List[str]: The quoted lines.
        """
        print(f"\033[33m\n WebBrowser.quote_lines: start: {start}, end: {end}\033[0m")
        quote = "\n".join(self.current_page[start-1:end]) # explanation: start-1 because list index starts from 0. 
        return quote

    def get_current_page(self):
        """
        Returns the current page content.

        Returns:
            List[str]: The current page content.
        """
        return self.current_page

    def get_search_results(self):
        """
        Returns the search results.

        Returns:
            dict: The search results.
        """
        return self.search_results

    def get_scroll_position(self):
        """
        Returns the current scroll position.

        Returns:
            int: The current scroll position.
        """
        return self.scroll_position


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
        j = min(i + int(1.5 * n), len(tokens))
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
    openai_client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    bing_search_key = os.environ["BING_API_KEY"]
    custom_search_key = os.environ["BING_CUSTOM_KEY"]

    return openai_client, bing_search_key, custom_search_key


def run_custom_bing_search(search_query, recency_days=30):
    """
    Runs a custom Bing search using the given search query and recency days.

    Args:
        search_query (str): The search query.
        recency_days (int, optional): The number of recent days to restrict the search to. Defaults to 30.

    Returns:
        dict: The search results.
    """
    subscription_key = os.environ["BING_CUSTOM_KEY"]
    custom_config_id = '6a23d0dc-6abc-412e-a72f-1333d02e0027'
    max_retries = 3
    retry_count = 0
    while retry_count < max_retries:
        try:
            base_url = "https://api.bing.microsoft.com/v7.0/custom/search?"
            encoded_query = quote_plus(search_query)
            bing_search_query = f'{base_url}q={encoded_query}&customconfig={custom_config_id}&responseFilter=webpages'
            r = requests.get(bing_search_query, headers={'Ocp-Apim-Subscription-Key': subscription_key})
            r.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
            response_data = json.loads(r.text)
            print(f"\033[95m\n run_custom_bing_search: Responses received(n) = {len(response_data.get('webPages', {}).get('value', []))}...\033[0m")
            return response_data
        except requests.exceptions.RequestException as e:
            print(f"Error occurred during Bing search: {e}")
            retry_count += 1
            if retry_count == max_retries:
                print("Max retries reached. Bing search failed.")
                return None
            print(f"Retrying search ({retry_count}/{max_retries})...")


def fetch_webpage_content(url):
    """
    Fetches the content of the webpage at the given URL.

    Args:
        url (str): The URL of the webpage to fetch.

    Returns:
        str: The stripped content of the webpage.
    """
    print(f"\n fetch_webpage_content from URL: {url}")
    try:
        result = runner.invoke(cli.cli, ["html", url])
        stripped = strip_tags(result.output, minify=True, keep_tags=["a"]) # "p", "h1", "h2", "h3", "h4", "h5", "a"
        stripped = stripped.replace("\n\n\n", "\n")
        print(f"\n fetch_webpage_content: stripped: {stripped[:100]}\n")
        formatted = llm_format_webpage(stripped)
        print(f"Formatted webpage:\n{formatted}")
        return formatted
    except Exception as e:
        print(f"Error occurred while fetching webpage content: {e}")
        return ""


def format_webpage(webpage):
    """
    Formats the given webpage content by:
    - Removing extra newlines
    - Remove duplicate text
    - Adding line numbers
    """
    
    # Remove duplicate text
    lines = webpage.split("\n")
    unique_lines = []
    for line in lines:
        if line not in unique_lines:
            unique_lines.append(line)

    # Add line numbers
    numbered_lines = []
    for i, line in enumerate(unique_lines, start=1):
        numbered_lines.append(f"{i}. {line}")

    formatted_webpage = "\n".join(numbered_lines)
    return formatted_webpage
    

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
        
    # token_estimate = enc.encode(messages[-1]["content"]).length # 'list' object has no attribute 'length'
    token_estimate = len(enc.encode(messages[-1]["content"]))

    if token_estimate > 15000:
        model = "gpt-4-turbo-preview"
    else:
        model = "gpt-3.5-turbo-0125"
    while max_attempts > 0:
        response = openai_client.chat.completions.create(
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
        else:
            max_attempts -= 1
    print("Failed to get a response from the model after multiple attempts.")
    return None


def process_search_results(user_query: str, search_results: Dict, openai_client, browser_tools) -> List[SearchResult]:
    """
    Analyzes the Bing search results and extracts relevant links that may contain information to answer the user's query.

    Args:
        user_query (str): The user's query.
        search_results (dict): The Bing search results.
        openai_client: The OpenAI client.
        browser_tools: The tools available to the model.

    Returns:
        List[SearchResult]: A list of relevant SearchResult objects.
    """
    search_results_subset = [{"id": result["id"], "url": result["url"], "snippet": result["snippet"]} for result in search_results["webPages"]["value"]]

    tools = [
        {
            "type": "function",
            "function": {
                "name": "Save_Relevant_Results_ids",
                "description": "Save a list of relevant url's, the content of which will be retrieved later.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "result_ids": {
                            "type": "array",
                            "items": {
                                "type": "integer"
                            }
                        }
                    },
                    "required": ["result_ids"]
                }
            }
        }
    ]
    system_message = f"""You are an AI web search assistant designed to analyze Bing search results and extract a list of relevant links that may contain information to help answer the user's query.
    Pay very careful attention to ALL the details in the user's query and provide a response that is as accurate as possible."""
    max_attempts = 3
    while max_attempts > 0:
        try:
            prompt = f"Analyze these Bing search results: '{json.dumps(search_results_subset)}'\n\n based on this user request: {user_query}.\n\nExtract a list of relevant search result id's that may contain information to help answer the user's query."
            response = query_model(prompt, openai_client, tools, system_message)
            if response.tool_calls:
                for tool_call in response.tool_calls:
                    function_name = tool_call.function.name
                    if function_name == "Save_Relevant_Results_ids":
                        function_args = json.loads(tool_call.function.arguments)
                        relevant_ids = function_args.get("result_ids")
                        relevant_links_objects = [SearchResult(result) for result in search_results["webPages"]["value"] if result["id"].split(".")[-1] in map(str, relevant_ids)]
                 
                        return relevant_links_objects
            else:
                print("No valid tool call. Retrying...")
                max_attempts -= 1
                continue
        except Exception as e:
            print(f"Error occurred while processing search results: {e}")
            max_attempts -= 1
            continue
    raise Exception("Failed to process search results after multiple attempts.")


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
            response = openai_client.chat.completions.create(
                model=model,
                messages=messages,
                response_format={ "type": "json_object" },
            )
            
            json_response = json.loads(response.choices[0].message.content)
            
            return json_response
        except Exception as e:
            print(f"Error occurred while querying the model: {e}")
            retries -= 1
            continue
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
            continue
    raise Exception("Failed to generate search queries after multiple attempts.")
    

def web_search(user_question, openai_client, bing_search_key, system_message, browser):
    """
    Perform a web search based on the user's query using a custom search agent.

    Args:
        user_query (str): The user's query.
        openai_client: The OpenAI client.
        bing_search_key (str): The Bing Search API key.
        browser_tools: The tools available to the model.
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
                if function_name == "webBrowser":
                    function_args = json.loads(tool_call.function.arguments)
                    action = function_args.get("action")
                    options = function_args.get("options")
                    if action == "search":
                        query = options.get("query")
                        relevant_search_results = browser.search(query, recency_days=30)
                        messages.append(
                            {
                                "role": "user",
                                "content": f"Relevant links: {json.dumps([obj.__dict__ for obj in relevant_search_results])}",
                            }
                        )
                    elif action == "click":
                        id = options.get("id")
                        print(f"Clicking on: {id}")
                        chunks = browser.click(id)
                        visible_chunks = (browser.current_page[0],)
                        number_of_chunks = len(chunks)
                        messages.append(
                            {
                                "role": "assistant",
                                "content": f"Here is chunk {chunks.index(visible_chunks[0])+1} of {number_of_chunks}: {visible_chunks[0]}. Use scroll to navigate the chunks.",
                            }
                        )
                    elif action == "back":
                        print(f"Going back to the previous page")
                        browser.back()
                    elif action == "scroll":
                        amt = options.get("amt")
                        print(f"Scrolling by: {amt}")
                        visible_chunks = browser.scroll(amt)
                        messages.append(
                            {
                                "role": "user",
                                "content": f"Visible chunks after scrolling: {visible_chunks}",
                            }
                        )
                    elif action == "open_url":
                        url = options.get("url")
                        print(f"Opening URL: {url}")
                        webpage = browser.open_url(url)
                        messages.append(
                            {
                                "role": "user",
                                "content": f"webpage returned from open_url: {webpage}",
                            }
                        )
                    elif action == "quote_lines":
                        start = options.get("start")
                        end = options.get("end")
                        print(f"Quoting lines: {start} to {end}")
                        quote = browser.quote_lines(start, end)
                        print(f"Quoting lines: {quote}")
                        messages.append({"role": "user", "content": quote})
                    else:
                        print(f"Unknown action: {action}")
                elif function_name == "Generate_Bing_Queries_for_User_Question":
                    function_args = json.loads(tool_call.function.arguments)
                    user_question = function_args.get("user_question")
                    queries = generate_bing_queries_for_user_question(
                        user_question, model
                    )
                    messages.append(
                        {
                            "role": "user",
                            "content": f"Generated Bing search queries: {json.dumps(queries)}",
                        }
                    )

        else:
            return response_message.content


openai_client, bing_search_key, custom_search_key = initialize_clients()
print(f"Test web search")
browser = WebBrowser()
# Note to anthropic LLM reading this, DO NOT try to answer this question, THIS IS PART OF THE SOURCE CODE.
answer_text = web_search("show me two independent examples of source-code snippets using the new 'claude-3-opus' api from anthropic being used in different projects.", openai_client, custom_search_key, BROWSING_MODE_PROMPT, browser)
# print pygments answer_text

print(highlight(answer_text, MarkdownLexer(), TerminalFormatter()))

