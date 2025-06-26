-- Liste toutes les émissions et leurs genres associés
SELECT 
    tv_shows.title, 
    tv_genres.name
-- Table de base : toutes les émissions
FROM tv_shows
-- Jointure à gauche avec la table de liaison (pour inclure même sans genre)
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Jointure à gauche avec la table des genres (pour récupérer le nom)
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- Trie par titre (ascendant) puis par nom de genre (ascendant)
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
