-- This script  creates the table unique_id on your MySQL server
-- unique_id: id INT with default 1, and must be unique
CREATE TABLE IF NOT EXISTS unique_id (
	id INT UNIQUE DEFAULT 1,
	name VARCHAR(256)
);
