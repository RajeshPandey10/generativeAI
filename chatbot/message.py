from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
def load_model():
    return ChatOpenAI(
        model='gpt-3.5-turbo',
        temperature=0.7, 
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1"
    )

model = load_model()

messages = [
    SystemMessage(content='You are a helpful assistant RP'),
    HumanMessage(content='Tell me about LangChain')
]
result=model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)