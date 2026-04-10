# Vector search logic

from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings

def load_vectorstore():
    return FAISS.load_local("data/embeddings", OpenAIEmbeddings())

def get_context(query):
    vs = load_vectorstore()
    docs = vs.similarity_search(query, k=3)
    return "\n".join([d.page_content for d in docs])