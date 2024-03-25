-- Script to list cities with their corresponding state names, in asc order
SELECT cities.id, cities.name, states.name AS name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
