# LLM wrapper

from langchain.chat_models import ChatOpenAI
from core.prompts import BASE_PROMPT

llm = ChatOpenAI(model="gpt-4o-mini")

def generate_answer(query, context):
    prompt = BASE_PROMPT.format(context=context, question=query)
    return llm.predict(prompt)