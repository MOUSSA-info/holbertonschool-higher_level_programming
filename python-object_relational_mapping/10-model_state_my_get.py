#!/usr/bin/python3
"""
Script pour récupérer un état par son nom
Prend 4 arguments : utilisateur, mot de passe, base de données et nom d'état
Utilise SQLAlchemy et le modèle State
Connecte en localhost:3306
Affiche l'ID de l'état ou "Not found"
Sécurisé contre les injections SQL
Ne s'exécute pas lors d'un import
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def get_state_by_name(username, password, db_name, state_name):
    """
    Connecte à la base et récupère l'ID d'un état par son nom
    """
    try:
        # Création du moteur de connexion
        engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
            pool_pre_ping=True
        )
        
        # Création d'une session
        Session = sessionmaker(bind=engine)
        session = Session()
        
        # Requête sécurisée pour récupérer l'état par son nom
        state = session.query(State)\
                      .filter(State.name == state_name)\
                      .first()
        
        # Affichage du résultat
        if state:
            print(state.id)
        else:
            print("Not found")
            
        # Fermeture de la session
        session.close()
        
    except Exception as e:
        print("Erreur :", e)
        sys.exit(1)

# Point d'entrée principal
if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./10-model_state_my_get.py <user> <password> <db_name> <state_name>")
        sys.exit(1)
    
    get_state_by_name(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
