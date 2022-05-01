from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def index():
    return "Hello World!!"


@app.get("/movies")
def index():
    return {"movies list": {"Movie One", "Movie two"}}
