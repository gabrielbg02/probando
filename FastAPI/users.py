from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    apellido: str
    edad: int

users_list = [User (id = 1, name = "Gabriel", apellido = "Borges", edad = 44),
              User (id = 2, name = "Juan", apellido = "Perez", edad = 11),
              User (id = 3, name = "Raul", apellido = "Caicedo", edad = 22)]


@app.get("/users")
def mostrar():
    return users_list
    
@app.get("/user/{id}")
def user(id:int):
    return search_user(id)


@app.get("/userquery")
def userquery(id:int):
    return search_user(id)


def search_user(id: int):
    users = filter (lambda user : user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"ERROR" : "NO SE HA ENCONTRADO AL USUARIO"}

@app.post ("/user/")
def user (user : User):
    if type(search_user(user.id)) == User:
        return {"ERROR" : "EL USUARIO YA EXISTE"}
    else:
        users_list.append(user)
        return user


@app.put ("/user/")
def user (user: User):
    found = False
    for index, saved_user in enumerate (users_list):
        if saved_user.id == user.id : 
            users_list [index] = user
            found = True
    if not found:
        return {"ERROR" : "EL USUARIO NO SE HA ACTUALIZADO"}
    else:
        return user

@app.delete("/user/{id}")
def borrar (id : int):
    found = False
    for index, saved_user in enumerate (users_list):
        if saved_user.id == id: 
            del users_list [index]
        found = True
    if not found:
        return {"ERROR" : "EL USUARIO NO SE HA ELIMINADO"}
   





#@app.get("/")
#def saludo():
#    return {"hlola": "mundddddo"}


#@app.get("/url")
#def proue():
#    return {"mggg": "mundo"}

#@app.get("/ulo")
#def proue():
#    return {"mggg": "mundo"}

