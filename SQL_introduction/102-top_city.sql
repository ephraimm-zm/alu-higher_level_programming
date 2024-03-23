-- Sccript to display top 3 cities by temp in Jul and Aug
SELECT city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
