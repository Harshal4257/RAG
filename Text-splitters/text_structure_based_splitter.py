from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader

loader = TextLoader('Text-splitters/test.txt')

docs = loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0
)

result = splitter.split_documents(docs)

print(result[0].page_content)