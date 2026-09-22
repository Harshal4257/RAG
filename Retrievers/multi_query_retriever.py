from langchain_huggingface import HuggingFaceEndpointEmbeddings, HuggingFaceEndpoint, ChatHuggingFace
from langchain_classic.retrievers.multi_query import MultiQueryRetriever
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
import warnings
warnings.filterwarnings('ignore')

load_dotenv()

documents = [
    Document(page_content="Regular walking boosts heart health and can reduce symptoms of depression.", metadata={"source": "H1"}),
    Document(page_content="Consuming leafy greens and fruits helps detox the body and improve longevity.", metadata={"source": "H2"}),
    Document(page_content="Deep sleep is crucial for cellular repair and emotional regulation.", metadata={"source": "H3"}),
    Document(page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity.", metadata={"source": "H4"}),
    Document(page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy.", metadata={"source": "H5"}),
    Document(page_content="The solar energy system in modern homes helps balance electricity demand.", metadata={"source": "I1"}),
    Document(page_content="Python balances readability with power, making it a popular system design language.", metadata={"source": "I2"}),
    Document(page_content="Photosynthesis enables plants to produce energy by converting sunlight.", metadata={"source": "I3"}),
    Document(page_content="The 2022 FIFA World Cup was held in Qatar and drew global energy and excitement.", metadata={"source": "I4"}),
    Document(page_content="Black holes bend spacetime and store immense gravitational energy.", metadata={"source": "I5"})
]

embeddings = HuggingFaceEndpointEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')

vector_store = FAISS.from_documents(
    embedding=embeddings,
    documents=documents
)

retriever = vector_store.as_retriever(search_type='similarity', search_kwargs = {'k':5})

llm = HuggingFaceEndpoint(
    model='openai/gpt-oss-120b',
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

multiretriever = MultiQueryRetriever.from_llm(
    retriever=vector_store.as_retriever(
        search_kwargs = {'k':5}
    ),
    llm=model
)

query = "How to improve energy levels and maintain balance?"

similarity_result = retriever.invoke(query)
multiquery_result = multiretriever.invoke(query)


for i, doc in enumerate(similarity_result):
    print(f'\n {i+1} : ')
    print(doc.page_content)

print("*" * 150)

for i, doc in enumerate(multiquery_result):
    print(f'\n {i+1} : ')
    print(doc.page_content)