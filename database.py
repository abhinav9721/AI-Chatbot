import sqlite3
import hashlib


DATABASE = "users.db"


# ==========================
# Database Connection
# ==========================

def get_connection():
    return sqlite3.connect(DATABASE)


# ==========================
# Password Hashing
# ==========================

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


# ==========================
# Create Tables
# ==========================

def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    # Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # Chat History Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS chat_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
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

    conn = get_connection()
    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO users(username, password)
            VALUES(?, ?)
            """,
            (username, hash_password(password))
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

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE username=? AND password=?
        """,
        (username, hash_password(password))
    )

    user = cursor.fetchone()

    conn.close()

    return user


# ==========================
# Chat History Functions
# ==========================

def save_message(username, role, message):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO chat_history(username, role, message)
        VALUES (?, ?, ?)
        """,
        (username, role, message)
    )

    conn.commit()
    conn.close()


def get_chat_history(username):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT role, message, created_at
        FROM chat_history
        WHERE username=?
        ORDER BY id ASC
        """,
        (username,)
    )

    history = cursor.fetchall()

    conn.close()

    return history


def clear_chat_history(username):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM chat_history
        WHERE username=?
        """,
        (username,)
    )

    conn.commit()
    conn.close()