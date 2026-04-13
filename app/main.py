# Entry point

#import sys
#import os
import streamlit as st
from core.agent import ask_agent

#sys.path.append(os.path.dirname(os.path.dirname(__file__)))

st.title("Marcos' PA Assistant")

query = st.text_input("Ask me anything about Marcos")

if query:
    response = ask_agent(query)
    st.write(response)