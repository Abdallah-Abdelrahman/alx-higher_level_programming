-- creates the DATABASE hbtn_0d_usa AND the TABLE states (IN the DATABASE hbtn_0d_usa)
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- CREATE TABLE
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id INT UNIQUE NOT NULL AUTO_INCREMENT,
	name VARCHAR(256) NOT NULL,
	CONSTRAINT `hbtn_0d_usa.states_pk` PRIMARY KEY (id)
);
