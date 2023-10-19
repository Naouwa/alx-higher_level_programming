-- This script creates the table force_name on your MySQL server.
-- id=int & name=VARCHAR and can't be NULL
CREATE TABLE IF NOT EXISTS `force_name` (
	`id` INT,
	`name` VARCHAR(256) NOT NULL
);
