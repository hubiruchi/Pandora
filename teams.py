#!py
from sqlalchemy import Column, Integer, String
from database import Base

class Team(Base):
    """A Team object.

    :param int number: team's number
    :param str name: team's name

    """
    __tablename__ = 'teams'

    number = Column(Integer, primary_key=True, autoincrement=False)
    name = Column(String(50))
    
    def __init__(self, number, name):
        self.number = number
        self.name = name
        
    def __repr__(self):
        return "< %s, %s>"%(self.name,self.number)