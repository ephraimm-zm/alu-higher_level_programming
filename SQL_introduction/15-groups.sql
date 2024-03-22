-- Lists number of records with the same score
SELECT COUNT(score) AS score_cont
FROM second_table
WHERE score > 1
GROUP BY score
ORDER BY score_count DESC;
