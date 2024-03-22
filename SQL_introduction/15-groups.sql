-- Lists number of records with the same score
SELECT score, COUNT(score) AS score_count
FROM second_table
GROUP BY score
ORDER BY score_count DESC;
