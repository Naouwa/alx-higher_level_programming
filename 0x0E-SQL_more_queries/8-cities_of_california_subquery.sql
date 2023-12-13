-- This script lists all the cities of California that are in database hbtn_0d_usa
-- states table contains one record (name=California)
-- result must be ascendent by cities.id
SELECT cities.id, name FROM cities WHERE state_id =
(SELECT id FROM states WHERE name = 'California') ORDER BY cities.id ASC;
