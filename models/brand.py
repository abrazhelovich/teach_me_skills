from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL
from models.db_connection import Base


class Brand(Base):
    __tablename__ = 'brand'

    id = Column(Integer, primary_key=True)
    name = Column('name', String)
    #car = relationship('Car', backref="brand")

    def __repr__(self):
        return f'id: {self.id} Name {self.name}'








