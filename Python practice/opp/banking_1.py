class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Balance for {self.owner}: {self.balance}")


class ATM:
    def __init__(self, account):
        self.account = account

    def run(self):
        while True:
            print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
            choice = input("Choose option: ")
            if choice == '1':
                self.account.check_balance()
            elif choice == '2':
                amount = float(input("Enter deposit amount: "))
                self.account.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter withdraw amount: "))
                self.account.withdraw(amount)
            elif choice == '4':
                print("Thank you for using ATM!")
                break
            else:
                print("Invalid option.")


# creating objects
my_account = Account("Rahim", 1000)
atm = ATM(my_account)
atm.run()
