-- Crée l'utilisateur user_0d_1 s'il n'existe pas déjà
-- et définit son mot de passe à user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Accorde tous les privilèges à user_0d_1 sur tous les objets de la base de données
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Applique immédiatement les nouveaux privilèges
FLUSH PRIVILEGES;
