#!/usr/bin/python3
"""
Script pour récupérer le premier objet State
Prend 3 arguments : utilisateur, mot de passe et nom de la base
Utilise SQLAlchemy et le modèle State
Connecte en localhost:3306
Affiche le premier état par id croissant
Si la table est vide, affiche "Nothing"
Ne s'exécute pas lors d'un import
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def get_first_state(username, password, db_name):
    """
    Connecte à la base et récupère le premier State
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
        
        # Récupération du premier état par id croissant
        first_state = session.query(State).order_by(State.id).first()
        
        # Affichage du résultat
        if first_state:
            print(f"{first_state.id}: {first_state.name}")
        else:
            print("Nothing")
            
        # Fermeture de la session
        session.close()
        
    except Exception as e:
        print("Erreur :", e)
        sys.exit(1)

# Point d'entrée principal
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./8-model_state_fetch_first.py <user> <password> <db_name>")
        sys.exit(1)
    
    get_first_state(sys.argv[1], sys.argv[2], sys.argv[3])
