import accountmanger as am



def admin_menu():   
    while(True):
        accounts=am.AccountManager()
        print("1-Create Account")
        print("2-Show Details")
        print("3-Show Transaction")
        print('4-Delete Account')
        print('5-Freeze Account')
        print('6-Set Transaction Limit for User')
        print('8-Monthly,Weekly, Yearly Reports')
        print('9-Back')
        choice=int(input("Choose an option:"))
        if choice==1:
            account_id = input("Enter account ID:")
            if account_id in accounts.accounts:
                print("Account already exists.")
                return
            name = input("Enter name:")
            pin = input("Enter pin:")
            accounts.create_account(account_id, name, pin)
        elif choice==2:
            account_id = input("Enter account ID:")
            accounts.show_account_details(account_id)
            print("\n\n")
            
        elif choice==3:
            account_id = input("Enter account ID (Leave Blank for All transaction History):")
            if account_id == "":
                accounts.show_transaction_history()
            else:
                accounts.show_transaction_history(account_id)
            print("\n\n")    
        elif choice==4:
            account_id = input("Enter account ID:")
            accounts.delete_account(account_id)
            print("\n\n")

        elif choice==5:
            account_id = input("Enter account ID:")
            accounts.freeze_account(account_id)
            print("\n\n")
        elif choice==6:
            account_id = input("Enter account ID:")
            limit = int(input("Enter limit:"))
            
            accounts.set_transaction_limit(account_id, limit)
            print("\n\n")
        elif choice==8:
            period = input("Enter period (monthly, weekly, yearly):")
            accounts.generate_report(period)
            print("\n\n")
        elif choice==9:
            print("\n\n")
            return
        else:
            print("Invalid choice.!! Please try again")
            return

if __name__ == "__main__":
    admin_menu()