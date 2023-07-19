-- List all shows without a genre linked

-- Use the hbtn_0d_tvshows database
-- List all shows without a genre linked
SELECT s.`title`, g.`genre_id` FROM `tv_shows` AS s
LEFT JOIN `tv_show_genres` AS g ON s.`id` = g.`show_id`
WHERE g.`genre_id` IS NULL
ORDER BY s.`title`, g.`genre_id`;
