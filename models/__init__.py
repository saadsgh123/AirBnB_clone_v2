#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBStorage"""
from models.engine.file_storage import FileStorage
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.file_storage import DBStorage
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()