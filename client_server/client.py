import requests
import streamlit as st

def get_openai_response(input_text):
    response=requests.post("http://localhost:8000/chatgpt/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']['content']

def get_ollama_response(input_text):
    response=requests.post(
    "http://localhost:8000/starcoder/invoke",
    json={'input':{'topic':input_text}})

    return response.json()['output']

    ## streamlit framework

st.title('Langchain Demo with chatgpt and startcoder')
input_text=st.text_input("Write an essay on")
input_text1=st.text_input("Write a poem on")

if input_text:
    st.write(get_openai_response(input_text))

if input_text1:
    st.write("THIS IS STAR CODER RESPONSE")
    st.write(get_ollama_response(input_text1))