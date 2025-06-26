-- Sélectionne les titres des émissions comiques
SELECT tv_shows.title
FROM tv_shows
-- Jointure avec la table de liaison (tv_show_genres)
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
-- Jointure avec la table des genres (tv_genres)
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
-- Filtre pour ne garder que le genre "Comedy"
WHERE tv_genres.name = 'Comedy'
-- Trie les résultats par titre (alphabétique croissant)
ORDER BY tv_shows.title ASC;
