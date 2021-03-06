from pydantic import BaseModel


class Product(BaseModel):
    name: str
    description: str
    price: int


class DisplaySeller(BaseModel):

    # Using Python3.9 the id must be declared.
    id: int
    username: str
    email: str

    class Config:
        orm_mode = True


class DisplayProduct(BaseModel):

    # Using Python3.9 the id must be declared.
    id: int
    name: str
    description: str
    seller: DisplaySeller

    class Config:
        orm_mode = True


class Seller(BaseModel):
    username: str
    email: str
    password: str
