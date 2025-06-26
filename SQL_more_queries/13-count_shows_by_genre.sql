-- Sélectionne le nom du genre et compte le nombre d'émissions associées
SELECT 
    tv_genres.name AS genre, 
    COUNT(tv_show_genres.show_id) AS number_of_shows
-- Table de base : les genres
FROM tv_genres
-- Jointure avec la table de liaison pour récupérer les émissions associées
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Groupe les résultats par genre
GROUP BY tv_genres.name
-- Trie par nombre d'émissions décroissant
ORDER BY number_of_shows DESC;
