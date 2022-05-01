from fastapi import FastAPI


app = FastAPI()

# id here is a path parameter
@app.get("/parameters/{id}")
def index(id):
    return {f"Hello to Paramete's World!!{id}"}


@app.get("/")
def index():
    return "Hello World!!"


@app.get("/movies")
def index():
    return {"movies list": {"Movie One", "Movie two"}}
