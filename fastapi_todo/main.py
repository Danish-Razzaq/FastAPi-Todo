from fastapi import FastAPI, Depends
from typing import Annotated
from .model import Todo , TodoBase , engine , conn_str, TodoResponse  # Import the Todo model here
from sqlmodel import Session, select
from sqlmodel import  create_engine
import os
from dotenv import load_dotenv


load_dotenv()

conn_str = os.getenv("DATABASE_URL") # thsi is best apporouch to set your links in .env file 

# OR

print("Database URL:", conn_str)  # Add this line to check conn_str
engine = create_engine(conn_str, echo=True)


app = FastAPI(title="Todo App")

def get_data():
    with Session(engine) as session:
        yield session    

# get data
@app.get("/todo")
def get_todo(session:Annotated[Session, Depends(get_data)]):
    todo = session.exec(select(Todo)).all()
    return todo
    

# post data
@app.post("/todo/add", response_model=TodoResponse)
def add_todo(todo:TodoBase, session:Annotated[Session, Depends(get_data)]):
    add_todo = Todo.model_validate(todo)
    session.add(add_todo)
    session.commit()
    session.refresh(add_todo)
    return add_todo

# update data
@app.put("/todo/update/{id}", response_model=TodoResponse)
def update_todo(id:int, todo:TodoBase, session:Annotated[Session, Depends(get_data)]):
 
    todo_update = session.get(Todo, id)
    if not todo_update:
        return {"message":"Todo not found"}
    todo_update.contant = todo.contant
    todo_update.is_done = todo.id_done
    session.commit()
    session.refresh(todo_update)
    return  todo_update
   

# delete data
@app.delete("/todo/delete/{id}", response_model=TodoResponse)
def delete_todo(id:int, session:Annotated[Session, Depends(get_data)]):
    
    todo_delete = session.get(Todo, id)
    if not todo_delete:
        return {"message":"Todo not found"}
    session.delete(todo_delete)
    session.commit()
    return  delete_todo
        
    




    


    

