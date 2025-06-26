-- Crée la table unique_id si elle n'existe pas déjà
CREATE TABLE IF NOT EXISTS unique_id (
    -- Colonne id de type INT, avec valeur par défaut 1 et contrainte UNIQUE
    id INT DEFAULT 1 UNIQUE,
    -- Colonne name de type VARCHAR(256)
    name VARCHAR(256)
);
