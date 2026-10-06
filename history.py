from banking.db_setup import get_connection


def show_history(account_number):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = """
        SELECT transaction_id,
               transaction_type,
               amount,
               transaction_date
        FROM transactions
        WHERE account_number = %s
        ORDER BY transaction_id DESC
        """

        cursor.execute(query, (account_number,))
        results = cursor.fetchall()

        if not results:
            print("No transactions found")
            return

        print("\n========== TRANSACTION HISTORY ==========")

        for row in results:
            print("Transaction ID:", row[0])
            print("Type:", row[1])
            print("Amount:", row[2])
            print("Date:", row[3])
            print("----------------------------------------")

    except Exception as e:
        print("Error:", e)

    finally:
        cursor.close()
        connection.close()