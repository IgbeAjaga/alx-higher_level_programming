-- Rotten tomatoes

-- Use the hbtn_0d_tvshows_rate database
USE hbtn_0d_tvshows_rate;

-- Query to list all shows and their rating sum
SELECT title, SUM(rate) AS rating_sum
FROM tv_shows
JOIN tv_show_ratings ON id = tv_show_ratings.show_id
GROUP BY title
ORDER BY rating_sum DESC;
