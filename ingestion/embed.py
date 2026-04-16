# ingestion/embed.py

import logging
from utils.config import LOG_LEVEL

logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)

from ingestion.loader import load_text
from ingestion.chunking import chunk_text

from langchain_community.vectorstores import FAISS
# to_be_deprecated: from langchain_community.embeddings import OpenAIEmbeddings
from langchain_openai import OpenAIEmbeddings

from utils.config import OPENAI_API_KEY

from pathlib import Path

# Path to the source data (CV/profile) used to generate embeddings
DATA_PATH_CV_TXT = "data/raw/CV Marcos Taboada 20260415 1548.txt"

def clean_text(text):
    return " ".join(text.split())


def main():

    logging.info("🔹 Loading data...")    
    if not Path(DATA_PATH_CV_TXT).exists():
      raise FileNotFoundError(f"❌ Input file not found: {DATA_PATH_CV_TXT}")
    text = load_text(DATA_PATH_CV_TXT)

    logging.info("🔹 Cleaning text...")    
    text = clean_text(text)

    logging.info("🔹 Chunking text...")    
    chunks = chunk_text(text)
    if not chunks:
      raise ValueError("❌ No chunks generated from input data.")
    logging.info(f"🔹 Number of chunks: {len(chunks)}")    

    for i, c in enumerate(chunks[:3]):
      logging.debug(f"\n--- Chunk {i} ---\n{c}")      

    logging.info("🔹 Creating embeddings (this may take a few seconds)...")
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

    vectorstore = FAISS.from_texts(chunks, embeddings)

    logging.info("🔹 Saving vectorstore...")
    vectorstore.save_local("data/embeddings")

    logging.info("✅ Embeddings created successfully!")


if __name__ == "__main__":
    main()