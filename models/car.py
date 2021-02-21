from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from models.db_connection import Base


class Car(Base):
    __tablename__ = 'car'

    id = Column(Integer, primary_key=True)
    model = Column('model', String)
    release_year = Column('release_year', Integer)
    brand_id = Column(Integer, ForeignKey('brand.id'), nullable=False)
    brand = relationship('Brand', foreign_keys='Car.brand_id', backref='cars')

    def __repr__(self):
        return f'{self.model} {self.release_year}'
