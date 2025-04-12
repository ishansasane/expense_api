from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import UserRegister, User, LoginUser
from database import get_db
from models import User as DBUser
from .Hash import hash_password, verify_password
from .token import create_access_token

router = APIRouter(
    prefix="/users",
    tags=["users"],
)

@router.post('/register', response_model=User)
def register_user(user: UserRegister, db: Session = Depends(get_db)):
    # Check if user already exists
    existing_user = db.query(DBUser).filter(DBUser.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = DBUser(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post('/login')
def login(user: LoginUser, db: Session = Depends(get_db)):
    user_db = db.query(DBUser).filter(DBUser.email == user.email).first()
    
    if not user_db or not verify_password(user.password, user_db.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    
    access_token = create_access_token(data={"user_id": user_db.id})
    return {"access_token": access_token, "token_type": "bearer"}
