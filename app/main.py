# app/main.py
# Entry point

import logging
from utils.config import LOG_LEVEL

logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)

import streamlit as st
from core.agent import ask_agent

from utils.config import (
    APP_VERSION,
    CANDIDATE_NAME,
    CANDIDATE_FULL_NAME,
    CANDIDATE_LINKEDIN,
    CANDIDATE_GITHUB,
)

st.set_page_config(
    page_title=f"{CANDIDATE_FULL_NAME} AI Professional Agent!",
    page_icon="💼",
    #layout="wide",
)

st.caption(f"🧪 BETA! {APP_VERSION}")

st.title(f"{CANDIDATE_NAME}’ AI Professional Agent")

query = st.text_input(f"Ask me anything about {CANDIDATE_NAME}")

if query:
    response = ask_agent(query)
    st.write(response)

st.caption(
    "This AI assistant was created as a personal project for learning and exploration."
    "It represents my professional experience and aims to provide helpful and accurate answers."
    "Feel free to ask follow-up questions."
)

st.markdown(f"""
### About {CANDIDATE_FULL_NAME}

🔗 [LinkedIn Profile]({CANDIDATE_LINKEDIN})
🔗 [GitHub]({CANDIDATE_GITHUB})

Feel free to connect or explore my professional background in more detail.
""")