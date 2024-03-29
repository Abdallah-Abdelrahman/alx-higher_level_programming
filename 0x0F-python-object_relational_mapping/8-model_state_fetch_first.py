#!/usr/bin/python3
'''Prints the first State object from the database hbtn_0e_6_usa'''

import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    # sessionmaker function returns `Session` class
    session = sessionmaker(bind=engine)()
    state = session.query(State).first()
    print('{}: {}'.format(state.id, state.name)) if state else print('Nothing')
