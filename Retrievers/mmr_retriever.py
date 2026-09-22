from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEndpointEmbeddings
from langchain_core.documents import Document
from dotenv import load_dotenv
import warnings
warnings.filterwarnings('ignore')

load_dotenv()

docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

embedding = HuggingFaceEndpointEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')

vector_store = FAISS.from_documents(
    embedding=embedding,
    documents=docs
)

retriver = vector_store.as_retriever(
    search_type='mmr',
    search_kwargs = {'k':3,'lambda_mult': 0}
)

query = 'tell me about Langchain'

result = retriver.invoke(query)

for i, x in enumerate(result):
    print(f'{i+1} :', x.page_content)