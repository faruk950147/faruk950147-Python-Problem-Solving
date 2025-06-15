class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. Total balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. Total balance: {self.balance}")
    
    def check_balance(self):
        print(f"Balance for {self.owner}: {self.balance}")

if __name__ == "__main__":
    account = Account("John", "123456789", 1000)
    account.check_balance()
    account.deposit(500)
    account.withdraw(200)
    account.check_balance()