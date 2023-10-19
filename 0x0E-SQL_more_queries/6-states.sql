-- This script creates database hbtn_0d_usa & table states on MY MySQL server.
-- state: id INT UNIQUE, auto generated, cant't be NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (id INT UNIQUE NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY(id)
);
