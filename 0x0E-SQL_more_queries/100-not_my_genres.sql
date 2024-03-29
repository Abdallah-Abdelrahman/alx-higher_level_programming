-- script that uses the hbtn_0d_tvshows DATABASE TO list ALL genres NOT linked TO the SHOW Dexter
SELECT g.name
FROM tv_genres AS g
WHERE g.id NOT IN (
	SELECT sg.genre_id
	FROM tv_shows AS s
	JOIN tv_show_genres AS sg
	ON s.id = sg.show_id
	WHERE s.title = 'Dexter'
)
ORDER BY g.name ASC;
