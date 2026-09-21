import warnings
warnings.filterwarnings('ignore')
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('Document-loaders/documents/dl-curriculum.pdf')

docs = loader.lazy_load()

for doc in docs:
    print(doc.page_content)