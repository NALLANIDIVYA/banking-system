from banking.db_setup import get_connection


def check_balance(account_number):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = """
        SELECT name, balance
        FROM accounts
        WHERE account_number = %s
        """

        cursor.execute(query, (account_number,))
        result = cursor.fetchone()

        if result:
            print("Account Holder:", result[0])
            print("Current Balance:", result[1])
        else:
            print("Account not found")

    except Exception as e:
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()


