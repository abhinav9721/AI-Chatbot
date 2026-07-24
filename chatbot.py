import streamlit as st

from utils import get_ai_response
from database import save_message
import streamlit as st

from utils import get_ai_response
from database import save_message


# ==========================
# Chatbot UI CSS
# ==========================

st.markdown(
    """

<style>


/* Chat Title */

h1 {

    text-align: center;

    color: #38bdf8;

}



/* Caption */

.stCaption {

    text-align: center;

}



/* Chat Messages */

[data-testid="stChatMessage"] {

    border-radius: 18px;

    padding: 15px;

    margin-bottom: 12px;

}



/* User Message */

[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {

    background-color: #1e40af;

}



/* Assistant Message */

[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {

    background-color: #1f2937;

}



/* Chat Input */

[data-testid="stChatInput"] textarea {

    border-radius: 15px;

    padding: 12px;

}



/* Spinner */

.stSpinner {

    text-align: center;

}


</style>

""",

unsafe_allow_html=True

)


def chatbot():

    st.title("🤖 AI Assistant")
    st.caption("Ask me anything...")



    # ==========================
    # Session State Initialize
    # ==========================

    if "messages" not in st.session_state:

        st.session_state.messages = [

            {
                "role": "system",
                "content": "You are a helpful AI Assistant."
            }

        ]


    if "chat_id" not in st.session_state:

        st.session_state.chat_id = None


    if "username" not in st.session_state:

        st.session_state.username = "user"



    # ==========================
    # Show Previous Messages
    # ==========================

    for message in st.session_state.messages:


        if message["role"] == "system":

            continue


        with st.chat_message(
            message["role"]
        ):

            st.markdown(
                message["content"]
            )



    # ==========================
    # Chat Input
    # ==========================

    prompt = st.chat_input(
        "💬 Ask anything..."
    )


    if prompt:


        # ==========================
        # Display User Message
        # ==========================

        with st.chat_message("user"):

            st.markdown(
                prompt
            )



        # ==========================
        # Save User Message
        # ==========================

        st.session_state.messages.append(

            {
                "role": "user",
                "content": prompt
            }

        )


        save_message(

            st.session_state.username,

            "user",

            prompt,

            st.session_state.get("chat_id")

        )



        # ==========================
        # Conversation Memory
        # ==========================

        history = []


        for message in st.session_state.messages[-10:]:


            if message["role"] != "system":


                history.append(

                    {
                        "role": message["role"],
                        "content": message["content"]
                    }

                )



        # ==========================
        # AI Messages
        # ==========================

        messages_for_ai = [

            {

                "role": "system",

                "content": """

You are a professional AI assistant.

Rules:

1. Continue conversation naturally.

2. Remember previous messages.

3. Answer in Hindi, Hinglish or English according to user.

4. Give clear and helpful answers.

5. Understand spelling mistakes and user intent.

"""

            }

        ]



        messages_for_ai.extend(

            history

        )



        # ==========================
        # AI Response
        # ==========================

        with st.spinner(
            "🤖 AI is thinking..."
        ):


            response = get_ai_response(

                messages_for_ai

            )



        # ==========================
        # Error Handling
        # ==========================

        if response is None:

            response = (
                "❌ Something went wrong. Please try again."
            )


        elif not isinstance(response, str):

            response = str(response)



        elif response.strip() == "":

            response = (
                "⚠️ No response received."
            )



        # ==========================
        # Save AI Response
        # ==========================

        st.session_state.messages.append(

            {
                "role": "assistant",
                "content": response
            }

        )


        save_message(

            st.session_state.username,

            "assistant",

            response,

            st.session_state.get("chat_id")

        )



        # ==========================
        # Show AI Response
        # ==========================

        with st.chat_message(
            "assistant"
        ):

            st.markdown(
                response
            )