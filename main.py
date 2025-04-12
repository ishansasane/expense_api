from fastapi import FastAPI
from database import base, engine
import models  # this is important to load the models before create_all()
from routes import Users , Expense

app = FastAPI()

# Create tables in DB
base.metadata.create_all(bind=engine)

app.include_router(Users.router)
app.include_router(Expense.router)
