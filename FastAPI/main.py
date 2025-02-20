from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def saludo():
    return {"hlola": "mundo"}


@app.get("/url")
def proue():
    return {"mggg": "mundo"}

