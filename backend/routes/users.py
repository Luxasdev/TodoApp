from fastapi import APIRouter
from sqlmodel import Session, select
from backend.models import User
from backend.database import engine

router = APIRouter()

@router.post("/register")
def register(user: User):
    with Session(engine) as session:
        session.add(user)
        session.commit()
        return {"message": "user created"}

@router.post("/login")
def login(user: User):
    with Session(engine) as session:
        statement = select(User).where(User.username == user.username)
        result = session.exec(statement).first()

        if result and result.password == user.password:
            return {"message": "login ok", "user_id": result.id}
        return {"error": "wrong credentials"}