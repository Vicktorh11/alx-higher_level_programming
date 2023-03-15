-- creates a table called first_table in the current database in your MySQL server
-- first_table descriptiion:
--	id INT
--	name VARCHAR(256)
-- The database name will be passed as an argument of the MySQL command
-- script should not fail if the table first_table already exists

CREATE TABLE IF NOT EXISTS first_table (id INT,  name VARCHAR(256));
