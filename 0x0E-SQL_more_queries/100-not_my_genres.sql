-- script that uses the hbtn_0d_tvshows DATABASE TO list ALL genres NOT linked TO the SHOW Dexter
SELECT g.name
FROM tv_genres AS g
JOIN tv_show_genres AS sg
ON g.id = sg.genre_id
JOIN tv_shows AS s
ON s.id = sg.show_id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC
