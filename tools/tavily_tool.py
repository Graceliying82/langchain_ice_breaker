from langchain_community.tools.tavily_search import TavilySearchResults



def search_by_tavily(keyword:str) -> str:
    search = TavilySearchResults();
    search_result = search.invoke(keyword);
    return search_result