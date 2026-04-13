# Main orchestration

from core.retriever import get_context
from core.llm import generate_answer

def ask_agent(query):
    context = get_context(query)
    return generate_answer(query, context)
