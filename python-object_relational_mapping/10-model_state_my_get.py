#!/usr/bin/python3
'''model state my get '''
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
if __name__ == "__main__":
    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]
    # Connect to the MySQL server
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}'
    )
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Query the database for the state with the given name
    state = session.query(State).filter(State.name == state_name).first()
    # Display the result
    if state:
        print(state.id)
    else:
        print("Not found")
