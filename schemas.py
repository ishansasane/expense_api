from pydantic import BaseModel
import datetime


class LoginUser(BaseModel):
    email: str
    password: str

class UserRegister(BaseModel):
    name: str
    email: str
    password: str

class User(BaseModel):  # Pydantic model for returning user details
    id: int
    name: str
    email: str
    created_date: datetime.datetime

    class Config:
        orm_mode = True  # This is needed to convert the SQLAlchemy model to Pydantic model

class Expense(BaseModel):
    id: int
    user_id: int
    expense_date: datetime.datetime
    expense_amount: float
    expense_type: str
    created_date: datetime.datetime
