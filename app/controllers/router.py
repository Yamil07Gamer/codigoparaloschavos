from fastapi import APIRouter, HTTPException
from app.schemas.schemas import ClienteSchema
from app.models.queries import ClienteModel

router = APIRouter()

@router.post("/clientes/")
def crear_cliente(cliente: ClienteSchema):
    cliente_id = ClienteModel.crear(cliente)
    return {"message": "Cliente creado", "id": cliente_id}

@router.get("/clientes/")
def obtener_clientes():
    return ClienteModel.listar_todos()