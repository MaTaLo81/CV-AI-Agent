# utils/config.py

import logging

import os
from dotenv import load_dotenv

LOG_LEVEL = logging.INFO
logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# To be replaced with your info: 
APP_VERSION = "v1.0"
CANDIDATE_NAME = "Marcos"
CANDIDATE_FULL_NAME = "Marcos Taboada Lorenzo"
CANDIDATE_LINKEDIN = "https://www.linkedin.com/in/marcostaboadalorenzo/"
CANDIDATE_GITHUB = "https://github.com/MaTaLo81/"
