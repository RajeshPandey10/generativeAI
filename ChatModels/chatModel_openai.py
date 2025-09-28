from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

# Configure for OpenRouter
model = ChatOpenAI(
    model='gpt-4',
    temperature=0, 
    max_completion_tokens=10,
    openai_api_key=os.getenv("OPENROUTER_API_KEY"),
    openai_api_base="https://openrouter.ai/api/v1"
)
result = model.invoke("What is the Capital of Nepal")
print(result)
print(result.content)
