-- lists ALL cities contained in the DATABASE hbtn_0d_usa.
SELECT cities.id, cities.name, states.name
FROM cities AS c
INNER JOIN states AS s
ON c.state_id = s.id
ORDER BY c.id ASC;
