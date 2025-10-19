"""
MySQL Server Script for ALX Book Store Database
Creates the alxbookstore database if it doesn't exist
"""

import mysql.connector
from mysql.connector import Error

def create_database():
    """Create the alxbookstore database if it doesn't exist"""
    connection = None
    try:
        # Connect to MySQL server without specifying a database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        
        if connection.is_connected():
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            create_db_query = "CREATE DATABASE IF NOT EXISTS alxbookstore"
            cursor.execute(create_db_query)
            
            print("Database 'alxbookstore' created successfully!")
            
    except mysql.connector.Error as e:
        print(f"Error: Failed to connect to the database - {e}")
    finally:
        # Close connection properly
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()