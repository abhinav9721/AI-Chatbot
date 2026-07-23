import streamlit as st
from chatbot import chatbot


def dashboard():

    # Session State
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


        if st.button("🏠 Dashboard", use_container_width=True):
            st.session_state.page = "dashboard"


        if st.button("💬 Start Chat", use_container_width=True):
            st.session_state.page = "chat"


        # Clear Chat Feature
        if st.button("🧹 Clear Chat", use_container_width=True):

            st.session_state.messages = [
                {
                    "role": "system",
                    "content": "You are a helpful AI Assistant."
                }
            ]

            st.success("Chat cleared successfully!")
            st.rerun()


        if st.button("📜 Chat History", use_container_width=True):
            st.session_state.page = "history"


        if st.button("👤 Profile", use_container_width=True):
            st.session_state.page = "profile"


        st.write("---")


        if st.button("🚪 Logout", use_container_width=True):

            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.page = "login"

            st.rerun()



    # =========================
    # Dashboard
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

Ask Questions

Generate Code

Solve Problems

Learn Anything
""")


            if st.button("Open Chat", use_container_width=True):

                st.session_state.page = "chat"
                st.rerun()



        with col2:

            st.info("""
### 📜 Chat History

View previous chats.

Coming Soon...
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
    # History
    # =========================

    elif st.session_state.page == "history":

        st.title("📜 Chat History")

        st.info("History feature will be added soon.")



    # =========================
    # Profile
    # =========================

    elif st.session_state.page == "profile":

        st.title("👤 Profile")

        st.write("### Username")

        st.code(st.session_state.username)

        st.info("Profile features coming soon.")