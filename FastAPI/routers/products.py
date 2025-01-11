# Iniciar el server: uvicorn products:app --reload
from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"], responses={404: {"description": "Not found"}})

product_list = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Mouse", "price": 20},
    {"id": 3, "name": "Keyboard", "price": 50},
]

@router.get("/")
async def get_products():
    return product_list

@router.get("/{id}")
async def get_product(id: int):
    return product_list[id]