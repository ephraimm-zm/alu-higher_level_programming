-- Script to list all cities of California sorted in ASC by cities id
SELECT id, name
FROM cities
WHERE state_id = (
	SELECT id
	FROM states
	WHERE name = 'California'
)
ORDER BY id ASC;
