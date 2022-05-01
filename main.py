from fastapi import FastAPI


app = FastAPI()

# Static Routes or Static Functions must be placed at first.
@app.get("/user/admin")
def profile():
    return {f"This a simple admin page"}


# Dynamics Routes or Dynamics Functions must be placed at first.
@app.get("/user/{username}")
def profile(username: str):
    return {f"This is a profile page for {username}"}
