-- List all genres of the show Dexter

-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- Query to list all genres of the show Dexter
SELECT tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;