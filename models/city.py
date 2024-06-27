#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

storage = getenv('HBNB_TYTPE_STORAGE')


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    if storage is 'db':
        name = Column(String(128), nullable=True)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=True)
        places = relationship("Place", backref="cities", cascade="delete")
    else:
        state_id = ""
        name = ""
