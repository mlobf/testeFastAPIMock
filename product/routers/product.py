from fastapi import APIRouter, Response, HTTPException, status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from typing import List
from .. import schemas


router = APIRouter(tags=["Products"], prefix="/product")


@router.get("/", response_model=List[schemas.DisplayProduct])
def get_products(db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    return products


@router.get("/{id}", response_model=schemas.DisplayProduct)
def get_product(id, response: Response, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found."
        )
    return product


@router.delete("/{id}")
def delete_product(id, db: Session = Depends(get_db)):
    product = (
        db.query(models.Product)
        .filter(models.Product.id == id)
        .delete(synchronize_session=False)
    )
    db.commit()
    return {"Data deleted"}


@router.put("/{id}")
def update_product(id, request: schemas.Product, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        pass
    product.update(request.dict())
    db.commit()
    return {"Product successfully updated"}


@router.post("/", status_code=status.HTTP_201_CREATED)
def add_product(request: schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(
        name=request.name,
        description=request.description,
        price=request.price,
        seller_id=1,
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    return request
