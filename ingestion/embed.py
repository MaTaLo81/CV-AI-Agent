# ingestion/embed.py

from ingestion.loader import load_text
from ingestion.chunking import chunk_text

from langchain_community.vectorstores import FAISS
# to_be_deprecated: from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings

from utils.config import OPENAI_API_KEY
from utils.config import DATA_PATH

from pathlib import Path

EMBEDDINGS_PATH = "data/embeddings"

import shutil
import os


def clean_text(text):
    return " ".join(text.split())


def main():

    print("🔹 Loading data...")
    if not Path(DATA_PATH).exists():
      raise FileNotFoundError(f"❌ Input file not found: {DATA_PATH}")
    text = load_text(DATA_PATH)

    print("🔹 Cleaning text...")
    text = clean_text(text)

    print("🔹 Chunking text...")
    chunks = chunk_text(text)
    if not chunks:
      raise ValueError("❌ No chunks generated from input data.")
    print(f"🔹 Number of chunks: {len(chunks)}")

    for i, c in enumerate(chunks[:3]):
      print(f"\n--- Chunk {i} ---\n{c}")

    print("🔹 Creating embeddings (this may take a few seconds)...")
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    vectorstore = FAISS.from_texts(chunks, embeddings)

    print("🔹 Saving vectorstore...")
    vectorstore.save_local("data/embeddings")

    print("✅ Embeddings created successfully!")


if __name__ == "__main__":
    main()