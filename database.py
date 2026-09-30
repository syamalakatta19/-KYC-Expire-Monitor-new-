import mysql.connector
from mysql.connector import Error


def get_connection():

    try:

        connection = mysql.connector.connect(
            host="127.0.0.1",
            port=3306,
            user="root",
            password="Kattasyamala@19",
            database="kyc_monitor",
            use_pure=True
        )

        return connection

    except Error as error:

        print(
            "Database Connection Error:",
            error
        )

        return None


if __name__ == "__main__":

    print("Testing MySQL connection...")
    print("-----------------------------------")

    connection = get_connection()

    if connection is not None and connection.is_connected():

        print("MySQL Connected Successfully!")
        print("Host: 127.0.0.1")
        print("Port: 3306")
        print("Database: kyc_monitor")

        cursor = connection.cursor()

        cursor.execute(
            "SELECT DATABASE()"
        )

        database_name = cursor.fetchone()[0]

        print(
            "Connected Database:",
            database_name
        )

        cursor.execute(
            "SELECT COUNT(*) FROM customers"
        )

        customer_count = cursor.fetchone()[0]

        print(
            "Total Customers:",
            customer_count
        )

        cursor.close()
        connection.close()

        print("-----------------------------------")
        print("Connection test successful!")

    else:

        print("-----------------------------------")
        print("Connection failed!")
        print("Check MySQL Server and password.")