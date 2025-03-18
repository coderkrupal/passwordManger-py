import banner
import signup

banner.colored_banner()


def main():
    print("1.log in")
    print("2.sign up")
    user_choice = int(input("Enter Your Choice > "))
    if(user_choice ==1):
        pass
    if(user_choice == 2):
        signup.signup()
    
    
if __name__ == "__main__":
    main()