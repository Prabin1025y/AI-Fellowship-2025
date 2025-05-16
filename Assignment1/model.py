#import required dependencies
from database import metadata
from sqlalchemy import Table, Column, Integer, String

#create a new notes table with 3 columns [id, title, content]
notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key = True), #this is primary key
    Column("title", String(length=100)),
    Column("content", String(length=255))
)