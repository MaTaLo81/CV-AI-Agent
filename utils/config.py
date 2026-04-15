
import logging

import os
from dotenv import load_dotenv

LOG_LEVEL = logging.DEBUG
logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Path to the source data (CV/profile) used to generate embeddings
DATA_PATH = "data/raw/CV Marcos Taboada 20260415 1548.txt"