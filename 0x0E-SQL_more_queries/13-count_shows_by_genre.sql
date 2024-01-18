-- lists ALL genres FROM hbtn_0d_tvshows AND displays the number of shows linked TO each
SELECT g.name AS `genre`, COUNT(sg.show_id) AS `number_of_shows`
FROM tv_genres AS g
JOIN tv_show_genres AS sg
ON g.id = sg.genre_id
GROUP BY `genre`
ORDER BY `number_of_shows` DESC
