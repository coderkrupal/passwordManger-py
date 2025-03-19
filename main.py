import banner
import signup
import Signin


banner.colored_banner()


def main():
    print("1.log in")
    print("2.sign up")
    user_choice = int(input("Enter Your Choice > "))
    if user_choice == 1:
        email = input("Enter email >")
        password = input("Enter password >")
        Signin.signin(email, password)
    if user_choice == 2:
        email = input("Enter email: ")
        username = input("Enter username: ")
        password = input("Enter password: ")
        signup.signup(email, username, password)
       
        


if __name__ == "__main__":
    main()
