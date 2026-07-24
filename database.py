import sqlite3
import hashlib


# ==========================
# Database Files
# ==========================

USER_DATABASE = "users.db"
CHAT_DATABASE = "chatbot.db"



# ==========================
# Connections
# ==========================

def get_user_connection():

    return sqlite3.connect(
        USER_DATABASE
    )



def get_chat_connection():

    return sqlite3.connect(
        CHAT_DATABASE
    )



# ==========================
# Password Hash
# ==========================

def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()



# ==========================
# Create Tables
# ==========================

def create_tables():


    # USER DATABASE

    conn = get_user_connection()

    cursor = conn.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT UNIQUE NOT NULL,

            password TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)


    conn.commit()

    conn.close()



    # CHAT DATABASE

    conn = get_chat_connection()

    cursor = conn.cursor()



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_sessions(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            username TEXT NOT NULL,

            title TEXT DEFAULT 'New Chat',

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)



    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chat_history(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            chat_id INTEGER,

            username TEXT NOT NULL,

            role TEXT NOT NULL,

            message TEXT NOT NULL,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)



    conn.commit()

    conn.close()
    
# ==========================
# Register User
# ==========================

def register_user(username, password):


    conn = get_user_connection()

    cursor = conn.cursor()



    try:


        cursor.execute(
            """
            INSERT INTO users
            (
                username,
                password
            )

            VALUES(?,?)
            """,

            (
                username,
                hash_password(password)
            )

        )


        conn.commit()


        return True



    except sqlite3.IntegrityError:


        return False



    finally:


        conn.close()




# ==========================
# Login User
# ==========================

def login_user(username, password):


    conn = get_user_connection()

    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT *

        FROM users

        WHERE username=? AND password=?

        """,

        (
            username,
            hash_password(password)
        )

    )


    user = cursor.fetchone()


    conn.close()



    return user





# ==========================
# Create New Chat
# ==========================

def create_new_chat(username, title="New Chat"):


    conn = get_chat_connection()

    cursor = conn.cursor()



    cursor.execute(
        """
        INSERT INTO chat_sessions
        (
            username,
            title
        )

        VALUES(?,?)

        """,

        (
            username,
            title
        )

    )


    chat_id = cursor.lastrowid



    conn.commit()

    conn.close()



    return chat_id





# ==========================
# Save Chat Message
# ==========================

def save_message(
    username,
    role,
    message,
    chat_id=None
):


    conn = get_chat_connection()

    cursor = conn.cursor()



    # Agar chat_id nahi hai to new chat create karo

    if chat_id is None:


        chat_id = create_new_chat(
            username
        )



    cursor.execute(
        """
        INSERT INTO chat_history
        (
            chat_id,
            username,
            role,
            message
        )

        VALUES(?,?,?,?)

        """,

        (
            chat_id,
            username,
            role,
            message
        )

    )


    conn.commit()

    conn.close()
    
# ==========================
# Get Chat History
# ==========================

def get_chat_history(username):


    conn = get_chat_connection()

    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT

            chat_id,

            role,

            message,

            created_at


        FROM chat_history


        WHERE username=?


        ORDER BY id ASC

        """,

        (
            username,
        )

    )


    history = cursor.fetchall()


    conn.close()



    return history





# ==========================
# Get Previous Chats
# ==========================

def get_previous_chats(username):


    conn = get_chat_connection()

    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT

            id,

            title,

            created_at


        FROM chat_sessions


        WHERE username=?


        ORDER BY id DESC

        """,

        (
            username,
        )

    )


    chats = cursor.fetchall()


    conn.close()



    return chats





# ==========================
# Clear Chat History
# ==========================

def clear_chat_history(username):


    conn = get_chat_connection()

    cursor = conn.cursor()



    cursor.execute(
        """
        DELETE FROM chat_history

        WHERE username=?

        """,

        (
            username,
        )

    )


    conn.commit()

    conn.close()
    
# ==========================
# User Profile
# ==========================

def get_profile(username):


    # USER DATA

    conn = get_user_connection()

    cursor = conn.cursor()



    cursor.execute(
        """
        SELECT

            username,

            created_at


        FROM users


        WHERE username=?

        """,

        (
            username,
        )

    )


    user = cursor.fetchone()



    conn.close()



    if user is None:

        return None




    # CHAT DATA

    conn = get_chat_connection()

    cursor = conn.cursor()



    # Total Messages

    cursor.execute(
        """
        SELECT COUNT(*)

        FROM chat_history

        WHERE username=?

        """,

        (
            username,
        )

    )


    total_messages = cursor.fetchone()[0]




    # User Messages

    cursor.execute(
        """
        SELECT COUNT(*)

        FROM chat_history

        WHERE username=?

        AND role='user'

        """,

        (
            username,
        )

    )


    user_messages = cursor.fetchone()[0]




    # AI Messages

    cursor.execute(
        """
        SELECT COUNT(*)

        FROM chat_history

        WHERE username=?

        AND role='assistant'

        """,

        (
            username,
        )

    )


    ai_messages = cursor.fetchone()[0]



    conn.close()




    return {


        "username": user[0],


        "created_at": user[1],


        "total_messages": total_messages,


        "user_messages": user_messages,


        "ai_messages": ai_messages

    }

