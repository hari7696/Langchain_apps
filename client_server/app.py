from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatOpenAI
from langchain_community.llms import Ollama
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv('../venv/.env')

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY2')

app = FastAPI(

    title = "first genAI api",
    version = "1.0",
    description="API server serving both ollama and chatgpt"

)

chat_gpt = ChatOpenAI()
start_coder_model = Ollama(model= "starcoder:1b")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")

add_routes(app, prompt1|chat_gpt, path = "/chatgpt")

add_routes(app, prompt2|start_coder_model, path = "/starcoder" )

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)