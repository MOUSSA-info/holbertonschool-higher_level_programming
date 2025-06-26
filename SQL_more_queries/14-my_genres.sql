-- Sélectionne le nom du genre
SELECT tv_genres.name
-- Part de la table des genres
FROM tv_genres
-- Jointure avec la table de liaison (tv_show_genres)
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
-- Jointure avec la table des émissions (tv_shows)
INNER JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
-- Filtre pour ne garder que l'émission "Dexter"
WHERE tv_shows.title = 'Dexter'
-- Trie les résultats par nom de genre (alphabétique)
ORDER BY tv_genres.name ASC;
