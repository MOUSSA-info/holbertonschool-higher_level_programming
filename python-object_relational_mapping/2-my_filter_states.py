#!/usr/bin/python3
"""
Script pour filtrer les états par nom saisi
Prend 4 arguments : utilisateur, mot de passe, base de données et nom d'état
Utilise le module MySQLdb
Connecte en localhost:3306
Affiche les résultats correspondants
Ne s’exécute pas lors d’un import
"""

import MySQLdb
import sys

def filter_states(user, password, db_name, state_name):
    """
    Connecte à la base et liste les états correspondant au nom fourni
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
        # Construction de la requête avec format()
        query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
        # Exécution de la requête
        cursor.execute(query)
        # Récupération et affichage des résultats
        states = cursor.fetchall()
        for state in states:
            print(state)
        # Nettoyage
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("Erreur MySQL :", e)
        sys.exit(1)

# Point d'entrée principal
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage : ./2-my_filter_states.py <user> <password> <db_name> <state_name>")
        sys.exit(1)
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
