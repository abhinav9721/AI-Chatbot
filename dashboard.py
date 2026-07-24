import streamlit as st

from chatbot import chatbot

from database import (
    get_chat_history,
    clear_chat_history,
    get_profile,
    create_new_chat
)



# ==========================
# GLOBAL CSS
# ==========================

def apply_css():


    st.markdown(
        """

<style>


/* Sidebar */

[data-testid="stSidebar"] {

    background-color:#111827;

}


/* Main Heading */

h1,h2,h3 {

    color:#38bdf8;

}


/* Buttons */

.stButton button {

    border-radius:12px;

    height:45px;

    font-weight:600;

}



/* Cards */

div[data-testid="stAlert"] {

    border-radius:15px;

}


/* Chat */

[data-testid="stChatMessage"] {

    border-radius:15px;

    padding:10px;

}


/* Metrics */

[data-testid="stMetric"] {

    background:#1e293b;

    padding:15px;

    border-radius:15px;

}


</style>

        """,

        unsafe_allow_html=True
    )





# ==========================
# DARK THEME
# ==========================


def apply_dark_theme():


    st.markdown(
        """

<style>


.stApp {

background-color:#0E1117;

color:white;

}



[data-testid="stSidebar"] {

background-color:#111827;

}



h1,h2,h3,p,label {

color:white;

}



.stButton button {

border-radius:12px;

}



[data-testid="stChatMessage"] {

background-color:#1f2937;

border-radius:15px;

}


</style>


        """,

        unsafe_allow_html=True
    )





# ==========================
# DASHBOARD FUNCTION
# ==========================


def dashboard():


    apply_css()


    # Theme State

    if "dark_mode" not in st.session_state:

        st.session_state.dark_mode = False



    if st.session_state.dark_mode:

        apply_dark_theme()
            # ==========================
    # SESSION STATE
    # ==========================

    if "page" not in st.session_state:

        st.session_state.page = "dashboard"


    if "chat_id" not in st.session_state:

        st.session_state.chat_id = None


    if "messages" not in st.session_state:

        st.session_state.messages = [

            {
                "role":"system",
                "content":"You are a helpful AI Assistant."
            }

        ]



    # ==========================
    # SIDEBAR
    # ==========================


    with st.sidebar:


        st.title("🤖 AI Assistant")


        st.write("---")


        st.write(
            f"👋 Welcome, {st.session_state.username}"
        )


        st.write("---")



        # Dashboard

        if st.button(
            "🏠 Dashboard",
            use_container_width=True
        ):

            st.session_state.page="dashboard"

            st.rerun()



        # Chat

        if st.button(
            "💬 Start Chat",
            use_container_width=True
        ):

            st.session_state.page="chat"

            st.rerun()




        # New Chat

        if st.button(
            "🆕 New Chat",
            use_container_width=True
        ):


            new_id=create_new_chat(
                st.session_state.username
            )


            st.session_state.chat_id=new_id



            st.session_state.messages=[

                {
                    "role":"system",
                    "content":"You are a helpful AI Assistant."
                }

            ]


            st.session_state.page="chat"

            st.rerun()
                    # Clear Chat

        if st.button(
            "🧹 Clear Chat",
            use_container_width=True
        ):


            clear_chat_history(
                st.session_state.username
            )


            st.session_state.messages=[

                {
                    "role":"system",
                    "content":"You are a helpful AI Assistant."
                }

            ]


            st.success(
                "Chat cleared successfully"
            )


            st.rerun()



        # History

        if st.button(
            "📜 Chat History",
            use_container_width=True
        ):


            st.session_state.page="history"

            st.rerun()



        # Profile

        if st.button(
            "👤 Profile",
            use_container_width=True
        ):


            st.session_state.page="profile"

            st.rerun()



        # Settings

        if st.button(
            "⚙️ Settings",
            use_container_width=True
        ):


            st.session_state.page="settings"

            st.rerun()



        st.write("---")



        # Logout


        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):


            st.session_state.logged_in=False

            st.session_state.username=""

            st.session_state.page="login"


            st.rerun()
                # ==========================
    # DASHBOARD PAGE
    # ==========================


    if st.session_state.page=="dashboard":


        st.title("🤖 AI Assistant")



        st.markdown(
f"""

# 👋 Welcome {st.session_state.username}

### Your Personal AI Assistant is Ready 🚀

"""
        )


        col1,col2=st.columns(2)



        with col1:


            st.success(
"""
### 💬 Chat

Ask questions

Generate code

Learn anything
"""
            )


            if st.button(
                "Open Chat",
                use_container_width=True
            ):


                st.session_state.page="chat"

                st.rerun()



        with col2:


            st.info(
"""
### 📜 History

View your conversations
"""
            )




    # ==========================
    # CHAT PAGE
    # ==========================


    elif st.session_state.page=="chat":


        chatbot()
            # ==========================
    # HISTORY PAGE
    # ==========================


    elif st.session_state.page=="history":


        st.title("📜 Chat History")


        history=get_chat_history(
            st.session_state.username
        )


        if not history:


            st.info(
                "No chat history found."
            )


        else:


            for chat_id,role,message,date in history:


                with st.chat_message(role):

                    st.markdown(message)


                st.caption(date)






    # ==========================
    # PROFILE PAGE
    # ==========================


    elif st.session_state.page=="profile":


        st.title("👤 My Profile")



        profile=get_profile(
            st.session_state.username
        )



        if profile:


            st.metric(
                "Username",
                profile["username"]
            )


            st.metric(
                "Total Messages",
                profile["total_messages"]
            )


            st.metric(
                "AI Replies",
                profile["ai_messages"]
            )


        else:


            st.warning(
                "Profile not found"
            )
                # ==========================
    # SETTINGS PAGE
    # ==========================


    elif st.session_state.page=="settings":


        st.title("⚙️ Settings")



        st.subheader(
            "🎨 Appearance"
        )



        st.session_state.dark_mode = st.toggle(

            "🌙 Dark Theme",

            value=st.session_state.dark_mode

        )



        if st.session_state.dark_mode:


            st.success(
                "Dark Theme Enabled"
            )


            apply_dark_theme()



        else:


            st.info(
                "Light Theme Enabled"
            )




        st.write("---")



        st.subheader(
            "💬 Chat Settings"
        )



        if st.button(
            "🧹 Clear Current Chat",
            use_container_width=True
        ):


            st.session_state.messages=[

                {
                    "role":"system",
                    "content":"You are a helpful AI Assistant."
                }

            ]


            st.success(
                "Current chat cleared"
            )


            st.rerun()




        st.write("---")



        st.subheader(
            "📄 Export"
        )


        st.info(
            "PDF Export feature coming soon."
        )
