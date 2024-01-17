-- Delete duplicate rows from the states table
DELETE s1
FROM states s1
JOIN states s2 ON s1.name = s2.name AND s1.id > s2.id;
