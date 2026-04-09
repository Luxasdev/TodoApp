from fastapi import FastAPI
from backend.routes import todos

from fastapi import FastAPI
from backend.database import create_db
from backend.routes import users, todos

app = FastAPI()

app.include_router(todos.router)


app = FastAPI()

create_db()

app.include_router(users.router)
app.include_router(todos.router)