-- Sélectionne les colonnes score et name de la table second_table
SELECT score, name
FROM second_table
-- N'affiche que les lignes où le champ name n'est pas NULL
WHERE name IS NOT NULL
-- Trie les résultats par score (décroissant)
ORDER BY score DESC;
