from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

model = ChatOpenAI(model='gpt-4',temperature=0, max_completion_tokens=10) #temperature is the creativeness of the response its basically lies from 0 to 2 .
result = model.invoke("What is the Capital of Nepal")
print(result)
print(result.content)
