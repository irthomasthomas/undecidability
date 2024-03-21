import asyncio
import json
import os
from typing import List, Dict, Union, Optional

import aiohttp
import openai
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import tiktoken

load_dotenv()

enc = tiktoken.get_encoding("cl100k_base")
openai_client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_KEY"),
)

BROWSING_MODE_PROMPT = """You have a 'browser' tool with access to the following functions for browsing and searching the internet:
    `bing_search(query: str)` Issues a query to a search engine and displays the results. 
    
    `open_result(id: str)` Opens the webpage with the given id from the search results, displaying it.
    
    `click(url: str)` Opens the webpage with the given full URL, displaying it. The URL should be a fully qualified URL starting with http:// or https://.
    
    `back()` Returns to the previous page and displays it.

    `scroll(amt: int)` Scrolls up or down in the open webpage by the given amount. 

    `quote(start: int, end: int)` Stores a text span from an open webpage. start and end are inclusive line numbers. To quote a single line, use `start` = `end`.

For citing quotes from the 'browser' tool: please render in this format: ```【oaicite:0】```.
For long citations: please render in this format: `[link text](#0)`.
Always be very thorough in your search. If you weren't able to find information in a first search, search again and click on more pages.  
Use high effort and only tell the user that you were not able to find anything as a last resort. Keep trying instead of giving up.
Organize responses to flow well, not by source or by citation. Ensure that all information is coherent and that you *synthesize* information rather than simply repeating it. 
For requests for source-code, provide a working example that blends your findings with the user's request, incorporate their data if relevant, and include a link to the original source.
Provide context in your answers, and consult relevant sources found during browsing, but keep answers concise and avoid superfluous information.
"""

def truncate(text: str, max_length: int, truncate_str: str = "...") -> str:
    """Truncates text to max_length characters, adding truncate_str at the end if truncated."""
    return text[:max_length] + (truncate_str if len(text) > max_length else "")

class SearchResult:
    def __init__(self, data: Dict[str, Union[str, int]]):
        self.id: int = int(data["id"])
        self.url: str = data["url"]
        self.title: str = data["title"]
        self.snippet: str = data["snippet"]

class WebBrowser:
    def __init__(self):
        self.search_results: List[SearchResult] = []
        self.result_pages: List[List[str]] = []
        self.current_page_index: int = -1
        self.current_scroll_position: int = 0

    async def bing_search(self, query: str) -> List[SearchResult]:
        async with aiohttp.ClientSession() as session:
            subscription_key = os.environ["BING_CUSTOM_KEY"]
            custom_config_id = "6a23d0dc-6abc-412e-a72f-1333d02e0027"
            base_url = "https://api.bing.microsoft.com/v7.0/custom/search?"
            search_url = f"{base_url}q={query}&customconfig={custom_config_id}&responseFilter=webpages" 
            async with session.get(search_url, headers={"Ocp-Apim-Subscription-Key": subscription_key}) as resp:
                data = await resp.json()
                self.search_results = [SearchResult(result) for result in data["webPages"]["value"]]
                return self.search_results

    async def open_result(self, id: int) -> List[str]:
        result = next((r for r in self.search_results if r.id == id), None)
        if result:
            page_text = await self._fetch_page_text(result.url)
            self.result_pages.append(self._split_into_chunks(page_text))
            self.current_page_index = len(self.result_pages) - 1
            return self.result_pages[-1]
        else:
            return []

    async def click(self, url: str) -> List[str]:
        page_text = await self._fetch_page_text(url)
        self.result_pages.append(self._split_into_chunks(page_text))
        self.current_page_index = len(self.result_pages) - 1
        return self.result_pages[-1]

    def back(self) -> List[str]:
        if self.current_page_index > 0:
            self.current_page_index -= 1
            self.current_scroll_position = 0
        return self.result_pages[self.current_page_index]

    def scroll(self, amt: int) -> List[str]:
        current_page = self.result_pages[self.current_page_index]
        self.current_scroll_position = max(0, min(self.current_scroll_position + amt, len(current_page) - 1))
        return [current_page[self.current_scroll_position]]

    def quote(self, start: int, end: int) -> str:
        current_page = self.result_pages[self.current_page_index]
        return "\n".join(current_page[start-1:end])

    def _split_into_chunks(self, text: str, chunk_size: int = 2048) -> List[str]:
        return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

    @staticmethod
    async def _fetch_page_text(url: str) -> str:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                html = await resp.text()
                soup = BeautifulSoup(html, "html.parser")
                for script in soup(["script", "style"]):
                    script.extract() 
                text = soup.get_text()
                lines = (line.strip() for line in text.splitlines())
                return "\n".join(line for line in lines if line)


async def query_model(system_prompt: str, browser_tools: List[Dict], user_message: str, messages: List[Dict]):
    model = "openai/gpt-3.5-turbo-0125"
    token_estimate = len(enc.encode(messages[-1]["content"]))

    if token_estimate > 15000:
        model = "openai/gpt-4-turbo-preview"
    
    messages = [{"role": "system", "content": system_prompt}] + messages
    
    # Retry with exponential backoff
    for attempt in range(3):
        try:
            response = openai_client.chat.completions.create(
                model=model,
                temperature=1,
                seed=1234,
                messages=messages,
                tools=browser_tools,
            )
            
            response_message = response.choices[0].message
            if response_message:
                return response_message
        except openai.error.RateLimitError:
            delay = 2 ** attempt
            print(f"Rate limit exceeded. Retrying in {delay} seconds...")
            await asyncio.sleep(delay) # 

    raise Exception("Failed to get response from model after multiple attempts")

def generate_bing_queries(user_question: str) -> List[str]:
    input_prompt = f"""
    Generate an array of 3-5 search queries relevant to this question.
    Use related keywords and advanced Bing search operators.
    Be creative - better queries improve the likelihood of finding relevant information.
    
    User question: {user_question}
    
    Format the output as a JSON array of strings, e.g.: ["query 1", "query 2", "query 3"]
    """
    # Missing required arguments; Expected either ('model' and 'prompt') or ('model', 'prompt' and 'stream') arguments to be given
    response = openai_client.completions.create(
        engine="openai/gpt-3.5-turbo-0125",
        prompt=input_prompt,
        max_tokens=200,  
        n=1,
        stop=None,
        temperature=0.8,
        response_format="text",
    )
    
    try:
        queries = json.loads(response.choices[0].text)
        queries.append(user_question)  # Include the original question
        return queries
    except json.JSONDecodeError:
        print("Failed to parse JSON response from model")
        return [user_question]

async def web_search(user_question: str, browser: WebBrowser) -> str:
    queries = generate_bing_queries(user_question)

    search_tasks = [browser.bing_search(query) for query in queries]
    search_results = await asyncio.gather(*search_tasks)
    search_results = [item for sublist in search_results for item in sublist]  # Flatten list

    messages = [{"role": "user", "content": f"USER_QUESTION: {user_question}"}]

    while True:
        browser_tools = [
            {
                "type": "function",
                "function": {
                    "name": tool["name"], 
                    "description": tool["description"],
                    "parameters": tool["parameters"],
                }
            }
            for tool in [
                {
                    "name": "bing_search",
                    "description": "Search Bing for the given query.",
                    "parameters": {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]},
                },
                {
                    "name": "open_result",
                    "description": "Open a search result by ID.",
                    "parameters": {"type": "object", "properties": {"id": {"type": "integer"}}, "required": ["id"]},
                },
                {
                    "name": "click", 
                    "description": "Navigate to a URL.",
                    "parameters": {"type": "object", "properties": {"url": {"type": "string"}}, "required": ["url"]},
                },
                {
                    "name": "back",
                    "description": "Go back to the previous page.",
                    "parameters": {"type": "object", "properties": {}},
                },
                {
                    "name": "scroll",
                    "description": "Scroll the current page.", 
                    "parameters": {"type": "object", "properties": {"amt": {"type": "integer"}}, "required": ["amt"]},
                },
                {
                    "name": "quote",
                    "description": "Quote lines from the current page.", 
                    "parameters": {
                        "type": "object",
                        "properties": {"start": {"type": "integer"}, "end": {"type": "integer"}},
                        "required": ["start", "end"],
                    },    
                },
            ]
        ]
        
        response_message = query_model(BROWSING_MODE_PROMPT, browser_tools, user_question, messages)

        if response_message.tool_calls:
            for call in response_message.tool_calls:
                args = json.loads(call.function.arguments)
                result = None

                if call.function.name == "bing_search":
                    result = await browser.bing_search(args["query"])
                elif call.function.name == "open_result":
                    result = await browser.open_result(args["id"])
                elif call.function.name == "click":
                    result = await browser.click(args["url"])
                elif call.function.name == "back":  
                    result = browser.back()
                elif call.function.name == "scroll":
                    result = browser.scroll(args["amt"])
                elif call.function.name == "quote":
                    result = browser.quote(args["start"], args["end"])

                if isinstance(result, list):
                    messages.append({"role": "user", "content": truncate("\n".join(result), 4096)})
                else:
                    messages.append({"role": "user", "content": truncate(result, 4096)})

        else:
            print(f"ASSISTANT: {response_message.content}")
            user_input = input("USER: ")
            messages.append({"role": "user", "content": user_input})

async def main():
    browser = WebBrowser()
    user_question = """Find an authoritative source to answer: who is the original author of this quote:
    There is not any present moment that is unconnected with some future one.
    The life of every man is a continued chain of incidents, each link of which hangs upon the former. 
    The transition from cause to effect, from event to event, is often carried on by secret steps, which our foresight cannot divine, and our sagacity is unable to trace. 
    Evil may at some future period bring forth good; and good may bring forth evil, both equally unexpected. 
    """
    await web_search(user_question, browser)
    
asyncio.run(main())