from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey, func
from database import base

class User(base):  # SQLAlchemy Model
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())

class Expense(base):
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    expense_date = Column(DateTime(timezone=True), nullable=False)
    expense_amount = Column(Float, nullable=False)
    expense_type = Column(String(50), nullable=False)
    created_date = Column(DateTime(timezone=True), server_default=func.now())
