import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Path to the source data (CV/profile) used to generate embeddings
DATA_PATH = "data/raw/CV Marcos Taboada 20260415 1548.txt"