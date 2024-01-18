-- script that lists ALL shows FROM hbtn_0d_tvshows_rate by their rating.
SELECT s.title, SUM(r.rate) AS `rating`
FROM tv_shows AS s
JOIN tv_show_ratings AS r
ON s.id = r.show_id
ORDER BY `rating` DESC