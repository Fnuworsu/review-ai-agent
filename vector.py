"""
logic for vectorizing
"""
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("reviews.csv")
embeddings = OllamaEmbeddings(
    model="mxbai-embed-large",
    )

db_location = "./chroma_langchain_db"
#check if path to vector_db already exists
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []

    for i, row in df.iterrows():
        document = Document(
            page_content = row["Framework"] + " " + row["Ideal Use Cases"],
            metadata = {"rating" : row["Rating"], "date" : row["Date Rated"]},
            id = str(i)
        )
        ids.append(str(i))
        documents.append(document)
    
vector_store = Chroma(
    collection_name = "backend_framework_reviews",
    persist_directory = db_location,
    embedding_function = embeddings,
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

# connecting vector_db to ollama
retriever = vector_store.as_retriever(
    search_kwargs = {"k" : 5}
)