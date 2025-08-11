#!/usr/bin/python3
''' model state delete'''
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    # Connect to the MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query and delete states containing 'a' in their name
    states_to_delete = session.query(State).filter(
            State.name.like('%a%')).all()
    for state in states_to_delete:
        session.delete(state)
    # Commit the transaction
    session.commit()
