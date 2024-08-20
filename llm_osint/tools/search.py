from langchain_community.tools import DuckDuckGoSearchRun, DuckDuckGoSearchResults
from langchain.agents import Tool

from llm_osint import cache_utils


class CachedDuckDuckGoSearchRun(DuckDuckGoSearchRun):
    @cache_utils.cache_func
    def run(self, query: str) -> str:
        return super().run(query)


def get_search_tool(**kwargs) -> Tool:
    search = CachedDuckDuckGoSearchRun(**kwargs)
    return Tool(
        name="Search Term",
        func=search.run,
        description="Useful for finding information on general topics, names, usernames, places, etc. The input should be a search term.",
    )


def get_detailed_search_tool(**kwargs) -> Tool:
    search = DuckDuckGoSearchResults(**kwargs)
    return Tool(
        name="Detailed Search",
        func=search.run,
        description="Useful for getting detailed search results, including links and sources. The input should be a search term.",
    )


def get_news_search_tool(**kwargs) -> Tool:
    search = DuckDuckGoSearchResults(backend="news", **kwargs)
    return Tool(
        name="News Search",
        func=search.run,
        description="Useful for searching recent news articles. The input should be a search term.",
    )
