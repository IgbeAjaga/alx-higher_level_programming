#!/usr/bin/python3
"""Defines the City class
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State

class City(Base):
    """City class definition
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nunique=True, ullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
