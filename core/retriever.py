# Vector search logic

# deprecated: from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS

# deprecated: from langchain.embeddings import OpenAIEmbeddings
from langchain_community.embeddings import OpenAIEmbeddings

from utils.config import OPENAI_API_KEY

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
vectorstore = FAISS.load_local(
    "data/embeddings",
    embeddings,
    allow_dangerous_deserialization=True
)

def get_context(query):    
    docs = vectorstore.similarity_search(query, k=3)
    return "\n".join([d.page_content for d in docs])