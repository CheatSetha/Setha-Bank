from SethaBank import SethaBank


def main():
    bank = SethaBank('Setha Bank')
    account_number = 0

    def press_enter():
        input("Press Enter to continue...")

    while True:
        print('\n Welcome to ', bank.name)
        print('1. Create Account')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Check Balance')
        print('5. View Bank Information')
        print('6. View Transaction History')
        print('7. Close Account')
        print('0. Exit')

        choice = input("Please your option: ")
        if choice == '1':
            account_name = input("Enter your Account Name: ")

            print('\n Select Account type:')
            print("1. Saving")
            print("2. Checking")
            print("3. Investment")
            account_type = input("Select your choice: ")
            if account_type == '1':
                account_type = 'Saving'
            elif account_type == '2':
                account_type = 'Checking'
            elif account_type == '3':
                account_type = 'Investment'
            else:
                print(f"Invalid choice. Defaulting to Saving.")

            balance = input("Enter your balance: ")
            account_number = bank.create_account(account_name, account_type, float(balance))
            press_enter()

        elif choice == '2':
            amount = input("Enter the amount: ")
            bank.deposit(account_number, float(amount))
            press_enter()
        elif choice == '3':
            amount = input("Enter the amount: ")
            bank.withdraw(account_number, float(amount))
            press_enter()
        elif choice == '4':
            current_balance = bank.get_balance(account_number)
            print(f"Your current balance is {current_balance}")
            press_enter()
        elif choice == '5':
            print("===============| User's Information |==============")
            print(bank.get_info(account_number))
            press_enter()

        elif choice == '6':
            print("===============| Transaction History |==============")
            history = bank.get_transaction_history(account_number)
            if len(history) == 0:
                print("No transaction history found")
            elif len(history) > 0:
                for transaction in history:
                    print(transaction)
            press_enter()
        elif choice == '7':
            opt = input("Are you sure you want to close your account? (y/n): ")
            if opt == 'y':
                bank.close_account(account_number)
                print("Account closed successfully")
                account_number = 0
                press_enter()
            else:
                print("Account not closed")
                press_enter()
        elif choice == '0':
            return
        else:
            print("invalid option")


if __name__ == '__main__':
    main()
