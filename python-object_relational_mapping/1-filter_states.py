#!/usr/bin/python3
"""
Script pour lister les états commençant par 'N' de la base hbtn_0e_0_usa
Prend 3 arguments : utilisateur, mot de passe et nom de la base
Utilise le module MySQLdb
Connecte en localhost:3306
Affiche les résultats comme dans l’exemple
Ne s’exécute pas lors d’un import
"""

import MySQLdb
import sys

def filter_states(user, password, db_name):
    """
    Connecte à la base et liste les états commençant par 'N'
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
        # Requête SQL pour récupérer les états commençant par 'N'
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
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
    if len(sys.argv) != 4:
        print("Usage : ./1-filter_states.py <user> <password> <db_name>")
        sys.exit(1)
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
