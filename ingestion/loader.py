# ingestion/loader.py

import logging
from utils.config import LOG_LEVEL

logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)

def load_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
    