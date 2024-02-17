#!/usr/bin/python3
'''prints the State object with the name passed as argument'''

import sys
from model_state import State, Base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    # sessionmaker function returns `Session` class
    session = sessionmaker(bind=engine)()
    id = session.query(State.id)\
        .filter_by(name=func.binary(sys.argv[4])).one_or_none()
    print(id[0] if id else 'Not found')
