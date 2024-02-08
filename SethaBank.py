from datetime import datetime

from Account import Account


class SethaBank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}  # dictionary to store acc key by acc num
        self.transaction_history = []

    def check_acc_num(self, acc_num):
        if acc_num in self.accounts:
            return True
        else:
            return False

    def create_account(self, acc_name, acc_type, balance=0):
        acc_num = len(self.accounts) + 1
        acc = Account(acc_num, acc_name, acc_type, balance)
        self.accounts[acc_num] = acc
        print(f"Account created successfully. Account Number: {acc_num}")
        return acc_num

    def close_account(self, acc_num):
        is_exist = self.check_acc_num(acc_num)
        if is_exist:
            del self.accounts[acc_num]
            print("Account closed successfully")

    def deposit(self, acc_num, amount):
        if acc_num in self.accounts:
            account = self.accounts[acc_num]
            account.deposit(amount)
            # add transaction history
            self.transaction_history.append({
                "acc_num": acc_num,
                "type": "deposit",
                "amount": amount,
                "balance": account.get_balance(),
                "date": datetime.now()
            })
        else:
            print("Account not found")

    def withdraw(self, acc_num, amount):
        is_exist = self.check_acc_num(acc_num)
        if is_exist:
            account = self.accounts[acc_num]
            account.withdraw(amount)
            self.transaction_history.append({
                "acc_num": acc_num,
                "type": "withdraw",
                "amount": amount,
                "balance": account.get_balance(),
                "date": datetime.now()
            })
        else:
            print("Account not found")

    def get_balance(self, acc_num):
        is_exist = self.check_acc_num(acc_num)
        if is_exist:
            return self.accounts[acc_num].get_balance()
        else:
            print("Account not found!")

    def get_transaction_history(self, acc_num):
        is_exist = self.check_acc_num(acc_num)
        if is_exist:
            return self.transaction_history
        else:
            print("Account not found!")

    def get_info(self, acc_num):
        is_exist = self.check_acc_num(acc_num)
        if is_exist:
            return self.accounts[acc_num]
        else:
            print("Account not found!")
