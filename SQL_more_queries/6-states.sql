-- Script to create database and table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
	id INT NOT NULL UNIQUE,
	name VARCHAR(256)
	);
