from banking.db_setup import get_connection


def deposit_money(account_number, amount):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            SELECT balance
            FROM accounts
            WHERE account_number = %s
            """,
            (account_number,)
        )

        result = cursor.fetchone()

        if result is None:
            print("Account not found")
            return

        if amount <= 0:
            print("Amount must be greater than 0")
            return

        current_balance = float(result[0])
        new_balance = current_balance + amount

        cursor.execute(
            """
            UPDATE accounts
            SET balance = %s
            WHERE account_number = %s
            """,
            (new_balance, account_number)
        )

        cursor.execute(
            """
            INSERT INTO transactions
            (account_number, transaction_type, amount)
            VALUES (%s, %s, %s)
            """,
            (account_number, "DEPOSIT", amount)
        )

        connection.commit()

        print("Amount deposited successfully")
        print("Deposited Amount:", amount)
        print("New Balance:", new_balance)

    except Exception as e:

        connection.rollback()
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()