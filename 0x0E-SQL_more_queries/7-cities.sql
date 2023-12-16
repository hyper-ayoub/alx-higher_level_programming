-- Create the database hbtn_0d_usa if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database.
USE hbtn_0d_usa;

-- Create the cities table.
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);

