import pickle
import Account
from datetime import datetime, timedelta
class AccountManager:
    def __init__(self,storage_file ="accouts.pkl"):
        self.accounts = {}
        self.storage_file=storage_file
        self.load_account()
    def create_account(self,acount_id,name,pin):
        if acount_id in self.accounts:
            print(f"Account with {acount_id} already exists")
        account= Account.Account(acount_id,name,pin)
        self.accounts[acount_id] =account
        self.save_account()
        return True
      

    def delete_account(self, account_id):
        if account_id not in self.accounts:
            print(f"Account {account_id} does not exist.")
            return
        del self.accounts[account_id]
        self.save_account()
        print(f"Account {account_id} deleted successfully.")

    def freeze_account(self, account_id):
        if account_id not in self.accounts:
            print(f"Account {account_id} does not exist.")
            return
        obj=self.accounts[account_id]
        obj.is_frozen = True
        self.save_account()
        print(f"Account {account_id} is now frozen.")
    
    def unfreeze_account(self, account_id):
        if account_id not in self.accounts:
            print(f"Account {account_id} does not exist.")
            return
        obj=self.accounts[account_id]
        obj.is_frozen = False
        self.save_account()
        print(f"Account {account_id} is now unfrozen.")


    def set_transaction_limit(self, account_id, limit):
        if account_id not in self.accounts:
            print(f"Account {account_id} does not exist.")
            return
        obj=self.accounts[account_id]
        obj.transaction_limit = limit
        self.save_account()
        print(f"Transaction limit for account {account_id} set to {limit}.")

    def show_account_details(self, account_id):
        if account_id not in self.accounts:
            print(f"Account {account_id} does not exist.")
            return
        account = self.accounts[account_id]
        print(f"Account ID: {account.account_id}")
        print(f"Name: {account.name}")
        print(f"Balance: {account.balance}")
        print(f"Transaction Limit: {account.transaction_limit}")
        print(f"Frozen: {account.is_frozen}")

    def show_transaction_history(self, account_id=None):
        if account_id is None:
            for account in self.accounts.values():
                print(f"Account ID: {account.account_id}")
                print("Transaction History:")
                account.statement()
                print()
        else:
            if account_id not in self.accounts:
                print(f"Account {account_id} does not exist.")
                return
            account = self.accounts[account_id]
            print(f"Account ID: {account.account_id}")
            print("Transaction History:")
            account.statement()


    def generate_report(self, period='monthly'):
        if period == 'monthly':
            start_date = datetime.now() - timedelta(days=30)
        elif period == 'weekly':
            start_date = datetime.now() - timedelta(days=7)
        elif period == 'yearly':
            start_date = datetime.now() - timedelta(days=365)
        else:
            print("Invalid period.")
            return
        for account in self.accounts.values():
            print(f"Account ID: {account.account_id}")
            print("Transaction History:")
            for transaction in account.transaction_history:
                if transaction[2] > start_date:
                    print(transaction)
            print()

    def load_account(self):
        try:
            with open(self.storage_file,"rb") as f:
                self.accounts = pickle.load(f)
        except:
            pass
    def save_account(self):
        with open(self.storage_file,"wb") as f:
            pickle.dump(self.accounts,f)

if __name__=="__main__":
    AccountManager()
                
# am=AccountManager()