import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def get_ai_response(messages):

    try:

        completion = client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=messages,

            temperature=0.7,
            max_tokens=1024

        )

        return completion.choices[0].message.content

    except Exception as e:

        return f"Error: {e}"