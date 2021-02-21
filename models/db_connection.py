from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL


DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': '',
    'password': '',
    'database': 'postgres'
}

engine = create_engine(URL(**DATABASE))
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()
