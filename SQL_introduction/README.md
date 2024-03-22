## Learning Objectives
- What is a database
- What's a relational database
- What does SQL stand for
- What's MySQL
- How to create a database in MySQL
- What does *DDL* and *DML* stand for
- How to *CREATE* or *ALTER* a table
- How to *SELECT* data from a table
- How to *INSERT*, *UPDATE*, or *DELETE* data
- What are subqueries
- How to use MySQL functions

## Requrements
- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

## Description Of Tasks
- [0-list_databases.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/0-list_databases.sql) - Script to list all databases of MySQL server
- [1-create_database_if_missing.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/1-create_database_if_missing.sql) - Script to create database in MySQL server
- [2-remove_database.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/2-remove_database.sql) - Script to delete a database in MySQL server
- [3-list_tables.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/3-list_tables.sql) - Script to list all tables of a database
- [4-first_table.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/4-first_table.sql) - Script to create a table in the current database
- [5-full_table.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/5-full_table.sql) - Script that prints full description of a table from the current database
- [6-list_values.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/6-list_values.sql) - Script to list all rows of a table from a specific database
- [7-insert_value.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/7-insert_value.sql) - Script to insert a new row with id and name in a specific table in a database
- [8-count_89.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/8-count_89.sql) - Script to display the number of records with a specific id
- [9-full_creation.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/9-full_creation.sql) - Script that creates a table in the current database and adds multiple rows with the values id, name and score
- [10-top_score.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/10-top_score.sql) - Script to display the score and name of all records in a table in descending order
- [11-best_score.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/11-best_score.sql) - Script that lists all records with a score greater than or equal to 10, in desceinding order
- [12-no_cheating.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/12-no_cheating.sql) - Script that updates the score of Bob to 10 in a table
- [13-change_class.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/13-change_class.sql) - Script that removes all records with a score less than or equal to 5 from a table in a database
- [14-average.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/14-average.sql) - Script to compute the average score of all the records in the table
- [15-groups.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/15-groups.sql) - Script to count the number of records with the same score in a specific tabl
- [16-no_link.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/16-no_link.sql) - Script to list all records of a specific table
- [100-move_to_utf8.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/100-move_to_utf8.sql) - Script to convert a database in the MySQL server to UTF8
- [101-avg_temperatures.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/101-avg_temperatures.sql) - Script that displays the avg temp in Fahrenheit by city ordered in descending order by temperature
- [102-top_city.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/102-top_city.sql) - Script to display the top 3 cities with the highest temperature through the month of July to August
- [103-max_state.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_introduction/103-max_state.sql) - Script to display the max temperature of each state ordered by state name
