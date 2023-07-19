-- List all shows with genre_id as NULL for shows without a genre
-- Use the hbtn_0d_tvshows database
-- List all shows with genre_id as NULL for shows without a genre
SELECT s.`title`, g.`genre_id` FROM `tv_shows` AS s
LEFT JOIN `tv_show_genres` AS g ON s.`id` = g.`show_id`
ORDER BY s.`title`, g.`genre_id`;
