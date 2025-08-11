#!/usr/bin/python3
''' model state update id 2'''
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
    # Query the state with id 2
    state = session.query(State).filter(State.id == 2).first()
    # Update the state's name
    if state:
        state.name = "New Mexico"
        session.commit()