import streamlit as st

from database import create_tables
from auth import login, signup
from dashboard import dashboard


# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# -------------------------------
# Create Database
# -------------------------------
create_tables()

# -------------------------------
# Session State
# -------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "page" not in st.session_state:
    st.session_state.page = "login"

if "username" not in st.session_state:
    st.session_state.username = ""


# -------------------------------
# Login / Signup Screen
# -------------------------------
if not st.session_state.logged_in:

    st.title("🤖 AI Assistant")

    tab1, tab2 = st.tabs(["Login", "Signup"])

    with tab1:
        login()

    with tab2:
        signup()

# -------------------------------
# Dashboard
# -------------------------------
else:

    dashboard()