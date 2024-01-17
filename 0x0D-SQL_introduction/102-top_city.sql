-- displays the top 3 of cities temperature during July and August ordered by temperature (descending)
SELECT TOP 3 city, AVG(value) AS 'avg_temp' FROM temperatures
WHERE month = 'July' OR month = 'August'
ORDER BY value DESC;
