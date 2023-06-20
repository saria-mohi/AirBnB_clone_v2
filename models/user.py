#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    places = relationship("Place",
                          cascade="all,delete",
                          backref=backref("user", cascade="all,delete"),
                          passive_deletes=True,
                          single_parent=True)
    reviews = relationship("Review",
                           cascade="all,delete",
                           backref=backref("user", cascade="all,delete"),
                           passive_deletes=True,
                           single_parent=True)
