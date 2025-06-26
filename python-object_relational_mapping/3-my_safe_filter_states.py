#!/usr/bin/python3
"""
Script sécurisé contre les injections SQL pour filtrer les états par nom
Prend 4 arguments : utilisateur, mot de passe, base de données et nom d'état
Utilise des requêtes paramétrées pour éviter les injections SQL
Connecte en localhost:3306
Affiche les résultats correspondants
Ne s’exécute pas lors d’un import
"""

import MySQLdb
import sys

def safe_filter_states(user, password, db_name, state_name):
    """
    Connecte à la base et liste les états correspondant au nom fourni
    en utilisant une requête paramétrée pour la sécurité
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
        # Requête SQL paramétrée
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
        # Exécution sécurisée avec le paramètre
        cursor.execute(query, (state_name,))
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
if __name__ ==
