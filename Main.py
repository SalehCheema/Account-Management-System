import Admin
import Account
import User
import key as k


def main():
    print("Welcome to the Bank")
    while True:
        print("1-Admin")
        print("2-User")
        print("3-Exit")
        choice = int(input("Choose an option:"))
        if choice == 1:
            print("\n\n")
            Admin.admin_menu()
        elif choice == 2:
            print("\n\n")
            User.user_menu()
        elif choice == 3:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    k.generate_key()
    main()              
