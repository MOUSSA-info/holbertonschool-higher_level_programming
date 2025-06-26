-- Sélectionne les colonnes id et name de la table cities
SELECT id, name
FROM hbtn_0d_usa.cities
-- Où le state_id correspond à l'id de l'état 'California'
WHERE state_id = (
    -- Sous-requête : récupère l'id de l'état dont le nom est 'California'
    SELECT id
    FROM hbtn_0d_usa.states
    WHERE name = 'California'
)
-- Trie les résultats par id croissant
ORDER BY id ASC;
