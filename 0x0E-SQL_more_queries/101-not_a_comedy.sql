-- script that lists ALL shows without the genre Comedy IN the DATABASE hbtn_0d_tvshows.
SELECT s.title
FROM tv_shows AS s
	WHERE s.id NOT IN (
		SELECT sg.show_id
		FROM tv_show_genres AS sg
		JOIN tv_genres AS g
		ON sg.genre_id = g.id
		WHERE g.name = 'Comedy'
	)
ORDER BY s.title;

