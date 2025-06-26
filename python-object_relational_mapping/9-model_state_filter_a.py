#!/usr/bin/python3
"""
Script pour lister les états contenant la lettre 'a'
Prend 3 arguments : utilisateur, mot de passe et nom de la base
Utilise SQLAlchemy et le modèle State
Connecte en localhost:3306
Trie par id croissant
Affiche les résultats au format <id>: <name>
Ne s'exécute pas lors d'un import
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def filter_states_with_a(username, password, db_name):
    """
    Connecte à la base et liste les états contenant 'a'
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
        
        # Requête filtrée et triée
        states = session.query(State)\
                       .filter(State.name.like('%a%'))\
                       .order_by(State.id)\
                       .all()
        
        # Affichage des résultats
        for state in states:
            print(f"{state.id}: {state.name}")
            
        # Fermeture de la session
        session.close()
        
    except Exception as e:
        print("Erreur :", e)
        sys.exit(1)

# Point d'entrée principal
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./9-model_state_filter_a.py <user> <password> <db_name>")
        sys.exit(1)
    
    filter_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
