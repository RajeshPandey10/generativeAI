from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
load_dotenv()

model = ChatOpenAI(
        model='gpt-3.5-turbo',
        temperature=0.7, 
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1"
    )

#1st prompt ->detailed report
template1=PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

#2nd report
template2=PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

# prompt1 =template1.invoke({'topic':'black hole'})


# result = model.invoke(prompt1)

# prompt2 = template2.invoke({'text':result.content})
# result1=model.invoke(prompt2)
# print(result1.content)


#see how the parser is extracting the content and sent to the pipeline
parser =StrOutputParser()

chain =template1 | model | parser | template2| model | parser
result =chain.invoke({'topic':'black hole'})
print(result)