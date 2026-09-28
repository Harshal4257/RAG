from langchain_community.document_loaders import CSVLoader

loader = CSVLoader('Document-loaders/documents/Social_Network_Ads.csv')

docs = loader.load()

print(docs[0].page_content)
