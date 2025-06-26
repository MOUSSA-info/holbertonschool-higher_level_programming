-- Sélectionne le titre des émissions et l'id du genre associé (NULL)
SELECT tv_shows.title, tv_show_genres.genre_id
-- Table principale : toutes les émissions
FROM tv_shows
-- Jointure à gauche pour inclure même les émissions sans genre
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Filtre pour garder uniquement les émissions sans genre (genre_id IS NULL)
WHERE tv_show_genres.genre_id IS NULL
-- Trie par titre (ascendant)
ORDER BY tv_shows.title ASC;
