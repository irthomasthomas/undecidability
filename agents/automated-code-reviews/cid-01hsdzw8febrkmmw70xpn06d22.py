import asyncio
import json
import os
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass
from dotenv import load_dotenv
from urllib.parse import urljoin
import tiktoken

import openai

load_dotenv()

enc = tiktoken.get_encoding("cl100k_base")


@dataclass
class SearchResult:
    id: int
    url: str
    name: str
    snippet: str
    
    def __init__(self, data):
        self.id = int(data["id"].split(".")[-1]) 
        self.url = data["url"]
        self.name = data["name"] 
        self.snippet = data["snippet"]
        

class WebBrowser:
    def __init__(self):
        self.search_results = []
        self.current_page = [] 
        self.current_page_url = None
        self.history = []
        self.visible_chunk_count = 1
        self.page_scroll_position = 0

    def search(self, query, recency_days=30):
        search_results = run_bing_search(query, recency_days)
        if search_results:
            self.search_results = [SearchResult(result) for result in search_results["webPages"]["value"]]
        return self.search_results

    def scroll(self, amt):
        self.page_scroll_position = max(0, min(self.page_scroll_position + amt, len(self.current_page) - 1))
        start = self.page_scroll_position
        end = min(start + self.visible_chunk_count, len(self.current_page))
        return self.current_page[start:end]

    def open_result(self, id):
        result = next((result for result in self.search_results if result.id == id), None)
        if result:
            return self.navigate(result.url)
        return []

    def navigate(self, url):
        if not url.startswith("http"):
            url = urljoin(self.current_page_url, url)

        content = fetch_webpage_content(url)
        chunks = list(chunk_text(content, 2048, enc))
        
        self.history.append((self.current_page_url, self.current_page))
        self.current_page = chunks
        self.current_page_url = url
        self.page_scroll_position = 0
        
        return chunks

    def back(self):
        if self.history:
            self.current_page_url, self.current_page = self.history.pop()
            self.page_scroll_position = 0
        return self.current_page

    def quote(self, start, end):
        return "\n".join(self.current_page[start-1:end])


def chunk_text(text, n, tokenizer):
    tokens = tokenizer.encode(text)
    chunks = []
    for i in range(0, len(tokens), n):
        chunk = tokenizer.decode(tokens[i:i+n])
        if chunk.endswith((".", "!", "?", "\n", ". ", "! ", "? ")):
            chunks.append(chunk)
        else:
            remainder = tokenizer.decode(tokens[i+n:])
            last_sentence_end = max(
                remainder.find("."),
                remainder.find("!"),
                remainder.find("?"),
                remainder.find("\n")
            )
            if last_sentence_end != -1:
                sliced_remainder = remainder[:last_sentence_end+1]
                chunks.append(chunk + sliced_remainder)
                chunks.extend(chunk_text(remainder[last_sentence_end+1:], n, tokenizer))
            else:
                chunks.append(chunk)
                chunks.extend(chunk_text(remainder, n, tokenizer))
            break
    return chunks


def run_bing_search(query, recency_days=30):
    url = "https://api.bing.microsoft.com/v7.0/search"
    headers = {"Ocp-Apim-Subscription-Key": os.environ["BING_API_KEY"]}
    params = {
        "q": query,
        "count": 10,
        "offset": 0,
        "freshness": f"Day_{recency_days}",
        "responseFilter": "webpages",
        "textDecorations": True,
        "textFormat": "HTML"
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


def fetch_webpage_content(url):
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text


def openai_request(prompt, model, max_tokens=None):
    params = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    if max_tokens:
        params["max_tokens"] = max_tokens
    
    response = openai.chat.completions.create(**params)
    
    return response.choices[0].message.content.strip()


def extract_relevant_results(query, search_results, model):
    prompt = f"""
    Search Quality Reflection:
    Search query: {query}
    Search results:
    {json.dumps(search_results, indent=2)}
    
    Given the search query and search results above, respond with a JSON array containing the ids of the search results that are most relevant to answering the original query. Choose up to 5 results. Format: ["id1", "id2", ...]
    """
    
    relevant_ids = json.loads(openai_request(prompt, model, max_tokens=100))
    
    return [result for result in search_results if result["id"] in relevant_ids]

    
def parallel_search(queries, model):
    search_results = []
    
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(run_bing_search, query) for query in queries]
        for future in as_completed(futures):
            search_results.extend(future.result()["webPages"]["value"])
    
    relevant_results = []
    
    with ThreadPoolExecutor() as executor:        
        futures = [executor.submit(extract_relevant_results, query, results, model) 
                   for query, results in zip(queries, [search_results]*len(queries))]
        for future in as_completed(futures):
            relevant_results.extend(future.result()) 
            
    return relevant_results


def generate_bing_queries(question, model):
    prompt = f"""
    Generate search queries:
    
    Original question: {question}
    
    Generate a JSON array of 3-5 search queries to run on Bing that would help find information to answer the original question. Use a variety of keywords and phrasings. Format:
    ["query 1", "query 2", ...]
    """
    
    queries = json.loads(openai_request(prompt, model, max_tokens=200))
    
    return queries + [question]


def web_search(question, model="gpt-3.5-turbo"):
    browser = WebBrowser()
    
    queries = generate_bing_queries(question, model)
    print(f"Generated queries: {queries}")
    
    search_quality_reflection = "The original search queries did not yield sufficiently relevant or comprehensive results to answer the question. Additional targeted searches are needed."
    
    while search_quality_reflection.lower() != "the search results so far provide sufficient information to comprehensively answer the original question.":
        relevant_results = parallel_search(queries, model) 
        print(f"Found {len(relevant_results)} relevant results.")
        
        result_snippets = " ".join([r["snippet"] for r in relevant_results])
        
        prompt = f"""
        Search Quality Reflection:
        
        Original question: {question}
        
        Search queries: {queries}
        
        Relevant search result snippets:
        {result_snippets}
        
        Based on the original question, search queries, and relevant search result snippets, analyze if the search results so far provide sufficient information to comprehensively answer the original question. 
        
        If so, respond with: "The search results so far provide sufficient information to comprehensively answer the original question."
        
        If not, reflect on what key information is still missing to answer the original question, and respond with a critique of the search quality so far highlighting the specific additional information that needs to be searched for.
        """
        
        search_quality_reflection = openai_request(prompt, model)
        print(f"Search quality reflection: {search_quality_reflection}")
        
        if search_quality_reflection.lower() != "the search results so far provide sufficient information to comprehensively answer the original question.":
            queries = generate_bing_queries(search_quality_reflection, model)
    
    print(f"Searches complete. Relevant results: {len(relevant_results)}")
    
    for result in relevant_results:
        browser.search_results.append(SearchResult(result))
        
        content = fetch_webpage_content(result["url"])
        chunks = list(chunk_text(content, 2048, enc))
        
        quote_scores = [
            {
                "url": result["url"],
                "content": chunk, 
                "score": openai_request(
                    f"On a scale of 1-5, rate how relevant this quote is to answering the question '{question}'\nQuote: {chunk}", 
                    model, 
                    max_tokens=10
                )
            }
            for chunk in chunks
        ]
        
        top_quotes = sorted(quote_scores, key=lambda x: int(x["score"]), reverse=True)[:3]
        
        browser.history.append((result["url"], "\n".join([q["content"] for q in top_quotes])))
    
    assistant_prompt = f"""
    Use the search result quotes provided to write a comprehensive answer to the question:
    
    {question}
    
    Relevant quotes from web search:
    
    {browser.history}
    """
    
    assistant_response = openai_request(assistant_prompt, model)
    
    return assistant_response

async def main():
    browser = WebBrowser()
    user_question = """Using authoritative web sources to answer: who is the original author of this quote:
    There is not any present moment that is unconnected with some future one.
    The life of every man is a continued chain of incidents, each link of which hangs upon the former. 
    The transition from cause to effect, from event to event, is often carried on by secret steps, which our foresight cannot divine, and our sagacity is unable to trace. 
    Evil may at some future period bring forth good; and good may bring forth evil, both equally unexpected. 
    """
    await web_search(user_question, browser)
    
asyncio.run(main())