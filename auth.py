import streamlit as st

from database import register_user, login_user



# ==========================
# Auth CSS
# ==========================

st.markdown(
    """

<style>


/* Auth Box */

.auth-box {

    background-color: #1e293b;

    padding: 30px;

    border-radius: 20px;

    margin-top: 20px;

}



/* Sub Heading */

h2 {

    color: #38bdf8;

}



/* Input Fields */

.stTextInput input {

    border-radius: 12px;

    height: 45px;

}



/* Buttons */

.stButton > button {

    border-radius: 12px;

    height: 45px;

    font-weight: 600;

}



</style>


""",

unsafe_allow_html=True

)




def login():


    st.subheader(
        "🔐 Login"
    )


    st.write(
        "Welcome back! Login to continue 🚀"
    )


    username = st.text_input(

        "Username",

        key="login_user"

    )


    password = st.text_input(

        "Password",

        type="password",

        key="login_pass"

    )



    if st.button(

        "🚀 Login",

        use_container_width=True

    ):


        user = login_user(

            username,

            password

        )


        if user:


            st.session_state.logged_in = True


            st.session_state.username = username


            st.session_state.page = "dashboard"


            st.success(
                "Login successful!"
            )


            st.rerun()



        else:


            st.error(
                "❌ Invalid Username or Password"
            )





def signup():


    st.subheader(
        "📝 Create Account"
    )


    st.write(
        "Create your AI Assistant account ✨"
    )


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



    if st.button(

        "✨ Create Account",

        use_container_width=True

    ):


        if username == "" or password == "":


            st.warning(
                "Please fill all fields."
            )

            return



        if password != confirm:


            st.error(
                "Passwords do not match."
            )

            return



        if register_user(

            username,

            password

        ):


            st.success(
                "Account created successfully."
            )


            st.info(
                "Now login with your account."
            )



        else:


            st.error(
                "Username already exists."
            )