-- Select all rows from table where name is not empty
SELECT name, score
FROM second_table
WHERE name <> ''
ORDER BY score DESC;
