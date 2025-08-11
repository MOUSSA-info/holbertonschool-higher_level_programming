#!/usr/bin/python3
"""List all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City  # N'oubliez pas d'importer la classe City !

if __name__ == "__main__":

    # Vérification du nombre d'arguments
    if len(sys.argv) != 4:
        exit(1)

    # Connexion à la base de données
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(username, password, db_name),
        pool_pre_ping=True
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Interroger les villes et les états associés
    cities = session.query(City, State).join(State).order_by(City.id).all()

    # Affichage des résultats
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Fermeture de la session
    session.close()
