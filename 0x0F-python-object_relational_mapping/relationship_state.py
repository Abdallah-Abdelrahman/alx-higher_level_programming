#!/usr/bin/python3
'''Extends class definition of `State`'''

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    '''class State maps to `states` table

    Attrs:
        __tablename__: table's name
        id: state id
        name: state name
        cities: relationship with class `City`
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan', order_by='City.id')
