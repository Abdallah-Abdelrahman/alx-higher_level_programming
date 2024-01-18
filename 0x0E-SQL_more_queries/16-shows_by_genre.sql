-- script that lists ALL shows, AND ALL genres linked TO that SHOW, FROM the DATABASE hbtn_0d_tvshows
SELECT s.title, g.name
FROM tv_shows AS s
outer JOIN tv_show_genres AS sg
ON s.id = sg.show_id
outer JOIN tv_genres AS g
g.id = sg.genre_id
ORDER BY s.title, g.name ASC
