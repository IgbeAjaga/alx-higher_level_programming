-- Task 19: List all shows from hbtn_0d_tvshows_rate by their rating

-- Use the hbtn_0d_tvshows_rate database
-- Query to list all shows and their rating sum
SELECT title, SUM(rating) AS rating_sum
FROM tvshows_rate
LEFT JOIN tv_show_rating_sum ON id = tv_show_rating_sum.show_id
LEFT JOIN tv_rating_sum ON tv_show_rating_sum.rating_sum_id = tv_rating_sum.id
GROUP BY title
ORDER BY rating_sum DESC;
