-- Script to print full description of books table without using DESCRIBE or EXPLAIN
-- Uses INFORMATION_SCHEMA.COLUMNS to get table structure details

SELECT 
    COLUMN_NAME,      -- Name of the column
    DATA_TYPE,        -- Data type of the column  
    IS_NULLABLE,      -- Whether column allows NULL values
    COLUMN_DEFAULT    -- Default value of the column
FROM 
    INFORMATION_SCHEMA.COLUMNS  -- System table containing column metadata
WHERE 
    TABLE_SCHEMA = 'alx_book_store'  -- Filter by database name
    AND TABLE_NAME = 'books';        -- Filter by table name