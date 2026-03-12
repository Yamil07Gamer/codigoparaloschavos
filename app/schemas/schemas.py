from pydantic import BaseModel
from typing import Optional

class ClienteSchema(BaseModel):
    nombre: str
    telefono: Optional[str] = None
    email: Optional[str] = None

class VehiculoSchema(BaseModel):
    placa: str
    marca: str
    modelo: str
    cliente_id: int