from langchain_openai import ChatOpenAI # we need this for whatever chat API we are using
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#basically, you need a chat api, a prompter and a output parser
import streamlit as st
import os 
from dotenv import load_dotenv

load_dotenv(r'Langchain_apps\.env')

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY2")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

"""
systemp prompt: Personally, I use the system part to give instruction/persona/specifications
                I want it to keep on the long run. Might be mistaken,
                but I believe the system part is kept in “active memory” the whole length of your discussion.
user prompt: user interactions
"""
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are genius math teacher"),
        ("user","Question:{question}")
    ]
)

#streamlit framework
st.title("Langchain demo")
input_text = st.text_input("Ask you math question")

# intializing the api
chatgpt_llm = ChatOpenAI(model = 'gpt-3.5-turbo')

#parswr
output_parser = StrOutputParser()

chain = prompt|chatgpt_llm|output_parser
# chaining all of the three componenets

if input_text:
    st.write(chain.invoke({'question': input_text}))






