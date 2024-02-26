from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.tools import Tool
from agents.linkedin_lookup_agent import  lookup as linkedin_lookup_agent

from third_parties.linkedin import scrape_linkedin_profile
from tools.tavily_tool import search_by_tavily
from tools.serpapi_tool import search_by_serpapi
import time
def compare_search(search_keyword):
    start_time_tavily = time.time()
    result_tavily = search_by_tavily(search_keyword)
    end_time_tavily = time.time()
    runtime_tavily = end_time_tavily - start_time_tavily

    start_time_serpapi = time.time()
    result_serpapi = search_by_serpapi(search_keyword)
    end_time_serpapi = time.time()
    runtime_serpapi = end_time_serpapi - start_time_serpapi

    print(f"Context from search_by_tavily: \n {result_tavily}")
    print(f"Context from search_by_serpapi: \n {result_serpapi}")

    # Compare runtimes
    print("Runtime for search_by_tavily:", runtime_tavily)
    print("Runtime for search_by_serpapi:", runtime_serpapi)


def ice_break(name):
    # summary_template = """
    # given the LinkedIn information {information} about a person I want you to create:
    # 1 A short summary
    # 2 two interesting facts about them
    # """
    #
    # summary_prompt_template = PromptTemplate(
    #     input_variables=["information"], template=summary_template
    # )
    #
    # llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    #
    # chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    #
    # linkedin_profile_url = linkedin_lookup_agent("elon musk")
    #
    # print(f"linkedin_profile_url is {linkedin_profile_url}")

    # linkedin_data = scrape_linkedin_profile()
    #
    # print(chain.run(information=linkedin_data))
    search_keyword = (name)
    search_results = search_by_tavily(search_keyword)
    return (search_results[0]['content'], search_results[0]['url'])
    # compare_search(search_keyword)

if __name__ == "__main__":
    load_dotenv()

    print("Hello Langchain")
    ice_break("Elon Musk")



