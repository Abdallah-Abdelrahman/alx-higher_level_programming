#!/usr/bin/python3
'''Adds the State object “Louisiana” to the database hbtn_0e_6_usa'''

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
    state = State(name='Louisiana')
    session.add(state)
    session.commit()
    print(state.id)
