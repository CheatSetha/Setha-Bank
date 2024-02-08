class Account:
    def __init__(self, acc_num, acc_name, acc_type, balance=0.0):
        self.acc_num = acc_num
        self.acc_name = acc_name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Amount {amount} deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Amount {amount} withdrawn successfully")
        else:
            print("Insufficient balance or invalid amount to withdraw")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.acc_num}, \nAccount Name: {self.acc_name}, \nAccount Type: {self.acc_type}, \nBalance: {self.balance}"
