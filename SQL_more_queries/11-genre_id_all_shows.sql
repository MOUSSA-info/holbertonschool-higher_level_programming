-- Sélectionne le titre des émissions et l'id du genre associé (ou NULL)
SELECT tv_shows.title, tv_show_genres.genre_id
-- Table principale : toutes les émissions
FROM tv_shows
-- Jointure à gauche pour inclure même les émissions sans genre
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Trie par titre (ascendant) puis par genre_id (ascendant)
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
