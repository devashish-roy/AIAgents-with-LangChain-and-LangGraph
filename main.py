import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup

def ice_break_with(name: str):
    linkedin_url = lookup(name)
    

    summary_template = """
    given the likedin information {linkedin_data} about a person, i want to create:
    1. a short summary
    2. five interesting facts aboth them
    """

    summary_prompt_template = PromptTemplate(
        input_variables="linkedin_data", template=summary_template
        )

    llm = ChatOllama(model="llama3")

    chain = summary_prompt_template | llm | StrOutputParser()
    linkedin_data = scrape_linkedin_profile(linkedin_url)

    res = chain.invoke(input={"linkedin_data": linkedin_data})

    print(res)



if __name__ == '__main__':
    load_dotenv()
    ice_break_with(name="devashish singha roy master in applied ai LTU TCS stockholm linkedin")
    #print('hello LangChain!')
    #print(os.environ['OPENAI_API_KEY'])
    
    #summary_template = """
    #given the likedin information {information} about a person, i want to create:
    #1. a short summary
    #2. two interesting facts aboth them
    #""" 

    """
    summary_prompt_template = PromptTemplate(
        input_variables="information", template=summary_template
        )

    #llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")   # temp decided how creative the model can be.. 0 = not creative
    llm = ChatOllama(model="llama3")

    chain = summary_prompt_template | llm | StrOutputParser()
    linkedin_data = scrape_linkedin_profile("https://www.linkedin.com/in/devashish-singha-roy/")

    res = chain.invoke(input={"information": linkedin_data})

    print(res)
    """