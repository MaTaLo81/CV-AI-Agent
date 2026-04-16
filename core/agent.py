# core/agent.py
# Main orchestration

import logging
from utils.config import LOG_LEVEL

logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)

from core.retriever import get_context
from core.llm import generate_answer

def ask_agent(query):
    context = get_context(query)
    return generate_answer(query, context)
