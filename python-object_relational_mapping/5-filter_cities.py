#!/usr/bin/python3
"""
Script pour lister les villes d'un état spécifique
Prend 4 arguments : utilisateur, mot de passe, base de données et nom d'état
Utilise des requêtes paramétrées pour éviter les injections SQL
Connecte en localhost:3306
Trie par id de ville croissant
Utilise une seule commande execute()
Affiche les résultats sous forme de chaîne séparée par des virgules
Ne s’exécute pas lors d’un import
"""

import MySQLdb
import sys

def list_cities_by_state(user, password, db_name, state_name):
    """
    Connecte à la base et liste les villes d'un état spécifique
    """
    try:
        # Connexion à la base MySQL
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=user,
            passwd=password,
            db=db_name
        )
        # Création du curseur
        cursor = db.cursor()
        # Requête SQL paramétrée avec jointure
        query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
        """
        # Exécution sécurisée avec le paramètre
        cursor.execute(query, (state_name,))
        # Récupération de tous les résultats
        cities = cursor.fetchall()
        # Formatage des résultats en chaîne séparée par des virgules
        city_names = [city[0] for city in cities]
        print(", ".join(city_names))
        # Fermeture des ressources
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("Erreur MySQL :", e)
        sys.exit(1)

# Point d'entrée principal
if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) != 5:
        print("Usage : ./5-filter_cities.py <user> <password> <db_name> <state_name>")
        sys.exit(1)
    # Appel avec les bons arguments
    list_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
