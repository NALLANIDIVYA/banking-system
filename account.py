from banking.db_setup import get_connection


def create_account(account_number, name, balance):

    connection = get_connection()
    cursor = connection.cursor()

    try:
        query = """
        INSERT INTO accounts (account_number, name, balance)
        VALUES (%s, %s, %s)
        """

        cursor.execute(query, (account_number, name, balance))
        connection.commit()

        print("Account created successfully")

    except Exception as e:
        connection.rollback()
        print("Error creating account:", e)

    finally:
        cursor.close()
        connection.close()