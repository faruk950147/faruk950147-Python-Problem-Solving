class Account:
    def __init__(self, owner, pin, balance=0):
        self.owner = owner
        self.pin = pin
        self.balance = balance

    def verify_pin(self, input_pin):
        return self.pin == input_pin

    def change_pin(self, old_pin, new_pin):
        if self.verify_pin(old_pin):
            self.pin = new_pin
            print("PIN changed successfully.")
        else:
            print("Incorrect old PIN.")

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
        input_pin = input("Enter your PIN: ")
        if not self.account.verify_pin(input_pin):
            print("Invalid PIN.")
            return

        while True:
            print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Change PIN\n5. Exit")
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
                old_pin = input("Enter old PIN: ")
                new_pin = input("Enter new PIN: ")
                self.account.change_pin(old_pin, new_pin)
            elif choice == '5':
                print("Thank you for using ATM!")
                break
            else:
                print("Invalid option.")


my_account = Account("Rahim", "1234", 1000)
atm = ATM(my_account)
atm.run()
