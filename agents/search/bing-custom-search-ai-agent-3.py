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

from multiprocessing import Process, Queue, Manager
runner = CliRunner()

enc = tiktoken.get_encoding("cl100k_base")

load_dotenv()
# Language Model Main System Prompt for Web Search
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

# Simplify and merge the allbrowser / webBrowser_tools logic. Instead of having all the tools combined in each list, lets assemble them from the functions as needed.
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
            "name": "open_bing_result",
            "description": "Open a Bing search result by its ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "The ID of the webpage to open from search results"
                    }
                },
                "required": ["id"]
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
            "name": "open_bing_result",
            "description": "Open a Bing search result by its ID.",
            "parameters": {
                "type": "object",
                "properties": {
                    "id": {
                        "type": "integer",
                        "description": "The ID of the webpage to open from search results"
                    }
                },
                "required": ["id"]
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
        """
        Initializes a new instance of the WebBrowser class.
        """
        self.search_results = [SearchResult]
        self.page_scroll_position = 0
        self.current_page = self.webpage()
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
        start_index = max(0, self.page_scroll_position) 
        end_index = min(start_index + self.visible_chunk_count, len(self.current_page))
        visible_chunks = self.current_page[start_index:end_index]
        return visible_chunks

    def open_bing_result(self, id: int):
        """
        Opens a link from the search results with the given ID and displays the webpage content.

        Args:
            id (str): The ID of the search result link to open.

        Returns:
            List[str]: The chunks of the webpage content.
        """
        url = next((result.url for result in self.search_results if result.id == int(id)), None)
        print(f"\033[94m\n WebBrowser.open_bing_result: id: {id} url: {url}\033[0m") # blue
        if url is None:
            print("URL is None, cannot fetch webpage content.")
            return []

        return self.click(url)
    
    def click(self, url: str):
        """
        Opens the webpage at the given URL and displays the content. 

        Args:
            url (str): The full URL of the webpage to open. Should start with http:// or https://
        
        Returns:
            List[str]: The chunks of the webpage content.
        """
        print(f"\033[94m\n WebBrowser.click: url: {url}\033[0m") # blue
        
        if not url.startswith("http://") and not url.startswith("https://"):
            if self.current_page:
                url = urljoin(self.current_page[0], url)
            else:
                print("Cannot convert relative URL to absolute URL without current page.")
                return []
        
        content = fetch_webpage_content(url)
        chunk_size = 2048
        self.history.append(self.current_page) 
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
        quote = "\n".join(self.current_page[start-1:end])  # Access the content attribute
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
    openai_client = openai.OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_KEY"),
        )
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
    max_retries = 3
    retry_count = 0
    while retry_count < max_retries:
        try:
            result = runner.invoke(cli.cli, ["html", url])
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


def format_webpage(webpage: str) -> str:
    """
    Formats the given webpage content by:
    - Removing extra newlines
    - Adding paragraph breaks
    - Adding line numbers
    
    Args:
        webpage (str): The webpage content to format.
    Returns:
        str: The formatted webpage content.    
    """
    lines = webpage.split("\n")
    formatted_lines = []
    line_number = 1
    
    for line in lines:
        line = line.strip()
        if line:
            formatted_lines.append(f"{line_number}. {line}")
            line_number += 1
        else:
            formatted_lines.append("")
    
    formatted_webpage = "\n\n".join(formatted_lines)
    return formatted_webpage
    
    

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
            response = openai_client.chat.completions.create(
                model=model,
                temperature=1,
                seed=1234,
                messages=messages,
                tools=tools,
            )
            #{'message': '{\n  "error": {\n    "message": "This model\'s maximum context length is 16385 tokens. However, you requested 16610 tokens (14138 in the messages, 226 in the functions, and 2246 in the completion). Please reduce the length of the messages, functions, or completion.",\n    "type": "invalid_request_error",\n    "param": "messages",\n    "code": "context_length_exceeded"\n  }\n}\n', 'code': 400}
            
            response_message = response.choices[0].message
            
            if response_message is not None:
                return response_message
        except Exception as e:
            # check if response contains message about context length:
            if "context_length_exceeded" in str(e):
                model = "openai/gpt-4-turbo-preview"
                max_attempts -= 1
                
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
    if 'webPages' not in search_results or 'value' not in search_results['webPages']:
        print("No web pages found in the search results.")
        return []

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
        except Exception as e:
            print(f"Error occurred while processing search results: {e}")
        max_attempts -= 1
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
    # Tofix: use better context management and parallellism to improve speed and reduce token usage. 
    # e.g. after sending  a webpage to be analyzed and recieving a request to quote a section, do not resend that full webpage in future messages, only the quoted section. 
    # Also maintain a message status that summarises the actions taken so far and the present status. i.e. which page, which chunk of chunk visible, and anything else apropriate to help manage state without sending everything with every request, as happens now.
    # read from /home/thomas/OPENROUTER_KEY
    with open('/home/thomas/OPENROUTER_KEY') as f:
        OPENROUTER_KEY = f.read()
        
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
        # The following can be simplified greatly, by directly calling, instead of the complex if/else:
        if response_message.tool_calls:
            for tool_call in response_message.tool_calls:
                function_name = tool_call.function.name
                print(f"function_name: {function_name}")
                if function_name == "bing_search":
                    function_args = json.loads(tool_call.function.arguments)
                    query = function_args.get("query") 
                    relevant_search_results = browser.search(query, recency_days=30)
                    messages.append(
                        {
                            "role": "user",
                            "content": f"Relevant links: {json.dumps([obj.__dict__ for obj in relevant_search_results])}",
                        }
                    )
                elif function_name == "open_bing_result":
                    function_args = json.loads(tool_call.function.arguments)
                    id = function_args.get("id")
                    print(f"Opening link: {id}")
                    chunks = browser.open_bing_result(int(id))
                    visible_chunks = (browser.current_page[0],)
                    number_of_chunks = len(chunks)
                    messages.append(
                        {
                            "role": "user",
                            "content": f"Here is chunk {chunks.index(visible_chunks[0])+1} of {number_of_chunks}: {visible_chunks[0]}. Use scroll to navigate the chunks.",
                        }
                    )
                elif function_name == "click": # Tofix: We should not continually append to messages here, but only send the original question, a summary of actions so far, and the page chunk returned from the click request.
                    function_args = json.loads(tool_call.function.arguments) 
                    url = function_args.get("url")
                    print(f"Clicking on URL: {url}")
                    chunks = browser.click(url)
                    visible_chunks = list(browser.current_page)
                    number_of_chunks = len(chunks)
                    if visible_chunks:
                        messages.append(
                            {
                                "role": "user",
                                "content": f"Here is chunk {chunks.index(visible_chunks[0])+1} of {number_of_chunks}: {visible_chunks[0]}. Use scroll to navigate the chunks.",
                            }
                        )
                    else:
                        messages.append(
                            {
                                "role": "user",
                                "content": "The webpage content is empty.",
                            }
                        )

                elif function_name == "back":
                    print(f"Going back to the previous page")
                    browser.back()
                elif function_name == "scroll": # Tofix: should handle negative scrolling.
                    # Needs better thread message managment for long scrolls. 
                    # Do not resend the entire message history, only the original request, a summary of the actions so far, and the current visible content after the scroll.
                    function_args = json.loads(tool_call.function.arguments)
                    amt = function_args.get("amt")
                    print(f"Scrolling by: {amt}")
                    visible_chunks = browser.scroll(amt)
                    if visible_chunks:
                        messages.append(
                            {
                                "role": "assistant", 
                                "content": f"Visible chunks after scrolling: {visible_chunks}",
                            }
                        )
                    else:
                        messages.append(
                            {
                                "role": "assistant",
                                "content": "No visible chunks after scrolling.",
                            }
                        )
                elif function_name == "quote_lines": # tofix: thread management to reduce token use.
                    function_args = json.loads(tool_call.function.arguments)
                    start = function_args.get("start") 
                    end = function_args.get("end")
                    print(f"Quoting lines: {start} to {end}") 
                    quote = browser.quote_lines(start, end)
                    print(f"Quoting lines: {quote[:140]}")
                    # This should be appended to a new thread seperate to the main message thread.
                    # We need better thread managment in the future.
                    messages.append({"role": "assistant", "content": quote})
                elif function_name == "Generate_Bing_Queries_for_User_Question": # tofix:
                    function_args = json.loads(tool_call.function.arguments)
                    user_question = function_args.get("user_question")
                    queries = generate_bing_queries_for_user_question(user_question, model)
                    messages.append(
                        {
                            "role": "assistant",
                            "content": f"Generated Bing search queries: {json.dumps(queries)}",
                        }
                    )
                    # Now call browser.search in parallell threads for each query and append results to messages for each query, and appending the query text to the top.
                    # after performing the searches in parallell, join the search_result to the query and call the LLM in parallell again for each one to look for relevant results from each result.
                    # finally merge all relevant chosen results into a new message thread.
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

answer_text = web_search("example question needing a web search to answer.",
                         openai_client, custom_search_key, BROWSING_MODE_PROMPT, browser)
    
    
print(highlight(answer_text, MarkdownLexer(), TerminalFormatter()))