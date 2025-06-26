-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Create cities table with foreign key constraint
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    -- Unique auto-generated primary key
    id INT AUTO_INCREMENT PRIMARY KEY,
    -- Foreign key referencing states(id)
    state_id INT NOT NULL,
    -- City name (cannot be null)
    name VARCHAR(256) NOT NULL,
    -- Foreign key constraint
    FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
