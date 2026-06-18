import streamlit as st
from run_graph import ask_question

st.set_page_config(
    page_title="IPL Intelligence Assistant",
    page_icon="🏏",
    layout="wide"
)

st.title("🏏 IPL Intelligence Assistant")
st.markdown(
    "Multi-Agent RAG using LangGraph + ChromaDB + Groq"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.write(message["content"])

question = st.chat_input(
    "Ask an IPL Question..."
)

if question:

    with st.spinner("Thinking..."):

        result = ask_question(question)

    st.session_state.messages.append(
        {"role": "user", "content": question}
    )

    st.session_state.messages.append(
        {"role": "assistant", "content": result}
    )

    st.rerun()