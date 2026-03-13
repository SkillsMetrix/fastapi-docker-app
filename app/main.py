from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():

    return {"message": "FastAPI running inside Docker via Jenkins again and again"}


@app.get("/welcome")
def home():
    return {"message": "Welcome to CI CD"}
