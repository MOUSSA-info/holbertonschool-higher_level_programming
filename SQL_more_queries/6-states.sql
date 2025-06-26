-- Crée la base de données hbtn_0d_usa si elle n'existe pas déjà
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Utilise la base de données hbtn_0d_usa
USE hbtn_0d_usa;

-- Crée la table states si elle n'existe pas déjà
CREATE TABLE IF NOT EXISTS states (
    -- Colonne id : 
    --   - INT (entier)
    --   - PRIMARY KEY (clé primaire, implique NOT NULL et UNIQUE)
    --   - AUTO_INCREMENT (génération automatique)
    id INT AUTO_INCREMENT PRIMARY KEY,
    -- Colonne name : 
    --   - VARCHAR(256) (texte max 256 caractères)
    --   - NOT NULL (valeur obligatoire)
    name VARCHAR(256) NOT NULL
);
