import accountmanger as am
import Account as ac
import Encrytion as e

import key as k

def user_menu():
    
    accounts=am.AccountManager()
    id = input("Enter account ID:")
    if id not in accounts.accounts:
        print("Account does not exist")
        return
    
    obj=accounts.accounts[id]
    key=k.load_key() 
    em=e.EncryptionManager(key)
    pin=input("Enter Pin:")

    decrypted_pin=em.decrypt(obj.pin)
    if pin != decrypted_pin:
        print("Invalid Pin")
        return

    while True:
        print("1-Deposit Amount")
        print("2-Check Amount")
        print("3-Print Statement")
        print('4-Transfer amount to other user')
        print('5-Withdraw Amount')
        print('6-Set Pin code')
        print('8-Transaction History')
        print('9-Back')
        choice=int(input("Choose an option:"))

        if choice==1:
            amount = int(input("Enter amount:"))
            obj.deposit(amount)
            accounts.accounts[id] = obj
            accounts.save_account()
            print("Amount deposited successfully")
            print("\n\n")
        
            
        elif choice==2:
            obj.check_amount()
        elif choice==3:
            obj.statement()
        elif choice==4:
            target_id = input("Enter target account ID:")
            if target_id not in accounts.accounts:
                print("Account does not exist")
                print("\n\n")
                return
            target_account = accounts.accounts[target_id]
            amount = int(input("Enter amount:"))
            obj.transfer(amount, target_account)
            accounts.accounts[id] = obj
            accounts.accounts[target_id] = target_account
            accounts.save_account()
            print("Amount transferred successfully")
            print("\n\n")
        elif choice==5:
            amount = int(input("Enter amount:"))
            obj.withdraw(amount)
            accounts.accounts[id] = obj
            accounts.save_account()
            print("Amount withdrawn successfully")
            print("\n\n")

        elif choice==6:
            new_pin = input("Enter new pin:")
            obj.change_pin(new_pin)
            accounts.accounts[id] = obj
            accounts.save_account()
            print("Pin changed successfully")
            print("\n\n")
        elif choice==8:
            obj.statement()
        elif choice==9:
            return
        else:
            print("Invalid choice. Please try again.")
            print("\n\n")
            return    

                

if __name__=="__main__":
   user_menu()