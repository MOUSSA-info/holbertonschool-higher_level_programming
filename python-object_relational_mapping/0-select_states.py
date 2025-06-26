#!/usr/bin/python3
"""
Script pour lister tous les états de la base hbtn_0e_0_usa
Prend 3 arguments : utilisateur, mot de passe et nom de la base
Utilise le module MySQLdb
Connecte en localhost:3306
Affiche les résultats comme dans l’exemple
Ne s’exécute pas lors d’un import
"""

import MySQLdb
import sys

def list_states(user, password, db_name):
    """
    Connecte à la base et liste les états, triés par id croissant
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
        # Exécution de la requête SQL
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        # Récupération de tous les résultats
        states = cursor.fetchall()
        # Affichage ligne par ligne
        for state in states:
            print(state)
        # Fermeture du curseur et de la connexion
        cursor.close()
        db.close()
    except MySQLdb.Error as e:
        print("Erreur MySQL :", e)
        sys.exit(1)

# Ne s’exécute que si le script est lancé directement
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage : ./0-select_states.py <user> <password> <db_name>")
        sys.exit(1)
    # Appel de la fonction avec les arguments
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
