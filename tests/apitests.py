from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_todo():
    # Test creating a new todo item
    todo_data = {"content": "Test Todo"}
    response = client.post("/todo/add", json=todo_data)
    assert response.status_code == 200
    assert response.json()["content"] == "Test Todo"

def test_get_todo():
    # Test getting all todo items
    response = client.get("/todo")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_update_todo():
    # Test updating a todo item
    todo_data = {"content": "Updated Todo"}
    response = client.put("/todo/update/1", json=todo_data)
    assert response.status_code == 200
    assert response.json()["content"] == "Updated Todo"

def test_delete_todo():
    # Test deleting a todo item
    response = client.delete("/todo/delete/1")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo deleted successfully"}

