#!/usr/bin/python3
"""
Script pour lister toutes les villes avec leur état
Prend 3 arguments : utilisateur, mot de passe et nom de la base
Utilise le module MySQLdb
Connecte en localhost:3306
Trie par id de ville croissant
Utilise une seule commande execute()
Affiche les résultats comme dans l’exemple
Ne s’exécute pas lors d’un import
"""

import MySQLdb
import sys

def list_cities(user, password, db_name):
    """
    Connecte à la base et liste les villes avec leur état
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
        # Requête SQL unique avec JOIN
        query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """
        # Exécution unique de la requête
        cursor.execute(query)
        # Récupération et affichage des résultats
        results = cursor.fetchall()
        for row in results:
            print(row)
        # Fermeture des ressources
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("Erreur MySQL :", e)
        sys.exit(1)

# Point d'entrée principal
if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) != 4:
        print("Usage : ./4-cities_by_state.py <user> <password> <db_name>")
        sys.exit(1)
    # Appel avec les bons arguments
    list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
