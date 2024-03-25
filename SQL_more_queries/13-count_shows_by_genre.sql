-- Script to list all genres and display number of shows linked
SELECT genre AS genre, COUNT(tv_shows.title) AS number_of_shows
FROM genres
JOIN tv_shows_genres ON genres.id = tv_shows_genres.genre_id
JOIN tv_shows ON tv_shows_genres.tv_show_id = tv_shows.id
GROUP BY genre
ORDER BY number_of_shows DESC;
