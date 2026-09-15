import os
from groq import Groq
from dotenv import load_dotenv

# ==========================
# Load Environment
# ==========================

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# ==========================
# AI Response
# ==========================

def get_ai_response(messages):

    try:

        completion = client.chat.completions.create(

            model="model="openai/gpt-oss-120b"",

            messages=messages,

            temperature=0.5,

            max_tokens=800,

            top_p=1,

            stream=False

        )

        return completion.choices[0].message.content

    except Exception as e:

        error = str(e)

        if "Request too large" in error:

            return (
                "⚠️ The uploaded document is too large for the current AI model.\n\n"
                "Please upload a smaller PDF (recommended under 20–25 pages) "
                "or split the document into multiple files."
            )

        elif "rate_limit_exceeded" in error:

            return (
                "⚠️ AI request limit reached.\n\n"
                "Please wait a few seconds and try again."
            )

        else:

            return f"❌ Error: {error}"
