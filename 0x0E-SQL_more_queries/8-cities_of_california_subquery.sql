-- List all cities of California without using JOIN

-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Query to get the state_id of California from the states table using a subquery
-- Query to get all the cities of California from the cities table using the state_id obtained from the subquery

SELECT id, name FROM cities
WHERE state_id = (
      SELECT id FROM states
      WHERE name = "California")
ORDER BY id ASC;
