from __future__ import barry_as_FLUFL
from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    price: int
