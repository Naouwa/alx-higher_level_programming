-- This script creates the database hbtn_0d_usa and the table cities on MYSQL
-- cities: id= INT unique, auto generated, can't be NULL
-- 	state_id= INT, cant be NULL, must be FOREIGN KEY, refrences to id in states TABLE
CREATE TABLE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT PRIMARY KEY UNIQUE NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id),
	name VARCHAR(256) NOT NULL,
);
