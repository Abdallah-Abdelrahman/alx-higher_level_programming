-- creates the DATABASE hbtn_0d_2 AND the USER user_0d_2.

CREATE DATABASE IF NOT EXISTS hbtn_0d_2; -- CREATE db

-- CREATE USER
CREATE USER user_0d_2@localhost
IDENTIFIED by user_0d_2_pwd;

-- assign privileges
GRANT SELECT
ON hbtn_0d_2
TO user_0d_2@localhost;
