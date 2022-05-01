from fastapi import FastAPI


app = FastAPI()

# id here is a path parameter
@app.get("/parameters/{id}")
def index(id):
    return {f"Hello to Paramete's World!!{id}"}


# id must be a integer now
@app.get("/parameter_typed/{id}")
def index(id: int):
    return {f"Hello to Paramete's World!!{id}"}


# id must be a string now
@app.get("/username/{username}")
def index(username: str):
    return {f"Hi my name is {username}"}


@app.get("/")
def index():
    return "Hello World!!"


@app.get("/movies")
def index():
    return {"movies list": {"Movie One", "Movie two"}}
