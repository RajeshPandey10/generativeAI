from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
load_dotenv()


def load_model():
    return ChatOpenAI(
        model='gpt-3.5-turbo',
        temperature=0.7, 
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1"
    )

model = load_model()

chat_history = [
    SystemMessage(content='You are a helpful assistant RP'),
]


while True:
    user_input = input('You:')
    chat_history.append(HumanMessage(content=user_input))
    if user_input =='exit':
        break
    result =model.invoke(chat_history)#sending the user_input to the prompt
    chat_history.append(AIMessage(content=result.content))
    print("AI:",result.content)
print(chat_history)