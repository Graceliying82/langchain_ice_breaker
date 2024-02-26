from langchain.serpapi import SerpAPIWrapper

def get_profile_url(text:str) -> str:
    """Searches for Linkedin profile page"""

    search = SerpAPIWrapper()

    return search.run(f"{text}")

def search_by_serpapi(keyword:str) -> str:
    search = SerpAPIWrapper();
    search_result = search.run(keyword);
    return search_result