from fastapi import FastAPI
from pydantic import BaseModel, Field


class Profile(BaseModel):
    name: str
    email: str
    age: int


class Product(BaseModel):
    name: str
    price: int = Field(
        title="Price of the item", description="This all values in Local Currency", gt=0
    )
    discount: int
    discounted_price: float


class User(BaseModel):
    name: str
    email: str


app = FastAPI()


@app.post("/purchase")
def purchase(user: User, product: Product):
    return {"user": user, "product": product}


# Static Routes or Static Functions must be placed at first.
@app.get("/user/admin")
def profile():
    return {f"This a simple admin page"}


# Dynamics Routes or Dynamics Functions must be placed at first.
# Path Parameters
@app.get("/user/{username}")
def profile(username: str):
    return {f"This is a profile page for {username}"}


# Query Parameters
@app.get("/products")
def products(id: int, price: int):
    return {f"Products with an id:{id} and price:{price}"}


# Default Values for Query Parameters
@app.get("/cars")
def products(id: int = 1, price: int = 10):
    return {f"Cars with an id:{id} and price:{price}"}


# Query Parameters and_
# Default Values for Query Parameters
@app.get("/profile/{userid}/comments")
def profile(userid: int = 10, commentid: int = 100):
    return {
        f"Profile page for user with user id {userid} and comment with :{commentid}"
    }


# Required Query Parameters
@app.get("/bikes")
def bikes(id: int = None, price: int = None):
    return {f"Cars with an id:{id} and price:{price}"}


# Post
@app.post("/add_user/")
def add_user(profile: Profile):
    return profile


@app.post("/add_product/{product_id}")
def add_product(product: Product, product_id: int, category: str):
    product.discounted_price = product.price - (product.price * product.discount) / 100
    return {"product_id": product_id, "product": product, "category": category}
