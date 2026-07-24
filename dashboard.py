import streamlit as st
from chatbot import chatbot
from database import get_chat_history


def dashboard():

    # =========================
    # Session State
    # =========================
    if "page" not in st.session_state:
        st.session_state.page = "dashboard"

    # =========================
    # Sidebar
    # =========================
    with st.sidebar:

        st.title("🤖 AI Assistant")

        st.write("---")

        st.write(f"👋 Welcome, {st.session_state.username}")

        st.write("---")

        # Dashboard
        if st.button("🏠 Dashboard", use_container_width=True):
            st.session_state.page = "dashboard"
            st.rerun()

        # Chat
        if st.button("💬 Start Chat", use_container_width=True):
            st.session_state.page = "chat"
            st.rerun()

        # Clear Chat
        if st.button("🧹 Clear Chat", use_container_width=True):

            st.session_state.messages = [
                {
                    "role": "system",
                    "content": "You are a helpful AI Assistant."
                }
            ]

            st.success("Chat cleared successfully!")
            st.session_state.page = "chat"
            st.rerun()

        # History
        if st.button("📜 Chat History", use_container_width=True):
            st.session_state.page = "history"
            st.rerun()

        # Profile
        if st.button("👤 Profile", use_container_width=True):
            st.session_state.page = "profile"
            st.rerun()

        st.write("---")

        # Logout
        if st.button("🚪 Logout", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.page = "login"
            st.rerun()

    # =========================
    # Dashboard Page
    # =========================
    if st.session_state.page == "dashboard":

        st.title("🤖 AI Assistant")

        st.markdown(
            f"""
# 👋 Welcome, {st.session_state.username}

### Your Personal AI Assistant is Ready 🚀
"""
        )

        st.write("")

        col1, col2 = st.columns(2)

        with col1:

            st.success("""
### 💬 Start Chat

• Ask Questions

• Generate Code

• Solve Problems

• Learn Anything
""")

            if st.button("Open Chat", use_container_width=True):
                st.session_state.page = "chat"
                st.rerun()

        with col2:

            st.info("""
### 📜 Chat History

View all your previous conversations.
""")

        st.write("")

        col3, col4 = st.columns(2)

        with col3:

            st.warning("""
### 👤 Profile

Manage your account.

Coming Soon...
""")

        with col4:

            st.error("""
### ⚙️ Settings

Dark Theme

Export Chat

Coming Soon...
""")

    # =========================
    # Chat Page
    # =========================
    elif st.session_state.page == "chat":

        chatbot()

    # =========================
    # History Page
    # =========================
    elif st.session_state.page == "history":

        st.title("📜 Chat History")

        history = get_chat_history(st.session_state.username)

        if len(history) == 0:

            st.info("No chat history found.")

        else:

            for role, message, created_at in history:

                with st.chat_message(role):
                    st.markdown(message)

                st.caption(f"🕒 {created_at}")

    # =========================
    # Profile Page
    # =========================
    elif st.session_state.page == "profile":

        st.title("👤 Profile")

        st.write("### Username")

        st.code(st.session_state.username)

        st.info("More profile features coming soon.")