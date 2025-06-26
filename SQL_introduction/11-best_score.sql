-- Sélectionne les colonnes 'score' et 'name' de la table second_table
-- où le score est supérieur ou égal à 10
SELECT score, name
FROM second_table
WHERE score >= 10
-- Trie les résultats par score en ordre décroissant
ORDER BY score DESC;
