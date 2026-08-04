'''A bank wants to manage customer accounts. Create a BankAccount class with a
constructor to initialize account number and balance. Implement methods to deposit,
withdraw, and display balance.'''

class BankAccount :
    def __init__(self, account_number, balance):
        self.account_number = account_number 
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("deposited : ",amount)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("withdrawn : ", amount)
        else:
            print("insufficient : ", amount)
    def display_balance(self):
        print("account_number : ", self.account_number)
        print("balance : ", self.balance)
account = BankAccount(1678, 3005)
account.deposit(2679)
account.withdraw(4561)
account.display_balance()
