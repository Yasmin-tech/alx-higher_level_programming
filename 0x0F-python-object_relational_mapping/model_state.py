#!/usr/bin/python3
""" This module contain the class State that will be a mapper
to table state in the database hbtn_0e_6_usa"""

from sqlalchemy import Integer, String, Column, MetaData
from sqlalchemy.ext.declarative import declarative_base


mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    __tablename__ = "states"

    id = Column(
        'id', Integer,
        autoincrement=True,
        nullable=False,
        unique=True,
        primary_key=True)
    name = Column('name', String(128), nullable=False)
