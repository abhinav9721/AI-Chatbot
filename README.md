# 🤖 AI Assistant Chatbot

An AI-powered chatbot built using **Streamlit** and **Groq AI API**.
This chatbot supports natural conversations and provides AI responses with conversation memory.

## 🚀 Features

* 🔐 User Authentication (Login & Signup)
* 💬 AI Chat Assistant
* 🧠 Conversation Memory
* 📜 Chat History
* 👤 User Profile Dashboard
* ⚙️ Settings Panel
* 🌙 Dark Theme Support
* 🗄️ SQLite Database Integration
* 🌐 Streamlit Deployment Ready

## 🛠️ Technologies Used

* Python
* Streamlit
* Groq AI API
* SQLite Database
* Pandas
* Python-dotenv

## 📂 Project Structure

```
AI-Chatbot
│
├── app.py              # Main application
├── chatbot.py          # Chat interface
├── dashboard.py        # Dashboard and UI
├── auth.py             # Login and Signup
├── database.py         # Database operations
├── utils.py            # AI API handling
├── requirements.txt    # Project dependencies
├── .env                # API keys (not uploaded)
└── README.md
```

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
```

Move into project folder:

```bash
cd AI-Chatbot
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 🔑 Environment Setup

Create a `.env` file:

```
GROQ_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your Groq API key.

## ▶️ Run Application

Start Streamlit:

```bash
streamlit run app.py
```

The application will open in your browser.

## 🔮 Future Improvements

* File upload support
* Image understanding
* PDF export
* Voice assistant
* Advanced UI improvements
* Cloud deployment

## 👨‍💻 Author

Abhinav Tripathi

AI Chatbot Project | Python + Streamlit + Groq AI
