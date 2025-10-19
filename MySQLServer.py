# MySQL Server Script for ALX Book Store Database
import mysql.connector

def create_database():
    """
    Creates the alx_book_store database in MySQL server
    """
    connection = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=''
        )
        
        # Create cursor for database operations
        cursor = connection.cursor()
        
        # Execute database creation command
        # Using CREATE DATABASE IF NOT EXISTS to avoid SELECT/SHOW
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        
        # Print success message
        print("Database 'alx_book_store' created successfully!")
            
    # Handle connection errors
    except mysql.connector.Error as e:
        print(f"Error: Failed to connect to the database - {e}")
        
    # Clean up resources
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Execute the function
if __name__ == "__main__":
    create_database()