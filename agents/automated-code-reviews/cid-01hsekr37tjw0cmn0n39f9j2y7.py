import asyncio
import json
import os
from dataclasses import dataclass
from typing import List, Dict, Tuple

import aiohttp
import openai
from dotenv import load_dotenv
import tiktoken

load_dotenv()

enc = tiktoken.get_encoding("cl100k_base")

SYSTEM_PROMPT = """
You are an AI assistant with access to a web browser for searching the internet to find information to answer questions. 
You have access to the following tools:

search(query: str) - Searches the internet for the given query and returns a list of Search Result objects. 
open_result(id: int) - Opens the search result with the given ID and returns the webpage content.
scroll_to(start: int, end: int) - Scrolls the open webpage to show the portion between the given start and end indexes of the content. Returns the now visible content.
quote(start: int, end: int) - Returns the extracted quote from the open webpage between the given start and end indexes.

To use a tool, format your response like this:
Action: <tool_name>
Args: <json_formatted_args>

When you have found enough information to answer the original question, format your response like this:
Action: finish
Answer: <result>

Let's begin!
"""

@dataclass
class SearchResult:
    id: int
    url: str 
    title: str
    snippet: str

# Improvement: Use an async HTTP client for better performance
async def search(query: str, session: aiohttp.ClientSession) -> List[SearchResult]:
    """Searches Bing for the given query and returns a list of SearchResult objects."""
    # ToOptimize: Use a more robust search API or custom web scraper for better quality results
    url = "https://api.bing.microsoft.com/v7.0/search"
    params = {
        "q": query, 
        "textDecorations": True,
        "textFormat": "HTML",
        "answerCount": 5,
    }
    headers = {"Ocp-Apim-Subscription-Key": os.environ["BING_API_KEY"]}

    async with session.get(url, params=params, headers=headers) as resp:
        resp.raise_for_status()
        data = await resp.json()
        
    results = []
    for i, webpage in enumerate(data["webPages"]["value"]):
        result = SearchResult(
            id=i, 
            url=webpage["url"],
            title=webpage["name"],
            snippet=webpage["snippet"],
        )
        results.append(result)
        
    return results

# Improvement: Extract core webpage content and split into chunks in one step
def extract_page_chunks(html: str) -> List[str]:
    """Extracts the core webpage content and splits it into chunks of ~500 tokens."""
    # ToOptimize: Use a more robust HTML parsing library like beautifulsoup
    content_start = html.find("<main>")  
    content_end = html.rfind("</main>")
    core_content = html[content_start:content_end]
    core_content = core_content.replace("\n", " ")
    
    token_chunks = []
    start = 0
    while start < len(core_content):
        end = min(start + 500, len(core_content))
        chunk = core_content[start:end]
        if not chunk.endswith(" "):
            end = chunk.rfind(" ")
        token_chunks.append(chunk)
        start = end
        
    return token_chunks

# Improvement: Use an async HTTP client for better performance  
async def fetch_webpage(url: str, session: aiohttp.ClientSession) -> str:
    """Fetches the HTML content of the webpage at the given URL."""
    async with session.get(url) as resp:
        resp.raise_for_status()
        return await resp.text()

class WebBrowser:
    def __init__(self):
        self.search_results: List[SearchResult] = []
        self.page_chunks: List[str] = []
        self.chunk_index = 0
        # Improvement: Use an aiohttp.ClientSession for connection pooling
        self.session: aiohttp.ClientSession = aiohttp.ClientSession()
        
    # Improvement: Make an async method for non-blocking I/O
    async def search(self, query: str) -> List[SearchResult]:
        """Searches the web for the given query."""
        self.search_results = await search(query, self.session)
        return self.search_results
    
    async def open_result(self, id: int) -> List[str]:  
        """Opens the search result with the given ID."""
        result = self.search_results[id]
        html = await fetch_webpage(result.url, self.session)
        self.page_chunks = extract_page_chunks(html)
        self.chunk_index = 0
        return self.scroll_to(0, 0)
        
    def scroll_to(self, start: int, end: int) -> List[str]:
        """Scrolls to show the webpage chunks between start and end."""
        self.chunk_index = max(0, min(start, len(self.page_chunks)-1))
        end_index = min(end, len(self.page_chunks))
        return self.page_chunks[self.chunk_index:end_index]
    
    def quote(self, start: int, end: int) -> str:
        """Extracts the quote between the start and end indexes."""
        flat_chunks = " ".join(self.page_chunks)
        return flat_chunks[start:end]

    async def close(self):
        await self.session.close()

async def answer_query_with_web_search(query: str, 
                                       browser: WebBrowser,
                                       model: str,
                                       search_quality_reflection_prompt: str,
                                       search_quality_score_prompt: str) -> str:
    """Answers the given query by searching the web and extracting relevant information."""
    
    # Phase 1: Perform iterative searches to find relevant results
    search_quality_score = 0
    search_quality_threshold = 4 
    while search_quality_score < search_quality_threshold:
        results = await browser.search(query)
        print(f"Found {len(results)} search results for '{query}'.")
        
        # Reflect on quality of search results
        reflection_prompt = search_quality_reflection_prompt.format(
            query=query,
            search_results=json.dumps([r.__dict__ for r in results])
        )
        print("Reflecting on initial search quality...")
        messages = [
            {"role": "system", "content": "You are an AI search quality reflection agent. Reflect on the quality and relevance of the search results for answering the given query."},
            {"role": "user", "content": reflection_prompt}
        ]
        response: Dict = await openai_chat_completion(model=model, messages=messages)
        print(f"Search quality reflection:\n{response['content']}\n")

        # Score search quality
        score_prompt = search_quality_score_prompt.format(
            query=query,
            search_quality_reflection=response["content"]
        )

        messages = [
            {"role": "system", "content": "You are an AI search quality scoring agent. Score the search quality reflection on a scale of 1-5, where 1 indicates the search results are not at all relevant or sufficient to answer the query, and 5 indicates the results are highly relevant and sufficient."},
            {"role": "user", "content": score_prompt}
        ]
        response = await openai_chat_completion(model=model, messages=messages)
        search_quality_score = int(response["content"])
        print(f"Search quality score: {search_quality_score}")
        
   # Phase 2: Open promising search results and extract relevant quotes
    relevant_quotes = []
    for result in results:
        content_chunks = await browser.open_result(result.id)
        print(f"Opened result {result.id}: '{result.title}'. Content chunks: {len(content_chunks)}")
        
        # Check each chunk for relevance to query
        for i, chunk in enumerate(content_chunks):
            relevance_prompt = f"""
            Query: {query}
            
            Webpage Content:
            ...
            {chunk}
            ...
            
            On a scale of 1-5, where 1 is not relevant at all and 5 is highly relevant, how relevant is this content for answering the query? Only respond with a single integer.
            """
            messages = [
                {"role": "system", "content": "You are an AI relevance scoring agent. Score the relevance of webpage content chunks for answering a given query."},
                {"role": "user", "content": relevance_prompt}
            ]
            response = await openai_chat_completion(model=model, messages=messages)
            relevance_score = int(response["content"])
            print(f"Chunk {i} relevance score: {relevance_score}")
            
            if relevance_score >= 4:
                quote = browser.quote(chunk.find(query), len(chunk))
                relevant_quotes.append(quote)
                
    # Phase 3: Synthesize relevant quotes into final answer
    answer_prompt = f"""
    Query: {query}
    
    Relevant Quotes:
    {relevant_quotes}
    
    Using only the relevant quotes, provide a concise answer to the original query. Do not add any information not contained in the quotes. 
    """ 
    messages = [
        {"role": "system", "content": "You are an AI question answering agent. Synthesize relevant quotes extracted from web search to concisely answer the given question."},
        {"role": "user", "content": answer_prompt}
    ]
    response = await openai_chat_completion(model=model, messages=messages)
    return response["content"]

async def openai_chat_completion(model: str, messages: List[Dict]) -> Dict:
    """Queries the OpenAI chat completion API."""
    response = await openai.ChatCompletion.acreate(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message  # type: ignore

async def main():
    load_dotenv()
    
    # Sample usage
    browser = WebBrowser()
    query = "What are the 3 main pyramids of Giza?"
    
    search_quality_reflection_prompt = """
    Query: {query}

    Search Results:
    {search_results}
    
    How relevant and sufficient are these search results for answering the query? What key information is missing? What additional searches would help find better information?
    """
    
    search_quality_score_prompt = """
    Query: {query}

    Search Quality Reflection:
    {search_quality_reflection}
    
    On a scale of 1-5, where 1 is not relevant or sufficient and 5 is very relevant and sufficient, how would you score the search results for answering the original query based on the reflection above? Respond with a single integer score.
    """
    
    result = await answer_query_with_web_search(
        query, 
        browser, 
        model="gpt-3.5-turbo",
        search_quality_reflection_prompt=search_quality_reflection_prompt,
        search_quality_score_prompt=search_quality_score_prompt
    )
    print(f"Final Result: {result}")
    
    await browser.close()

if __name__ == "__main__":
    asyncio.run(main())