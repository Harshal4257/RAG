from langchain_text_splitters import CharacterTextSplitter

text = """
Hello my name is harshal
i live in chalisgaon
i recently graduated be
and currently i am preparing for my interviews
"""

splitter =  CharacterTextSplitter(
    chunk_size=10,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_text(text)

print(len(result))
print(result)