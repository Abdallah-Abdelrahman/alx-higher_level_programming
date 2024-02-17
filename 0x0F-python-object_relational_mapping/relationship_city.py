#!/usr/bin/python3
'''Class definition of a City'''

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base


class City(Base):
    '''class City maps to `cities` table

    Attrs:
        __tablename__: table's name
        id: city's id
        name: city's name
        state_id: foreign key references `states.id`
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
