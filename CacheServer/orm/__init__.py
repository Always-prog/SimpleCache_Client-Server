"""FILE FOR SETTING UP WORK WITH DATABASE"""
from os import environ

from sqlalchemy import create_engine

# Connect
DB_USER = environ.get('DB_USER', 'postgres')
DB_PASSWORD = environ.get('DB_PASSWORD', 'postgres')
DB_NAME = environ.get('DB_NAME', 'fastapidb')
DB_HOST = environ.get('DB_HOST', 'localhost')

engine = create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}', echo=True)
db_connection = engine.connect()
