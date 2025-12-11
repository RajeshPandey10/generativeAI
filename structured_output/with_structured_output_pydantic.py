from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

from pydantic import BaseModel,Field
from typing import Optional,Literal
load_dotenv()


def load_model():
    return ChatOpenAI(
        model='gpt-3.5-turbo',
        temperature=0.7, 
        openai_api_key=os.getenv("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1"
    )

model = load_model()
#schema
class Review(BaseModel):
    key_themes:list[str]=Field(description="write down all the key themes disscussed in the review in a list")
    summary:str=Field(description="A brief summary of the review")
    sentiment:Literal["pos","neg"]=Field(description="Return sentiment of the review either negative,positive or neutral")
    pros:Optional[list[str]]=Field(default=None,description="Write down all the pros inside a list")
    cons:Optional[list[str]]=Field(default=None,description="Write down all the cons inside a list")
    name:Optional[str]=Field(default=None,description="Write the name of the reviewer")
    
structured_model=model.with_structured_output(Review)
result = structured_model.invoke("""Lenovo is a great brand, provides excellent products with an excellent quality and at a good price(great in my case, bought it in discount).

For my personal opinion this ones is an excellent purchase not only because of the specifications, this one is a win because it comes with accessories as a case and pen, something other brands don't come and are a little more expensive ( buy the case and a pen).

The tablet is really fast, has a great streaming quality, also the screen looks beautiful because of the 1920x1200 WUXGA display and the 11" screen. Also good speakers quality ( Dolby Atmos).

U can play so many games with this, but not too heavy and fast. I don't recommend for gaming.
Great for reading, studying, watching some movies and other tasks.

Quality and great price in your hands!!.""")
print(result)