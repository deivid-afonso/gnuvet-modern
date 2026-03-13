from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.deps import get_db
from app.schemas.user_schema import UserCreate, UserLogin
from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth")


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):

    db_user = User(
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(db_user)
    db.commit()

    return {"message": "user created"}


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        return {"error": "invalid credentials"}

    if not verify_password(user.password, db_user.password):
        return {"error": "invalid credentials"}

    token = create_access_token({"sub": db_user.email})

    return {"access_token": token}