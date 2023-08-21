#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create an engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
            .format(username, password, database), pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the database for all State objects
    states = session.query(State).order_by(State.id).all()

    # Display results
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
