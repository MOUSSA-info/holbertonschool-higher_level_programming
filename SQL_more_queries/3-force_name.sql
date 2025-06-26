-- Crée la table force_name si elle n'existe pas déjà
CREATE TABLE IF NOT EXISTS force_name (
    -- Colonne id de type INT
    id INT,
    -- Colonne name de type VARCHAR(256), non nulle
    name VARCHAR(256) NOT NULL
);
