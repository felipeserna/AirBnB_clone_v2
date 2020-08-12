#!/usr/bin/python3
""" City Module for HBNB project """

from models.base_model import BaseModel
#from sqlalchemy import Column, Integer, String, ForeignKey
#from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.orm import relationship


#Base = declarative_base()


class City(BaseModel):
    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
   # __tablename__ = 'cities'
   # state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
   # name = Column(String(128), nullable=False)
   # state = relationship("State", back_populates="cities",
   #                      cascade="all, delete")
