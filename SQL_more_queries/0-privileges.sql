-- Affiche les privilèges de l'utilisateur user_0d_1 sur localhost
-- Si l'utilisateur existe, la commande retourne ses droits
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Affiche les privilèges de l'utilisateur user_0d_2 sur localhost
-- Si l'utilisateur n'existe pas, une erreur sera générée
SHOW GRANTS FOR 'user_0d_2'@'localhost';
