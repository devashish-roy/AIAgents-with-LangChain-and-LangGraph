import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.tools import Tool
from langchain.agents import (create_react_agent, AgentExecutor)
from agents.tools.tools import get_profile_url_tavily
from langchain import hub

load_dotenv()

def lookup(name:str):
    llm = ChatOllama(model="llama3")

    template = """ given the fullname {name_of_the_person} i want to get it me a link to their LinkedIn profile page.
                    your answer should only contain the URL. """
    
    
    prompt_template = PromptTemplate(
        template=template,
        input_variables=["name_of_the_person"]
    )

    tools_for_agent = [
        Tool(
            name = "Crawl google to find LinkedIn profile page",
            func= get_profile_url_tavily,
            description= "Useful when you need to get the LinkedIn page URL"
        )
    ]


    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(llm=llm, tools=tools_for_agent, prompt=react_prompt)

    agent_executor = AgentExecutor(agent=agent, tools=tools_for_agent, verbose=True, handle_parsing_errors=True)

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_the_person=name)}
    )
    
    linkedin_profile_url = result["output"]
   
    return linkedin_profile_url



if __name__ == "__main__":
    url = lookup("mandve singha roy animation and vfx artist futuregames LinkedIn")
    print(url)