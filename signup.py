import sqlite3

def signup(email, username, password):
    try:
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()
        
        # Create table if not exists
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT NOT NULL UNIQUE,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        """)

        # Check if email or username already exists
        cursor.execute("SELECT * FROM users WHERE email = ? OR username = ?", (email, username))
        existing_user = cursor.fetchone()

        if existing_user:
            print("⚠️ Error: Email or username already exists!")
            return  # Exit the function to prevent inserting duplicate data

        # Insert new user
        cursor.execute("INSERT INTO users (email, username, password) VALUES (?, ?, ?)", 
                       (email, username, password))
        conn.commit()
        print(f"✅ User '{username}' signed up successfully!")
    
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    
    finally:
        conn.close()


