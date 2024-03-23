-- Convert the database to UTF8
ALTER DATABASE hbtn_0c_0 
    CHARACTER SET utf8mb4 
    COLLATE utf8mb4_unicode_ci;

-- Convert the table to UTF8
ALTER TABLE hbtn_0c_0.first_table 
    COLLATE utf8mb4_unicode_ci;

-- Modify the collation of the name field to utf8mb4_unicode_ci
ALTER TABLE hbtn_0c_0.first_table 
    MODIFY COLUMN name VARCHAR(256) 
    COLLATE utf8mb4_unicode_ci;
