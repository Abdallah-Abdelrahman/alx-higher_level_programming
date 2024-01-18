-- creates the DATABASE hbtn_0d_usa AND the TABLE cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- CREATE TABLE
CREATE TABLE hbtn_0d_usa.cities (
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	state_id INT NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (state_id)
		REFERENCES hbtn_0d_usa.states(hbtn_0d_usa.states.id);
);
