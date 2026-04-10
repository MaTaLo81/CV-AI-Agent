import streamlit as st
from core.agent import ask_agent

st.title("Marcos' PA Assistant")

query = st.text_input("Ask me anything about Marcos")

if query:
    response = ask_agent(query)
    st.write(response)