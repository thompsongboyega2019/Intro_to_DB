import mysql.connector

def create_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='@Lokoja123$'  
        )

        if connection.is_connected():
            cursor = connection.cursor()
            try:
                cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
                print("Database 'alx_book_store' created successfully!")
            except mysql.connector.Error as e:
                print(f"Error while creating database: {e}")
            finally:
                cursor.close()
                connection.close()
                print("MySQL connection closed.")

    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL Server: {e}")

if __name__ == "__main__":
    create_database()
