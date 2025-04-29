from pydantic import BaseModel, Field
from typing import Optional

# Modelo para representar una película
class usuario(BaseModel):
    id: int
    nombre: str = Field(..., min_length=1, max_length=50)
    

# Modelo para la respuesta simplificada de una película
class usuariorespuesta(BaseModel):
    nombre: str
    id: str
