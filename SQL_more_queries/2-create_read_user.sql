-- Create a database and user with SELECT priveleges
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

CREATE USER IF NOT EXISTS 'user_0d_2' IDENTIFIED BY 'user_0d_2_pwd';

GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'
