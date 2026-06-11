class Account:

    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print(f"Balance: ₹{self.balance}")


class SavingsAccount(Account):

    def withdraw(self, amount):
        if self.balance - amount >= 500:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")
        else:
            print("Minimum balance of ₹500 required")


account = SavingsAccount("Sneha", 2000)

account.display_balance()
account.deposit(1000)
account.withdraw(2200)
account.display_balance()
