-- Create a database if it doesn't existss
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the db
USE hbtn_0d_usa;

-- Create table if not exists with foreign key
CREATE TABLE IF NOT EXISTS cities (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256),
	FOREIGN KEY (state_id) REFERENCES states(id)
	);
