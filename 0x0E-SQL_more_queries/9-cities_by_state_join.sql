-- List all cities with their respective states using JOIN

-- Use the hbtn_0d_usa database
-- Query to list all cities with their respective states using JOIN
SELECT cities.id, cities.name, states.name FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
