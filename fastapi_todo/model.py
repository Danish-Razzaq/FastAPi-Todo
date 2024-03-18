from typing import Optional
from sqlmodel import SQLModel, Field, create_engine
import os
from dotenv import load_dotenv

load_dotenv()

conn_str = os.getenv("DATABASE_URL") # thsi is best apporouch to set your links in .env file 

print("Database URL:", conn_str)  # Add this line to check conn_str

class TodoBase(SQLModel):
    contant:str
    id_done :bool = Field(default=False)

# todo this type of data  todo crete in this project
class Todo(SQLModel, table= True):
    id: Optional[int] = Field(default=None, primary_key=True)
    contant : str
    is_done : bool = Field(default=False)

class TodoResponse(SQLModel):
    id : int
    contant : str
    is_done : bool

engine = create_engine(conn_str, echo=True)

def create_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == "__main__":
    create_tables()