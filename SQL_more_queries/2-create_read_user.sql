-- Crée la base de données hbtn_0d_2 si elle n'existe pas déjà
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Crée l'utilisateur user_0d_2 s'il n'existe pas déjà
-- et définit son mot de passe à user_0d_2_pwd
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Accorde uniquement le privilège SELECT sur la base hbtn_0d_2 à user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Applique immédiatement les changements de privilèges
FLUSH PRIVILEGES;
