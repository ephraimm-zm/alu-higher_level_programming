-- Script to display avg temp by city ordered by temp in desc
SELECT city, AVG(value) AS avg_temp
FROM temperatures
ORDER BY avg_temp DESC;
