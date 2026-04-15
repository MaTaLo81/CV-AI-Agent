# Prompt templates

import logging
from utils.config import LOG_LEVEL

logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)

BASE_PROMPT = """
You are Marcos' professional AI assistant.

Rules:
- Be accurate and honest
- Do not invent experience
- If unsure, say it clearly

Context:
{context}

Question:
{question}

Answer:
"""
