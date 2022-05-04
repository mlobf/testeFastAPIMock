from fastapi import FastAPI, status, Response, HTTPException
from fastapi.params import Depends
from sqlalchemy.orm import Session
from . import schemas
from . import models
from .database import engine, SessionLocal, get_db
from typing import List
from passlib.context import CryptContext
from .routers import product


app = FastAPI()

models.Base.metadata.create_all(engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app.include_router(product.router)


@app.post(
    "/seller", response_model=schemas.DisplaySeller, status_code=status.HTTP_201_CREATED
)
def create_seller(request: schemas.Seller, db: Session = Depends(get_db)):
    hashedpassword = pwd_context.hash(request.password)
    new_seller = models.Seller(
        username=request.username,
        email=request.email,
        password=hashedpassword,
    )

    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller
