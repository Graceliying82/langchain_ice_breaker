from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

from langchain.agents import initialize_agent, Tool, AgentType


def lookup(name: str) -> str:

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    template = """given the full name {name_of_person} I want you to get it me a link to their Linkedin profile page.
    Your answer should contain only a URL"""

    tools_for_agent = [
        Tool(
            name="Crawl Google 4 linkedin profile page",
            func="?",
            description="useful for when you need to get the Linkedin page ",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
    )

    return "Linkedin Profile URL"
