#!/usr/bin/python3
'''model state insert '''
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
    # Create a new state
    new_state = State(name="Louisiana")
    # Add the state to the session and commit
    session.add(new_state)
    session.commit()
    # Print the new state's id
    print(new_state.id)
