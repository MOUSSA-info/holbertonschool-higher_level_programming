-- Sélectionne le titre des émissions et l'id du genre associé
SELECT tv_shows.title, tv_show_genres.genre_id
-- Table principale : tv_shows
FROM tv_shows
-- Jointure avec tv_show_genres pour récupérer les genres liés
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Trie par titre (ascendant) puis par genre_id (ascendant)
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
