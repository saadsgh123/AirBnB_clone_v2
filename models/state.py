#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=True)
        cities = relationship('City', cascade="all,delete", backref="state")
    else:
        @property
        def cities(self):
            ''' return list '''
            from moduls import storage
            Cityl = []
            citys = storage.all(City)
            for city in citys.values():
                if city.state_id == self.id:
                    Cityl.append(city)
            return Cityl
