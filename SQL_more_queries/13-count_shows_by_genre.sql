-- Script to list all genres and display number of shows linked
SELECT tv_show_genres.genre_id AS 'TV show genre', COUNT(tv_shows.id) AS 'count(show genre)'
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
GROUP BY tv_show_genres.genre_id
ORDER BY COUNT(tv_shows.id) DESC;
