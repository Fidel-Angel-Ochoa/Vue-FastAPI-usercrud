from fastapi import APIRouter,Response, status
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.user import users
from schemas.user import User
from typing import List

from cryptography.fernet import Fernet

user = APIRouter()

# this method and function are used to encrypt the passwords
key = Fernet.generate_key()
f = Fernet(key)

# We use 'response_model' to stipulate in the documentation the model of data that we goin to get. It can be a model like 'User' or a error status. we most past this as a "List"
# At same time we can group the routes by 'tags'.
@user.get("/users", response_model=List[User], tags=["Users"])
def get_users():
    # we call 'fetchall' after made the sql consultation.
    return conn.execute(users.select()).fetchall()

# Usamos 'User' desde 'schemas.user' por que es la plantilla para recibir los datos que deseamos, esta se pasa a la app
@user.post('/users', response_model= User, tags=["Users"])
def create_user(user: User):
    new_user = {"name":user.name, "email":user.email}
    new_user["password"] = f.encrypt(user.password.encode("utf-8")) # we encrytp the password and we need to use utf-8 format to use it in a dictionary
    result = conn.execute(users.insert().values(new_user))
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first() # '.lastrowid es una propiedad que permite obtener el ultimo id junto con el resto de atributos. Lo anterior nos devuelve una lista entoces '.first()' nos devuelve el primer elemento.

@user.get("/users/{id}", response_model= User, tags=["Users"])
def get_user(id:str):
    return conn.execute(users.select().where(users.c.id == id)).first()

@user.delete("/users/{id}", status_code= status.HTTP_204_NO_CONTENT, tags=["Users"])
def delete_user(id:str):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)

# aqui no usamos otra variable como 'new_user' usada en 'create_user' por que el objeto ya esta creado, solo modificaremos los valores.
@user.put("/users/{id}", response_model= User, tags=["Users"])
def update_user(id:str, user:User):    
    conn.execute(users.update().values(name = user.name, email = user.email, password = f.encrypt(user.password.encode("utf-8"))).where(users.c.id == id))
    # la siguiente linea significa: conn(conectas a la db), execute(realizas accion) dentro de la tabla 'users', la accion es 'select'(seleccionar), .where(users.c.id == id (dentro de la tabla 'users' en la columna 'id' el id que sea igual al id que se proporciono en 'user' )
    return conn.execute(users.select().where(users.c.id == id)).first()
