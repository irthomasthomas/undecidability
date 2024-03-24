import asyncio
import json
from typing import List, Dict
from urllib.parse import urljoin

import aiohttp
import openai
import tiktoken
from tenacity import retry, wait_exponential, stop_after_attempt

from config import settings
from web_search_utils import strip_tags, create_chunks, format_webpage

enc = tiktoken.get_encoding("cl100k_base")


class SearchResult:
    def __init__(self, data: Dict):
        self.id: int = int(data["id"].split(".")[-1]) 
        self.url: str = data["url"]
        self.name: str = data["name"]
        self.snippet: str = data["snippet"]


class WebBrowser:
    def __init__(self, search_key: str, custom_search_key: str):
        self.search_key = search_key
        self.custom_search_key = custom_search_key
        self.search_results: List[SearchResult] = []
        self.current_page: List[str] = []
        self.history: List[List[str]] = []

    async def search(self, query: str) -> List[SearchResult]:
        search_results = await run_custom_bing_search(query, self.custom_search_key)
        relevant_results = [SearchResult(result) for result in search_results]
        self.search_results = relevant_results
        return relevant_results

    def scroll(self, amt: int) -> List[str]:
        start = max(0, min(len(self.current_page) - 1, amt - 1))
        end = min(len(self.current_page), start + settings.chunk_size)
        return self.current_page[start:end]
    
    def open(self, result_id: int) -> List[str]:
        url = next((result.url for result in self.search_results if result.id == result_id), None)
        if url:
            return self.navigate(url)
        else:
            return []
        
    def navigate(self, url: str) -> List[str]:  
        if not is_absolute_url(url):
            url = urljoin(self.current_page[0], url)
        
        self.history.append(self.current_page)
        self.current_page = fetch_page_chunks(url)
        return self.current_page
    
    def back(self) -> List[str]:
        if self.history:
            self.current_page = self.history.pop()
        return self.current_page
    
    def quote(self, start: int, end: int) -> str:
        return "\n".join(self.current_page[start-1:end])


def is_absolute_url(url: str) -> bool:
    return url.startswith("http://") or url.startswith("https://")


@retry(wait=wait_exponential(multiplier=1, min=2, max=10), stop=stop_after_attempt(3)) 
async def fetch_webpage_content(url: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status != 200:
                resp.raise_for_status()
            
            content = await resp.text()
            stripped = strip_tags(content, minify=True, keep_tags=["p", "a"])
            formatted = format_webpage(stripped)
            return formatted


def fetch_page_chunks(url: str) -> List[str]:
    content = asyncio.run(fetch_webpage_content(url))
    return list(create_chunks(content, settings.chunk_size, enc))

@retry(wait=wait_exponential(multiplier=1, min=2, max=10), stop=stop_after_attempt(3))
async def run_custom_bing_search(query: str, custom_search_key: str) -> List[Dict]:
    encoded_query = query.replace(" ", "+")
    url = f"https://api.bing.microsoft.com/v7.0/custom/search?q={encoded_query}&customconfig={settings.bing_custom_config}"
    headers = {"Ocp-Apim-Subscription-Key": custom_search_key}
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            if resp.status != 200:
                resp.raise_for_status()
            
            data = await resp.json()
            return data.get("webPages", {}).get("value", [])


async def query_chat_model(query: str, messages: List[Dict], tools: List[Dict]) -> Dict:
    kwargs = {
        "model": settings.chat_model,
        "temperature": settings.chat_temperature,
        "messages": messages,
        "tools": tools
    }
    if settings.use_openrouter:
        kwargs["base_url"] = "https://openrouter.ai/api/v1"
        kwargs["api_key"] = settings.openrouter_key
    else:  
        kwargs["api_key"] = settings.openai_key

    response = await openai.ChatCompletion.acreate(**kwargs)
    return response["choices"][0]["message"] 


def estimate_tokens(messages: List[Dict]) -> int:
    if messages:
        return len(enc.encode(messages[-1]["content"]))
    else:
        return 0



async def manage_browser_task(query: str, browser: WebBrowser):
    tools = build_tools(browser)
    messages = [{"role": "system", "content": settings.browsing_prompt}]
    messages.append({"role": "user", "content": query})

    while True:
        tokens = estimate_tokens(messages)
        model = settings.fast_llm if tokens < settings.fast_token_limit else settings.smart_llm

        assistant_message = await query_chat_model(query, messages, tools)
        messages.append(assistant_message)

        # Check if any browser actions were requested and execute them
        actions_completed = await execute_browser_actions(assistant_message, browser)

        # Check if search completed successfully  
        if "SEARCH_QUALITY_REFLECTION" in assistant_message["content"]:
            break
        
        # Handle case when assistant gets stuck
        if not actions_completed: 
            messages.append(
                {"role": "user", "content": "The search is not progressing. Please try a different approach."}
            )

    return assistant_message["content"]


def build_tools(browser: WebBrowser) -> List[Dict]:
    return [
        {
            "name": "search",
            "description": "Search the web for relevant information",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The search query"}
                },
                "required": ["query"],
            },
        },
        {
            "name": "open",
            "description": "Open a search result by its ID",
            "parameters": {
                "type": "object", 
                "properties": {
                    "result_id": {"type": "integer", "description": "The ID of the search result to open"}
                },
                "required": ["result_id"],
            },
        },
        {
            "name": "navigate",
            "description": "Navigate to a URL",
            "parameters": {
                "type": "object",
                "properties": {
                    "url": {"type": "string", "description": "The URL to navigate to"}
                },
                "required": ["url"],
            },
        },
        {
            "name": "scroll",
            "description": "Scroll the current page",
            "parameters": {
                "type": "object",
                "properties": {
                    "direction": {"type": "integer", "description": "The number of chunks to scroll, negative for up"},
                },
                "required": ["direction"],
            },
        },
        {
            "name": "quote",
            "description": "Quote content from the current page",
            "parameters": {
                "type": "object",
                "properties": {
                    "start": {"type": "integer", "description": "The line number to start quoting from"},
                    "end": {"type": "integer", "description": "The line number to end quoting at"},
                },
                "required": ["start", "end"],
            },
        },
    ]


async def execute_browser_actions(message: Dict, browser: WebBrowser) -> bool:
    if not message.get("tools"):
        return False

    for tool in message["tools"]:
        action = tool["name"]
        args = json.loads(tool["arguments"])

        if action == "search":
            results = await browser.search(args["query"])  
            browser.search_results = results

        elif action == "open":
            page_chunks = browser.open(args["result_id"])

        elif action == "navigate":
            page_chunks = browser.navigate(args["url"])

        elif action == "scroll":
            direction = args["direction"]
            page_chunks = browser.scroll(direction)

        elif action == "quote":
            quote = browser.quote(args["start"], args["end"])    

    return True


async def web_search(query: str) -> str:
    browser = WebBrowser(settings.bing_search_key, settings.bing_custom_search_key) 
    result = await manage_browser_task(query, browser)
    return result


query = "example question needing a web search to answer"
answer = asyncio.run(web_search(query))
print(answer)