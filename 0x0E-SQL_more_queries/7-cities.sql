-- creates the DATABASE hbtn_0d_usa AND the TABLE cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- CREATE TABLE
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id)
		REFERENCES states(id);
);
