-- List all genres in the hbtn_0d_tvshows_rate database by their rating

-- Use the hbtn_0d_tvshows_rate database
USE hbtn_0d_tvshows_rate;

-- Query to list all genres and their rating sum
SELECT tv_genres.name, SUM(rating) AS rating_sum
FROM tv_genres
LEFT JOIN tv_show_genres ON id = tv_show_genres.genre_id
LEFT JOIN tv_show_ratings ON tv_show_genres.tv_show_id = tv_show_ratings.tv_show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
