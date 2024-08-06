import datetime
import Encrytion as e
import accountmanger as am
import key as k
from cryptography.fernet import Fernet


class Account():
    def __init__(self,account_id,name,pin):  # constructor
        self.account_id = account_id
        self.name = name
        self.pin = e.EncryptionManager(k.load_key()).encrypt(pin)
        self.balance = 0
        self.is_frozen = False
        self.transaction_history = []
        self.transaction_limit = 10000
    def get_info(self):
        return {"account_id":self.account_id,"name":self.name,"balance":self.balance,"transaction_limit":self.transaction_limit,"is_frozen":self.is_frozen,"pin":self.pin}
    def check_info(self):
        if self.is_frozen:
            return False
        print("Account ID:",self.account_id)
        print("Name:",self.name)
        return 
    def deposit(self,amount):  # method
        if self.is_frozen:
            return False
        if amount > self.transaction_limit:
            return False
        self.balance += amount
        current_time= datetime.datetime.now()
        formatted_ct = current_time.strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_history.append(('deposit',amount,formatted_ct))
        return True   
     
    def check_amount(self):
        if self.is_frozen:
            print("Account is frozen")
            return 
        print("Your balance is:",self.balance)
        return True
    def withdraw(self,amount):
        if self.is_frozen:
            return False
        if amount > self.balance:
            return False
        self.balance -= amount
        ct = datetime.datetime.now()
        ft = ct.strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_history.append(("Withdraw",amount,ft))

    def transfer(self,amount,target_account):
        if self.is_frozen:
            print("Account is frozen")
            return 
        if amount > self.balance:
            print("Insufficient balance")
            return 
        if amount > self.transaction_limit:
            print("Transaction limit exceeded")
            return 
        self.withdraw(amount)
        target_account.deposit(amount)
        ct = datetime.datetime.now()
        ft = ct.strftime("%Y-%m-%d %H:%M:%S")
        self.transaction_history.append(('Transfer',amount,ft))
        return True
    def change_pin(self,new_pin):
        if self.is_frozen:
            print("Account is frozen")
            return 
        self.pin = e.EncryptionManager(k.load_key()).encrypt(new_pin)
    def statement(self):
        for transaction in self.transaction_history:  
            print(transaction)


if __name__=="__main__":

    Account()


