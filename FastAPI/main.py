from fastapi import FastAPI
from routers import users, products
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(products.router)
app.include_router(users.router)
app.mount("/static", StaticFiles(directory="static"), name="estatic")

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/url")
async def url():
    return {"url": "https://korn.com"}


# Iniciar el server: uvicorn main:app --reload