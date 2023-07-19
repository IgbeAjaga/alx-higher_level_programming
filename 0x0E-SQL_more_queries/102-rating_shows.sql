-- List all shows from hbtn_0d_tvshows_rate by their rating

-- Use the hbtn_0d_tvshows_rate database
-- Query to list all shows and their rating sum
SELECT tv_shows.title, SUM(rating) AS rating_sum FROM tv_shows
WHERE tv_shows.id NOT IN (
      SELECT tv_shows.id FROM tv_shows
      JOIN tv_show_ratings ON tv_shows.id=tv_show_ratings.tv_show_id
      JOIN tv_show_ratings ON tv_genres.id=tv_show_ratings.tv_genre_id
       )
GROUP BY tv_shows.title
ORDER BY rating_sum DESC;
