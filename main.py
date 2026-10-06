from banking.account import create_account
from banking.balance import check_balance
from banking.deposit import deposit_money
from banking.withdraw import withdraw_money
from banking.history import show_history
from banking.display import display_menu
from banking.validators import get_account_number, get_amount


while True:

    display_menu()

    choice = input("Enter your choice: ")

    # 1. Create Account
    if choice == "1":

        account_number = get_account_number()

        name = input("Enter account holder name: ")

        balance = get_amount("Enter initial balance: ")

        create_account(account_number, name, balance)

    # 2. Check Balance
    elif choice == "2":

        account_number = get_account_number()

        check_balance(account_number)

    # 3. Deposit Money
    elif choice == "3":

        account_number = get_account_number()

        amount = get_amount("Enter deposit amount: ")

        deposit_money(account_number, amount)

    # 4. Withdraw Money
    elif choice == "4":

        account_number = get_account_number()

        amount = get_amount("Enter withdrawal amount: ")

        withdraw_money(account_number, amount)

    # 5. Transaction History
    elif choice == "5":

        account_number = get_account_number()

        show_history(account_number)

    # 6. Exit
    elif choice == "6":

        print("Thank you for using Banking System")
        break

    # Invalid choice
    else:

        print("Invalid choice. Please select 1 to 6.")