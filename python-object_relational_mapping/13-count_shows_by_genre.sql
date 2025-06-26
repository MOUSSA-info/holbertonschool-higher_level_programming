-- Compte le nombre d'émissions par genre
SELECT 
    tv_genres.name AS genre,              -- Colonne 1 : nom du genre (alias 'genre')
    COUNT(tv_show_genres.show_id) AS number_of_shows  -- Colonne 2 : nombre d'émissions (alias 'number_of_shows')
FROM tv_genres
-- Jointure avec la table de liaison pour trouver les émissions associées
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Regroupement par nom de genre
GROUP BY tv_genres.name
-- Trie du genre le plus représenté au moins représenté
ORDER BY number_of_shows DESC;
