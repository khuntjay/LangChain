from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('C:\\Users\\khunt\\Desktop\\LangChain\\myenv\\Scripts\\demo.pdf')

docs = loader.load()

print(docs[0].page_content)