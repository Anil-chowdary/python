from typing import Optional
from fastapi import FastAPI, Depends, HTTPException
from model import Base, User
from pydantic import BaseModel
from schema import UserSchema
from database import engine, Sessionlocal
from sqlalchemy.orm import Session

# Initialize the FastAPI app
app = FastAPI()

# Create the database schema
Base.metadata.create_all(bind=engine)

# Dependency to get DB session
def get_db():
    try:
        db = Sessionlocal()
        yield db
    finally:
        db.close()

# Define the endpoint to add a user
@app.post("/adduser")
def add_user(request: UserSchema, db: Session = Depends(get_db)):
    user = User(name=request.name, email=request.email, nickname=request.nickname)
    db.add(user)
    db.commit()
    db.refresh(user)
