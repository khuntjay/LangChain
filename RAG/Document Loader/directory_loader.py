from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader

# load muliple files form folder 
loader = DirectoryLoader(
    path='.',     #folder patha
    glob='*.pdf',  # pattern of that file
    loader_cls= PyPDFLoader  #which loader we need to use
)

docs  = loader.load()

print(len(docs))