import banner
import sqlite3
import os
import secrets
import string

banner.colored_banner()


# ANSI Color Codes
RED = "\033[1;31m"
GREEN = "\033[1;32m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
MAGENTA = "\033[1;35m"
RESET = "\033[0m"  # Reset to default color

conn = sqlite3.connect("passwords.db")
cursor = conn.cursor()

cursor.execute(
    """
         CREATE TABLE IF NOT EXISTS password(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
         use_pass TEXT NOT NULL UNIQUE
        )
        """
)


def CreateStrongPassword():
    Npassword = int(input("enter a number of word > "))
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(Npassword))
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{GREEN}🔐 Strong Password:", password)
    try:
        cursor.execute("INSERT INTO password (use_pass) VALUES (?)", (password,))

        conn.commit()
        print("password addes successfully")
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    finally:
        conn.close()
        
    
def webApppasswords():
    web_password = input(f"{CYAN}enter application name you generate password >")
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(characters) for _ in range(10))
    os.system("cls" if os.name == "nt" else "clear")
    print(f"{GREEN}🔐 Strong web  Password:", password)

def signin(email, password):
    try:
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        # Check if user exists
        cursor.execute(
            "SELECT * FROM users WHERE email = ? AND password = ?", (email, password)
        )
        user = cursor.fetchone()

        if user:

            print(f"✅ Welcome back, {user[2]}!")  # user[2] is the username
            os.system("cls" if os.name == "nt" else "clear")
            banner.colored_banner()
            print(f"{GREEN}1. Create strong password{RESET}")
            print(f"{BLUE}2. Web passwords{RESET}")
            main_choice = int(input(f"{RED}enter choice > "))
            if main_choice == 1:
                CreateStrongPassword()
            if main_choice == 2:
                 webApppasswords()
            if main_choice == 3:
                pass
            if main_choice == 4:
                pass
        else:
            print("❌ Invalid email or password. Please try again.")

    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")

    finally:
        conn.close()


# Example usage
