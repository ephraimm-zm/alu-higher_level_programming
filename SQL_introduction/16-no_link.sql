-- Select all rows from table where name is not empty
SELECT score, name
FROM second_table
WHERE name <> ''
ORDER BY score DESC;
