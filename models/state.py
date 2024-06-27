#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import Base
from models.city import City



storage = getenv('HBNB_TYPE_STORAGE')

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if storage == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")
    else:
        name = ""
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
