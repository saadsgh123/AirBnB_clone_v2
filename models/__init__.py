#!/usr/bin/python3
"""This module instantiates an object of class FileStorage or DBStorage"""

from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    print("Using DBStorage...")
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    print("Using FileStorage...")
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()