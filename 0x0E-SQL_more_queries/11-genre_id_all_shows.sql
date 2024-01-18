-- lists ALL shows contained in the DATABASE hbtn_0d_tvshows
SELECT t1.title, t2.show_id
FROM tv_shows AS t1
LEFT OUTER JOIN tv_show_genres AS t2
ON t1.id = t2.genre_id
ORDER BY t1.title, t2.genre_id
