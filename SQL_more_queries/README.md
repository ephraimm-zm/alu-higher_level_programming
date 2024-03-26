## Learning Objectives
- How to create a new MySQL user
- How to manage privileges for a user to a database or table
- What's a *PRIMARY KEY*
- What's a *FOREIGN KEY*
- How to use *NOT NULL* and *UNIQUE* constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are *JOIN* and *UNION*

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
- All your files should end with a new line
- All your SQL queries should have a comment just before (i.e. syntax above)
- All your files should start by a comment describing the task
- All SQL keywords should be in uppercase (SELECT, WHERE…)
- A README.md file, at the root of the folder of the project, is mandatory
- The length of your files will be tested using wc

## Description of tasks
- [0-privileges.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_more_queries/0-privileges.sql) - List all privileges of different MySQL users
- [1-create_user.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_more_queries/1-create_user.sql) - Script to create a user in MySQL
- [2-create_read_user.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_more_queries/2-create_read_user.sql) - Script that creates a database and a user
- [3-force_name.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_more_queries/3-force_name.sql) - Script to creates a table with the given description
- [4-never_empty.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_more_queries/4-never_empty.sql) - Script that creates a table with the given description with the id having a defult value of 1
- [5-unique_id.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_more_queries/5-unique_id.sql) - Script to create a table whose id in the description must be unique
- [6-states.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_more_queries/6-states.sql) - Script to create a database and a table whose id must be a unique, auto-generated primary key
- [7-cities.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_more_queries/7-cities.sql) - Script to create a database and a table. The table must have a unique auto-generated primary key and a Foreign Key that references to the id of the states table
- [8-cities_of_california_subquery.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_more_queries/8-cities_of_california_subquery.sql) - A script to list all cities of California found in the database hbtn_0d_usa
- [9-cities_by_state_join.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_more_queries/9-cities_by_state_join.sql) - A script to list all cities in the database hbtn_0d_usa
- [10-genre_id_by_show.sql](https://github.com/ephraimm-zm/alu-higher_level_programming/blob/main/SQL_more_queries/10-genre_id_by_show.sql) - Script to list all shows in the database hbtn_0d_tvshows that have at least one genre linked
