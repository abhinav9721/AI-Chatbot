import streamlit as st
from database import register_user, login_user


def login():

    st.subheader("🔐 Login")

    username = st.text_input("Username", key="login_user")

    password = st.text_input(
        "Password",
        type="password",
        key="login_pass"
    )

    if st.button("Login", use_container_width=True):

        user = login_user(username, password)

        if user:

            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.page = "dashboard"

            st.rerun()

        else:

            st.error("Invalid Username or Password")


def signup():

    st.subheader("📝 Create Account")

    username = st.text_input(
        "Username",
        key="signup_user"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="signup_pass"
    )

    confirm = st.text_input(
        "Confirm Password",
        type="password",
        key="signup_confirm"
    )

    if st.button("Create Account", use_container_width=True):

        if username == "" or password == "":

            st.warning("Please fill all fields.")

            return

        if password != confirm:

            st.error("Passwords do not match.")

            return

        if register_user(username, password):

            st.success("Account created successfully.")
            st.info("Now login with your account.")

        else:

            st.error("Username already exists.")