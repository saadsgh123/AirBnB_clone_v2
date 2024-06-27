#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City
from os import getenv

storage_type = getenv('HBNB_TYPE_STORAGE')

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if storage_type == 'db':
        name = Column(String(128), nullable= False)
        cities_relationship = relationship("City", cascade='all, delete-orphan', backref='state')

    else:
        @property
        def cities(self):
            """Returns all cities associated with the state"""
            from models import storage
            cities = storage.all(City)
            return [city for city in cities.values() if city.state_id == self.id]
