def get_account_number():

    while True:

        try:
            account_number = int(input("Enter account number: "))

            if account_number <= 0:
                print("Account number must be positive")
                continue

            return account_number

        except ValueError:
            print("Please enter a valid account number")


def get_amount(message):

    while True:

        try:
            amount = float(input(message))

            if amount <= 0:
                print("Amount must be greater than 0")
                continue

            return amount

        except ValueError:
            print("Please enter a valid amount")