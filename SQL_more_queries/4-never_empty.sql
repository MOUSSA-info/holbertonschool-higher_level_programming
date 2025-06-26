-- Crée la table id_not_null si elle n'existe pas déjà
CREATE TABLE IF NOT EXISTS id_not_null (
    -- Colonne id de type INT, avec une valeur par défaut 1
    id INT DEFAULT 1,
    -- Colonne name de type VARCHAR(256)
    name VARCHAR(256)
);
