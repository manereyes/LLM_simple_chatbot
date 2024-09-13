from langchain_ollama import OllamaLLM
import streamlit as st
import time

def make_msg(role, msg):
    st.chat_message(role).write(msg)
    st.session_state.messages.append({"role": role, "content": msg})

### Initialize LLM ###
def invoke_ai(request):
    llm = OllamaLLM(
        model="llama3.1",
        temperature=0
    )

    with st.spinner('Making response...'):
        response = llm.invoke(request)
        make_msg("assistant", response)


