# import mysql.connector

# my_db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="@Lokoja123$",
# )

# my_db_cursor = my_db.cursor()

# for (each_database,) in my_db_cursor:
#     if each_database != "alx_be_store":
#         my_db_cursor.execute(
#             """
#              CREATE DATABASE alx_be_store
#               """
#         )
#         print(f"Database 'alx_book_store' created successfully!")

# try:
#     my_db.connect(database="alx_be_store")
# except Exception:
#     print("Error in connection")
# else:
#     my_db.commit()

# my_db.close()

import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (not to a specific database)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='@Lokoja123$'  # Replace with your actual password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except Error as e:
                print(f"Error while creating database: {e}")
            finally:
                cursor.close()
                connection.close()
                print("MySQL connection closed.")

    except Error as e:
        print(f"Error connecting to MySQL Server: {e}")

if __name__ == "__main__":
    create_database()
