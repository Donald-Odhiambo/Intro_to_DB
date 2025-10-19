-- Script that displays the full description of the table books
-- from the database alx_book_store without using DESCRIBE or EXPLAIN
-- All SQL keywords are in uppercase as required

SELECT COLUMN_NAME,
       COLUMN_TYPE,
       IS_NULLABLE,
       COLUMN_DEFAULT,
       COLUMN_KEY,
       EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store'
  AND TABLE_NAME = 'books';
