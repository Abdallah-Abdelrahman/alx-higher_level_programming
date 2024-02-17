#!/usr/bin/python3
'''lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa.
'''

import sys
from relationship_state import Base, State
from relationship_city import City as _
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    # sessionmaker function returns `Session` class
    session = sessionmaker(bind=engine)()
    query_result = ''
    states = session.query(State).all()
    for state in states:
        print('{}: {}'.format(state.id, state.name))
        for c in state.cities:
            print(f'\t{c.id}: {c.name}')
