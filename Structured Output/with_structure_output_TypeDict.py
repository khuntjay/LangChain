from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict
load_dotenv()

model = ChatOpenAI(
     model="gpt-4o-mini"
)

# Schema
class Review(TypedDict):
    summary: str
    sentiment : str
 

structure_model = model.with_structured_output(Review)

result = structure_model.invoke(""" Unfortunately, my experience wasn’t great. The service didn’t meet expectations, communication was slow, and the overall quality felt rushed. Issues took longer than promised to resolve, and I didn’t feel my concerns were taken seriously. I was hoping for a much better experience based on the reviews, but this fell short   """)

print(result)