-- lists ALL genres IN the DATABASE hbtn_0d_tvshows_rate by their rating
SELECT g.name, SUM(r.rate) AS `rating`
FROM tv_genres AS g
JOIN tv_show_genres AS sg
ON g.id = sg.genre_id
JOIN tv_shows AS s
ON s.id = sg.show_id
JOIN tv_show_ratings AS r
ON s.id = r.show_id
GROUP BY g.name
ORDER BY `rating` DESC;
