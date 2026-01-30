import mysql.connector
from mysql.connector import Error

try:
    conn1 = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="142434",
        auth_plugin="mysql_native_password"
    )

    if conn1.is_connected():
        print("Connection successful")

        cursor = conn1.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS ATHARVADB")
        conn1.commit()

        print("Database created successfully (or already exists)")

except Error as e:
    print("MySQL Error:", e)

finally:
    if "cursor" in locals():
        cursor.close()
    if "conn1" in locals() and conn1.is_connected():
        conn1.close()
        print("Connection closed")