# ingestion/embed.py

from ingestion.loader import load_text
from ingestion.chunking import chunk_text

from langchain_community.vectorstores import FAISS
# to_be_deprecated: from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings

from utils.config import OPENAI_API_KEY
from utils.config import DATA_PATH


def main():
    print("🔹 Loading data...")
    text = load_text(DATA_PATH)

    print("🔹 Chunking text...")
    chunks = chunk_text(text)

    print(f"🔹 Number of chunks: {len(chunks)}")

    print("🔹 Creating embeddings...")
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    vectorstore = FAISS.from_texts(chunks, embeddings)

    print("🔹 Saving vectorstore...")
    vectorstore.save_local("data/embeddings")

    print("✅ Embeddings created successfully!")


if __name__ == "__main__":
    main()