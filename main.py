import streamlit as st
from llm import invoke_ai

### Initialize chat ###
greeting  = "Hello I am a RAG assistant"
if 'messages' not in st.session_state:
    st.session_state['messages']= []
    st.session_state.messages.append({"role": "assistant", "content": greeting})

def make_msg(role, msg):
    st.chat_message(role).write(msg)
    st.session_state.messages.append({"role": role, "content": msg})

### Header ###
st.title("RAG CHATBOT")
st.markdown("Example RAG Chatbot")

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if request := st.chat_input("Make your request..."):
    ## Conversation ##
    make_msg("user", request)
    invoke_ai(request)


