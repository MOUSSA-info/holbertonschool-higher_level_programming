-- Sélectionne le score et compte le nombre d'occurrences
SELECT score, COUNT(*) AS number
FROM second_table
-- Groupe les résultats par score
GROUP BY score
-- Trie par nombre d'occurrences (décroissant) puis par score (décroissant)
ORDER BY number DESC, score DESC;
