from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# loda openai model
model = ChatOpenAI()

# use template to pass prompt into the model
prompt = PromptTemplate(
    template="Write summary of poem /n {poem}",
    input_variables=['poem']
)

parser = StrOutputParser()

# loda text file 
loader = TextLoader('my.txt', encoding='utf-8')

docs = loader.load()

# create a pipe line for the getting result 
pipe = prompt | model | parser
result = pipe.invoke({'poem': docs[0].page_content})

print(result)

# print(docs)