from fastapi import APIRouter

router = APIRouter()

todos = []

@router.get("/todos")
def get_todos():
    return todos

@router.post("/todos")
def add_todo(todo: dict):
    todos.append(todo)
    return {"message": "added"}