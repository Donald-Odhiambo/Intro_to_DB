# MySQL Server Script for ALX Book Store Database
# This script creates the alxbookstore database in MySQL server
# It handles connection errors and avoids using SELECT or SHOW statements

# Import MySQL connector for database operations
import mysql.connector

# Function to create the database
def create_database():
    """
    Creates the alxbookstore database if it doesn't exist
    Uses CREATE DATABASE IF NOT EXISTS to avoid SELECT/SHOW statements
    """
    # Initialize connection variable
    connection = None
    
    # Try to establish connection and create database
    try:
        # Connect to MySQL server without specifying a database
        connection = mysql.connector.connect(
            host='localhost',  # MySQL server host
            user='root',       # MySQL username
            password=''        # MySQL password (update if needed)
        )
        
        # Check if connection was successful
        if connection.is_connected():
            # Create cursor for executing SQL commands
            cursor = connection.cursor()
            
            # Create database without using SELECT or SHOW statements
            # CREATE DATABASE IF NOT EXISTS handles existence check internally
            cursor.execute("CREATE DATABASE IF NOT EXISTS alxbookstore")
            
            # Print success message when database is created
            print("Database 'alxbookstore' created successfully!")
            
    # Handle MySQL specific errors
    except mysql.connector.Error as e:
        # Print error message for connection failures
        print(f"Error: Failed to connect to the database - {e}")
        
    # Finally block to ensure proper resource cleanup
    finally:
        # Close cursor and connection if they were opened
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Main execution block
if __name__ == "__main__":
    # Call the function to create database
    create_database()