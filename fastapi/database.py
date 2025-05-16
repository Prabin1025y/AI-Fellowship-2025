#importing required dependencies
import os
from databases import Database
from sqlalchemy import create_engine, MetaData

#get db url form env of use a default sqlite if not avalilable

#initialize the database
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./notes.db")
database = Database(DATABASE_URL)
metadata = MetaData()

#create a new sqlalchemy engine to create tables
engine = create_engine(DATABASE_URL)