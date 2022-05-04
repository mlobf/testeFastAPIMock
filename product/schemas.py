from product.models import Product
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    price: int


class DisplayProduct(BaseModel):

    # Using Python3.9 the id must be declared.
    id: int
    name: str
    description: str

    class Config:
        orm_mode = True
