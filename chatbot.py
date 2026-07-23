import streamlit as st
from utils import get_ai_response


def chatbot():

    st.title("🤖 AI Assistant")
    st.caption("Ask me anything...")

    # Chat History
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Show old messages
    for message in st.session_state.messages:

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

        with st.chat_message("user"):
            st.markdown(prompt)

        # AI Thinking
        with st.spinner("🤖 AI is thinking..."):

            response = get_ai_response(prompt)

        # Save AI Message
        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": response
            }
        )

        # Show AI Message
        with st.chat_message("assistant"):
            st.markdown(response)