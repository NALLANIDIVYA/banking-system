import mysql.connector
from mysql.connector import Error

from banking.config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME


def test_connection():

    connection = None

    try:
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        if connection.is_connected():
            print("Successfully connected to MySQL")

    except Error as e:
        print("Error connecting to MySQL:", e)

    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            print("Connection closed")


def get_connection():

    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    return connection