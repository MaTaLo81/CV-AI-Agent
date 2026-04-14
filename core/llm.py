# LLM wrapper

# deprecated: from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI

from core.prompts import BASE_PROMPT
from utils.config import OPENAI_API_KEY

llm = ChatOpenAI(model="gpt-4o-mini")
openai_api_key=OPENAI_API_KEY

def generate_answer(query, context):
    prompt = BASE_PROMPT.format(context=context, question=query)
    # deprecated: return llm.predict(prompt)
    response = llm.invoke(prompt)
    return response.content
    