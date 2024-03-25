-- Creates new user if not exists and give priveleges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' 
IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

REVOKE ALL PRIVILEGES ON *.* FROM 'user_0d_1'@'localhost';
