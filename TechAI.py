from langchain_core.prompts import  ChatPromptsTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama
import streamlit as st

st.title("TechAI ChatBot")
input_txt=st.txt_input("Ask me anything!!!")

prompt=ChatPromptTemplate.from_messages(
    [("system","You are a helpful AI assistant. Your name is Ruhahuza."),
     ("user","user query:{query}")    
    ]) 
llm=ollama(model="llama2")
output_parser=StrOutputParser()
chain=prompt|llm|output_parser
if input_txt:
    st.write(chain.invoke({"query":input_txt}))
    