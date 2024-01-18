-- script that uses the hbtn_0d_tvshows DATABASE TO lists ALL genres of the SHOW Dexter
SELECT g.name FROM
tv_genres AS g
JOIN tv_show_genres AS sg
ON g.id = sg.genre_id
WHERE (SELECT title FROM tv_shows
	WHERE name = 'Dexter'
)
ORDER BY g.name ASC
