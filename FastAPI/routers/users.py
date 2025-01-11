# Iniciar el server: uvicorn users:app --reload
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

# Entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

# Lista de usuarios de ejemplo
users_list = [
    User(id=1, name="Rick", surname="Sanchez", url="https://korm.com", age=70),
    User(id=2, name="Morty", surname="Smith", url="https://korm.com", age=30),
    User(id=3, name="Summer", surname="Smith", url="https://korm.com", age=59)
]

# Función de búsqueda de usuarios
def search_user(user_id: int) -> Optional[User]:
    for user in users_list:
        if user.id == user_id:
            return user
    return None

# Rutas
@router.get("/usersjson")
async def usersjson():
    return [
        {"name": "Rick", "surname": "Sanchez", "url": "https://korm.com", "age": 70},
        {"name": "Morty", "surname": "Smith", "url": "https://korm.com", "age": 30},
        {"name": "Summer", "surname": "Smith", "url": "https://korm.com", "age": 59},
    ]

@router.get("/users")
async def get_users():
    return users_list

@router.get("/user/{id}")
async def get_user(id: int):
    user = search_user(id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/user/")
async def user_query(id: int):
    user = search_user(id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.post("/user/", response_model=User, status_code=201)
async def create_user(user: User):
    if search_user(user.id) is not None:
        raise HTTPException(status_code=400, detail="User already exists")
    users_list.append(user)
    return user

@router.put("/user/", response_model=User)
async def update_user(user: User):
    user_found = search_user(user.id)
    if user_found is not None:
        users_list.remove(user_found)
        users_list.append(user)
        return user
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.delete("/user/{id}", response_model=User)
async def delete_user(id: int):
    user_found = search_user(id)
    if user_found is not None:
        users_list.remove(user_found)
        return user_found
    else:
        raise HTTPException(status_code=404, detail="User not found")