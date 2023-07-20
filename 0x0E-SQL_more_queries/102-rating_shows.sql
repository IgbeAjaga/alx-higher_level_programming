-- Rotten tomatoes

-- Use the hbtn_0d_tvshows_rate database
USE hbtn_0d_tvshows_rate;

-- Query to list all shows and their rating sum
SELECT tv_shows.title, SUM(rating) AS rating_sum
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.tv_show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;

