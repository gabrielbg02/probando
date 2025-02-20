from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    apellido: str
    edad: int

user_list = [ User (id = 1, name = "Gabriel", apellido = "Borges", edad = 44),
              User (id = 2, name = "Juan", apellido = "Perez", edad = 11),
              User (id = 3, name = "Raul", apellido = "Caicedo", edad = 22),]


@app.get("/users")
def saludo():
    return user_list()
    



#@app.get("/")
#def saludo():
#    return {"hlola": "mundddddo"}


#@app.get("/url")
#def proue():
#    return {"mggg": "mundo"}

#@app.get("/ulo")
#def proue():
#    return {"mggg": "mundo"}

