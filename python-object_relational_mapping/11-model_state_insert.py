#!/usr/bin/python3
"""
Script pour ajouter l'état "Louisiana" à la base
Prend 3 arguments : utilisateur, mot de passe et nom de la base
Utilise SQLAlchemy et le modèle State
Connecte en localhost:3306
Affiche le nouvel ID après création
Ne s'exécute pas lors d'un import
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def add_louisiana(username, password, db_name):
    """
    Ajoute l'état "Louisiana" à la base et retourne son ID
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
        
        # Création du nouvel objet State
        new_state = State(name="Louisiana")
        
        # Ajout à la session
        session.add(new_state)
        
        # Validation dans la base
        session.commit()
        
        # Affichage du nouvel ID
        print(new_state.id)
            
        # Fermeture de la session
        session.close()
        
    except Exception as e:
        print("Erreur :", e)
        sys.exit(1)

# Point d'entrée principal
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./11-model_state_insert.py <user> <password> <db_name>")
        sys.exit(1)
    
    add_louisiana(sys.argv[1], sys.argv[2], sys.argv[3])
