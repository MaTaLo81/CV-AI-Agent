# Entry point

import logging
from utils.config import LOG_LEVEL

logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)

import streamlit as st
from core.agent import ask_agent

st.set_page_config(
    page_title="Marcos AI Professional Agent!",
    page_icon="💼",
    #layout="wide",
)

st.caption("🧪 BETA!")

st.title("Marcos’ AI Profile Agent")

query = st.text_input("Ask me anything about Marcos")

if query:
    response = ask_agent(query)
    st.write(response)

#st.info("I'm an AI assistant trained on Marcos’ experience. I try to be helpful—but like any assistant, I might occasionally miss context 🙂")

st.caption(
    "This AI assistant was created as a personal project for learning and exploration."
    "It represents my professional experience and aims to provide helpful and accurate answers."
    "Feel free to ask follow-up questions."
)


# st.sidebar.markdown("### 👤 Marcos")
# st.sidebar.markdown(
#     "[🔗 LinkedIn](https://www.linkedin.com/in/marcostaboadalorenzo/)"
# )

st.markdown("""
### About Marcos Taboada Lorenzo

🔗 [LinkedIn Profile](https://www.linkedin.com/in/marcostaboadalorenzo/)

Feel free to connect or explore my professional background in more detail.
""")