from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_core.documents import Document
from langchain_chroma import Chroma
from dotenv import load_dotenv

load_dotenv()

documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models.")
]

embeddings = HuggingFaceEndpointEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')

vector_store = Chroma.from_documents(
    embedding=embeddings,
    documents=documents,
    collection_name='sample'
)

retriever = vector_store.as_retriever(search_kwargs={'k': 2})

query = 'What is chrome uses for?'

result = retriever.invoke(query)

for i, doc in enumerate(result):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)
    
