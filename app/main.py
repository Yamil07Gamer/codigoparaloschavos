from fastapi import FastAPI
from app.controllers.router import router as cliente_router

app = FastAPI(title = "API Mecanico")

app.include_router(cliente_router, prefix="/api")

@app.get("/")
def home():
    return{"status": "API Mecánico funcionando en WSL"}