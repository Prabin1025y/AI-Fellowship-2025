#importing all needed dependencies
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from database import database, engine, metadata
from pydantic import BaseModel
from model import notes
import logging
import sys

#initializing the logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("app")

#sql alchemy creates all tables with specified columns using this line
metadata.create_all(engine)

#using modern lifespan handler of fastapi over deprecated on_event handler
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up... connecting to DB")
    await database.connect()
    yield
    print("Shutting down... disconnecting from DB")
    await database.disconnect()

#initializing our fastapi app
app = FastAPI(lifespan=lifespan)

#required basemodel classes
class NoteIn(BaseModel):
    title: str
    content: str

class NoteOut(NoteIn):
    id: int

#post request to create a new note
@app.post("/notes/", response_model=NoteOut)
async def create_note(note: NoteIn):
    query = notes.insert().values(title = note.title, content = note.content)
    note_id = await database.execute(query)
    logger.info(f"Note created {note.title}")
    return {**note.dict(), "id":note_id}

#get request to fetch all available notes
@app.get("/notes/", response_model=list[NoteOut])
async def read_notes():
    query = notes.select()
    logger.info("Note retreived")
    return await database.fetch_all(query)

#delete request to delete a note given its note id
@app.delete("/notes/{note_id}", status_code=204)
async def delete_note(note_id: int):
    query = notes.delete().where(notes.c.id == note_id)
    result = await database.execute(query)
    if result == 0:
        #raise an exception if note with given noteid is not available
        raise HTTPException(status_code=404, detail="Note not found")
    return None