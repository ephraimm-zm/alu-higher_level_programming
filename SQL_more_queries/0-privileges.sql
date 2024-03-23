-- Script to list all privelleges of the states users
-- Grants for user_0d_1@localhost
SELECT CONCAT('Grants for user_0d_1@localhost\n', SHOW GRANTS FOR 'user_0d_1'@'localhost') AS user_0d_1_grants;

-- Grants for user_0d_2@localhost
SELECT CONCAT('Grants for user_0d_2@localhost\n', SHOW GRANTS FOR 'user_0d_2'@'localhost') AS user_0d_2_grants;
