from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/url")
async def url():
    return {"url": "https://korn.com"}


# Iniciar el server: uvicorn main:app --reload