import banner
import sqlite3

banner.colored_banner()

# Creates a database file named 'my_database.db' if it doesn't exist, or connects to it if it does
conn = sqlite3.connect("my_database.db")
cursor = conn.cursor()


cursor.execute(
    """  
                CREATE TABLE IF NOT EXISTS users(
                   id INTEGAR PRIMARY KEY ,
                   email TEXT NOT NULL UNIQUE,
                   username TEXT NOT NULL UNIQUE,
                   password TEXT NOT NULL 
                );
                
               """
)


def addData(email, username, password):
    try:
        cursor.execute(
            "INSERT INTO users (email, username, password) VALUES (?, ?, ?)",
            (email, username, password),
        )
        conn.commit()
        print("✅ Data inserted successfully!")
    except sqlite3.IntegrityError:
        print("⚠️ Error: Email or username already exists!")
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")


def signup():
    print("Signup function is running...")
    email = input("Enter a Email ID:")
    username = input("Enter a new username: ")
    password = input("Enter a new password: ")
    addData(email, username, password)


    print(f"User '{username}' signed up successfully!\n")


# Prevents automatic execution when imported
if __name__ == "__main__":
    signup()
