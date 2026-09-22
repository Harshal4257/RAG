from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(top_k_results=2, lang='en')

query = 'India Pakistan geopolitical history america relations'

docs = retriever.invoke(query)

for i, doc in enumerate(docs):
    print(f'Result : {i+1}\n')
    print(doc.page_content)

