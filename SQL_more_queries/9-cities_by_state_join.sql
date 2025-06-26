-- Sélectionne les colonnes cities.id, cities.name, states.name
SELECT cities.id, cities.name, states.name
FROM hbtn_0d_usa.cities
-- Jointure sur l'id de l'état (state_id = states.id)
JOIN hbtn_0d_usa.states ON cities.state_id = states.id
-- Trie les résultats par cities.id croissant
ORDER BY cities.id ASC;
