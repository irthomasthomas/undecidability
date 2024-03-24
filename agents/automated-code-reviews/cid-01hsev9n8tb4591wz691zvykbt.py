import asyncio
import json
import logging
import openai 
import tiktoken
from dataclasses import dataclass
from typing import List

log = logging.getLogger(__name__)

@dataclass
class SearchQuery:
    text: str
    
@dataclass 
class SearchResult:
    id: str
    url: str
    title: str
    snippet: str
        
@dataclass
class WebPage:
    url: str
    title: str 
    headings: List[str]
    content: str

@dataclass
class SearchSession:
    original_query: str
    search_quality_reflection: str
    search_quality_score: int

class OpenAIClient:
    
    def __init__(self, api_key: str, model: str):
        openai.api_key = api_key
        self.model = model
        
    async def classify_search_quality(self, query: str, results: List[SearchResult]) -> SearchSession:
        prompt = f"""
        Given the following search query and search results, analyze the quality and comprehensiveness 
        of the search results for addressing the query. Provide a search quality score between 1 and 5, 
        as well as a written reflection explaining the score and what key information may be missing 
        from the results to fully address the query.
        
        Query: {query}
        
        Search Results JSON: {json.dumps([r.__dict__ for r in results], indent=2)}
        
        Provide your response in the following JSON format:
        {{
            "search_quality_reflection": "...",
            "search_quality_score": 1-5 
        }}
        """
        response = await openai.Completion.acreate(
            engine=self.model,
            prompt=prompt,
            max_tokens=500,
            temperature=0.7,
        )
        result = json.loads(response.choices[0].text)
        
        return SearchSession(
            original_query=query, 
            search_quality_reflection=result['search_quality_reflection'],
            search_quality_score=result['search_quality_score'],
        )
        
    async def extract_page_summary(self, page: WebPage) -> str:
        prompt = f"""
        Given the following web page, extract a concise summary of the key points most relevant to 
        the original search query. Omit any irrelevant details.
        
        Web Page JSON:
        {{
            "url": "{page.url}",
            "title": "{page.title}",
            "headings": {json.dumps(page.headings)},
            "content": "{page.content}"
        }}
        """
        response = await openai.Completion.acreate(
            engine=self.model,
            prompt=prompt,
            max_tokens=500,
            temperature=0.7,
        )
        return response.choices[0].text.strip()

    async def synthesize_final_answer(self, query: str, page_summaries: List[str]) -> str:
        prompt = f"""
        Given the original search query and the extracted summaries of the most relevant web pages 
        found, synthesize a comprehensive final answer to the original query. Aim to address all 
        aspects of the query, cite sources as "[Source 1]", "[Source 2]" etc, and provide an 
        in-depth answer while still being concise.
        
        Query: {query}
        
        Page summaries:
        {chr(10).join([f'[Source {i+1}]: {summary}' for i, summary in enumerate(page_summaries)])}
        """
        response = await openai.Completion.acreate(
            engine=self.model,
            prompt=prompt,
            max_tokens=800,
            temperature=0.8,
        )
        return response.choices[0].text.strip()

class BingSearchClient:
    
    def __init__(self, subscription_key: str):
        self.subscription_key = subscription_key
        self.endpoint = "https://api.bing.microsoft.com/v7.0/search"
    
    async def search(self, query: str, top: int = 30) -> List[SearchResult]:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                self.endpoint, 
                params={
                    "q": query,
                    "count": top,
                    "responseFilter": "webpages", 
                },
                headers={"Ocp-Apim-Subscription-Key": self.subscription_key},
            ) as resp:
                resp.raise_for_status()
                result = await resp.json()
                
        return [SearchResult(
            id=v['id'],
            url=v['url'],
            title=v['name'], 
            snippet=v['snippet'],
        ) for v in result['webPages']['value']]

@dataclass
class PageChunk:
    text: str
    token_count: int

class PageContentExtractor:
    
    def __init__(self):
        self.encoding = tiktoken.get_encoding("cl100k_base")
        
    def extract_clean_page_content(self, url: str) -> str:
        # Use shot-scraper library to fetch page content minus boilerplate 
        # and html tags, javascript etc.
        result = RUNNER.invoke(cli.cli, ["html", url])  
        content = strip_tags(result.output, keep_tags=["p", "a"])
        content = content.replace("\n\n\n", "\n").strip()
        return content
    
    def chunk_page_content(self, text: str, target_token_size: int = 2048) -> List[PageChunk]:
        tokens = self.encoding.encode(text)
        chunks = []
        start = 0
        
        while start < len(tokens):
            end = min(start + target_token_size, len(tokens))
            while end < len(tokens) and tokens[end] != ord(chr(46)): # Ensure chunks end on sentence boundary
                end -= 1
            chunk_text = self.encoding.decode(tokens[start:end+1]) 
            chunks.append(PageChunk(
                text=chunk_text,
                token_count=end - start + 1,
            ))
            start = end + 1
            
        return chunks
            
class SearchPipeline:
    
    def __init__(
        self, 
        bing_search_client: BingSearchClient,
        openai_client: OpenAIClient,
        content_extractor: PageContentExtractor,
    ):
        self.bing_search_client = bing_search_client
        self.openai_client = openai_client
        self.content_extractor = content_extractor
        
    async def run(self, query: str) -> str:
        search_quality_score = 0
        search_quality_reflection = None
        page_summaries = []

        while search_quality_score < 4:
            log.info(f"Searching Bing for: {query}")
            search_results = await self.bing_search_client.search(query)
            
            session = await self.openai_client.classify_search_quality(query, search_results)
            search_quality_score = session.search_quality_score
            search_quality_reflection = session.search_quality_reflection
            
            log.info(f"Search quality score: {search_quality_score}")
            log.info(f"Search quality reflection: {search_quality_reflection}")
            
            if search_quality_score < 4:
                query = search_quality_reflection
                continue
            
            pages = await asyncio.gather(*[
                self.fetch_and_extract_page(url) 
                for url in [r.url for r in search_results]    
            ])
            page_summaries = await asyncio.gather(*[
                self.openai_client.extract_page_summary(page)
                for page in pages
            ])
            
        return await self.openai_client.synthesize_final_answer(session.original_query, page_summaries)
            
    async def fetch_and_extract_page(self, url: str) -> WebPage:
        log.info(f"Fetching page content from {url}")
        try:
            content = self.content_extractor.extract_clean_page_content(url)
            chunks = self.content_extractor.chunk_page_content(content)
            return WebPage(
                url=url,
                title = extract_title(content),
                headings=extract_headings(content),
                content=chunks[0].text,
            )
        except Exception as e:
            log.warning(f"Failed to fetch content for {url}. Error: {str(e)}")
            return WebPage(url=url, title=None, headings=[], content=None)


async def main():
    bing_search_client = BingSearchClient(
        subscription_key=os.environ["BING_SUBSCRIPTION_KEY"]    
    )
    openai_client = OpenAIClient(
        api_key=os.environ["OPENAI_API_KEY"],
        model="gpt-4",
    )
    content_extractor = PageContentExtractor()
    
    pipeline = SearchPipeline(
        bing_search_client=bing_search_client, 
        openai_client=openai_client,
        content_extractor=content_extractor,
    )
    
    query = "What are the three main pyramids of Giza?"
    result = await pipeline.run(query)
    print(result)

if __name__ == "__main__":        
    asyncio.run(main())