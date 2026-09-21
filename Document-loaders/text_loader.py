from langchain_community.document_loaders import TextLoader
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader('Document-loaders/documents/cricket.txt',encoding='utf-8')

docs = loader.load()

prompt = PromptTemplate(
    template='Write 4 lines summary about following poem\n {poem}',
    input_variables=['poem']
)

llm = HuggingFaceEndpoint(
    model='openai/gpt-oss-120b',
    task='text-generation'
)

model = ChatHuggingFace(llm=llm)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'poem': docs[0].page_content})

print(result)
