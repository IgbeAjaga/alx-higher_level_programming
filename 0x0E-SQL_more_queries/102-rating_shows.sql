-- Rotten tomatoes

-- Use the hbtn_0d_tvshows_rate database
-- Query to list all shows and their rating sum
SELECT `title`, SUM(`rate`) AS `rating_sum`
FROM tv_shows AS tv
INNER JOIN `tv_show_ratings` AS rt ON tv.`id` = rt.`show_id`
GROUP BY `title`
ORDER BY `rating_sum` DESC;
