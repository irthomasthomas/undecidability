import asyncio
import json
import os
from typing import List, Dict, Optional
from urllib.parse import urljoin, quote_plus

import aiohttp
import openai
import tiktoken
from dotenv import load_dotenv
from pydantic import BaseModel


class SearchResult(BaseModel):
    id: int
    url: str
    name: str
    snippet: str


class WebPage(BaseModel):
    url: str
    content: List[str] = []


class WebBrowser:
    def __init__(self):
        self.search_results: List[SearchResult] = []
        self.current_page: WebPage = WebPage(url="")
        self.history: List[WebPage] = []

    async def search(self, query: str, *, recency_days: int = 30) -> List[SearchResult]:
        search_results = await run_bing_search(query, recency_days)
        if search_results:
            self.search_results = await process_search_results(query, search_results)
        return self.search_results

    def scroll(self, amt: int) -> List[str]:
        start_index = max(0, amt - 1) 
        end_index = start_index + 1
        return self.current_page.content[start_index:end_index]

    async def open_result(self, id: int) -> List[str]:
        url = next((result.url for result in self.search_results if result.id == id), None)
        if url is None:
            return []
        return await self.navigate(url)
    
    async def navigate(self, url: str) -> List[str]:
        if not url.startswith("http://") and not url.startswith("https://"):
            url = urljoin(self.current_page.url, url)

        content = await fetch_webpage(url)
        self.history.append(self.current_page)
        self.current_page = WebPage(url=url, content=content)
        return content

    def back(self) -> List[str]:
        if self.history:
            self.current_page = self.history.pop()
            return self.current_page.content
        return []

    def quote(self, start: int, end: int) -> str:
        return "\n".join(self.current_page.content[start-1:end])


async def run_bing_search(query: str, recency_days: int = 30) -> Optional[Dict]:
    subscription_key = os.environ["BING_CUSTOM_KEY"] 
    custom_config_id = os.environ["BING_CUSTOM_CONFIG"]
    encoded_query = quote_plus(query)
    
    url = f"https://api.bing.microsoft.com/v7.0/custom/search?q={encoded_query}&customconfig={custom_config_id}&responseFilter=webpages"
    headers = {"Ocp-Apim-Subscription-Key": subscription_key}

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as resp:
            if resp.status == 200:
                data = await resp.json()
                return data
            else:
                print(f"Bing search failed with status {resp.status}")


async def fetch_webpage(url: str) -> List[str]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                html = await resp.text()
                # Parse and format HTML (omitted for brevity)
                return format_webpage(html)
            else:
                print(f"Failed to fetch {url} with status {resp.status}")
                return []


def format_webpage(html: str) -> List[str]:
    # Parse HTML and extract text content
    # Split into chunks and add line numbers
    # Return list of formatted chunks
    # (omitted for brevity)
    pass


async def process_search_results(query: str, results: Dict) -> List[SearchResult]:
    # Extract and format search result data
    search_data = [
        {"id": int(result["id"].split(".")[-1]), 
         "url": result["url"],
         "name": result["name"], 
         "snippet": result["snippet"]}
        for result in results["webPages"]["value"]
    ]
    
    # Generate prompt for selecting relevant results
    prompt = (
        f"Analyze these Bing search results: {json.dumps(search_data)}\n\n"
        f"Based on this user query: {query}\n\n"
        "Extract a list of relevant search result IDs that may help answer the user's query."
    )

    # Query OpenAI model to select relevant results
    relevant_ids = await analyze_with_openai(prompt)
    
    return [SearchResult(**data) for data in search_data if data["id"] in relevant_ids]


async def analyze_with_openai(prompt: str) -> List[int]:
    response = await openai.Completion.acreate(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
    )
    result_ids_str = response.choices[0].text.strip()
    return json.loads(result_ids_str)


async def generate_queries(question: str) -> List[str]:
    prompt = (
        f"Generate an array of about three search queries relevant to answering this question:\n{question}\n\n"
        "Use related keywords and advanced search operators to refine the results.\n"
        "Format the response as a JSON array of strings."
    )
    response = await openai.Completion.acreate(
        engine="text-davinci-003", 
        prompt=prompt,
        max_tokens=200,
        n=1, 
        stop=None,
        temperature=0.7,
    )
    queries = json.loads(response.choices[0].text.strip())
    queries.append(question)  # Add original question 
    return queries


async def search_quality_reflection(results: List[SearchResult], question: str) -> str:
    prompt = (
        f"Here are the search results so far:\n{json.dumps([r.dict() for r in results])}\n\n"
        f"How well do you think these results could answer the original question: {question}\n"
        "Provide a quality score from 1-5 and explain your reasoning."
    )
    response = await openai.Completion.acreate(
        engine="text-davinci-003",
        prompt=prompt, 
        max_tokens=200,
        n=1,
        stop=None, 
        temperature=0.7,
    )
    return response.choices[0].text.strip()


async def summarize_search(browser: WebBrowser, question: str) -> str:
    prompt = (
        f"Here are the key details from the search results and web pages explored so far:\n"
        f"Search results: {json.dumps([r.dict() for r in browser.search_results])}\n"
        f"Browsed urls: {[p.url for p in browser.history]}\n"
        f"Quoted content: {browser.current_page.content}\n\n"
        f"Based on this, provide a concise summary that answers the original question: {question}"
    )
    response = await openai.Completion.acreate(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500, 
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()


async def run_search(question: str):
    browser = WebBrowser()

    print(f"Generating search queries for: {question}")
    queries = await generate_queries(question)
    print(f"Queries: {queries}")

    quality_score = 0
    quality_reflection = None
    search_rounds = 0

    while quality_score < 4:
        search_rounds += 1
        if search_rounds > 3:
            print("Reached maximum search rounds, stopping search.")
            break
        
        print(f"Executing Bing searches, round {search_rounds}")
        search_tasks = [browser.search(query) for query in queries]
        await asyncio.gather(*search_tasks)

        if quality_reflection:
            print(f"Previous quality reflection: {quality_reflection}")    
        quality_reflection = await search_quality_reflection(browser.search_results, question)
        quality_score = int(quality_reflection[0])
        print(f"Search quality score: {quality_score}, Reflection: {quality_reflection}") 

        print("Opening top search results...")
        await asyncio.gather(*(browser.open_result(result.id) for result in browser.search_results[:3]))

        print("Selecting quotes...")
        # Select quotes (omitted for brevity)
    
    print(f"Searches complete after {search_rounds} rounds. Generating summary...")
    summary = await summarize_search(browser, question)

    print("Final summary:")
    print(summary)


async def main():
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")

    question = "What are the three branches of the US government?"
    await run_search(question)


if __name__ == "__main__":
    asyncio.run(main())