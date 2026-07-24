import streamlit as st
from utils import get_ai_response

from database import save_message
def chatbot():

    st.title("🤖 AI Assistant")
    st.caption("Ask me anything...")

    # Session State
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "system",
                "content": "You are a helpful AI Assistant."
            }
        ]

    # Show Previous Messages
    for message in st.session_state.messages:

        if message["role"] != "system":

            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    # Chat Input
    prompt = st.chat_input("Type your message...")

    if prompt:

        # User Message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )
        save_message(st.session_state.username, "user", prompt)
        with st.chat_message("user"):
            st.markdown(prompt)

        # AI Response
        with st.spinner("🤖 AI is thinking..."):

            response = get_ai_response(st.session_state.messages)

        # Save AI Response
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )
        save_message(st.session_state.username, "assistant", response)
        # Show AI Response
        with st.chat_message("assistant"):
            st.markdown(response)