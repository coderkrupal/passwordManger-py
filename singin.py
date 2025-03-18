import banner
import signup
import sqlite3

banner.colored_banner()





def signin(email, password):
    try:
        conn = sqlite3.connect("my_database.db")
        cursor = conn.cursor()

        # Check if user exists
        cursor.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()

        if user:

            print(f"✅ Welcome back, {user[2]}!")  # user[2] is the username
        else:
            print("❌ Invalid email or password. Please try again.")
    
    except sqlite3.Error as e:
        print(f"❌ Database error: {e}")
    
    finally:
        conn.close()

# Example usage
if __name__ == "__main__":
    email = input("Enter email >")
    password = input("Enter password >")
    signin(email, password)
