#!/usr/bin/python3
'''class definition of a State'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    '''class State maps to `states` table

    Attrs:
        __tablename__: table's name
        id: state id
        name: state name
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
