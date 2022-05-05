from fastapi import FastAPI
from . import models
from .database import engine
from passlib.context import CryptContext
from .routers import product, seller


app = FastAPI(
    title="ChimichangApp",
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

app.include_router(product.router)
app.include_router(seller.router)

models.Base.metadata.create_all(engine)
