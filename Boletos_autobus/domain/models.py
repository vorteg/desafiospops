# domain/models.py
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class TipoUsuario(str, Enum):
    ADULTO = "adulto"
    NINO = "niño"
    ADULTO_MAYOR = "adulto mayor"

class ProfesionUsuario(str, Enum):
    ESTUDIANTE = "estudiante"
    MAESTRO = "maestro"
    NINGUNO = "ninguno"
    
class UbicacionAsiento(str, Enum):
    PASILLO = "pasillo"
    VENTANA = "ventana"
  


class Usuario(BaseModel):
    id: int = Field(...)
    nombre: str = Field(..., max_length=50)
    tipo: TipoUsuario
    profesion: ProfesionUsuario
    boleto_id:Optional[int] = Field(None, alias="id")
    
    class Config:
        orm_mode = True

class Asiento(BaseModel):
    id: int = Field(...)
    numero: int
    disponible: bool
    ubicacion:UbicacionAsiento
    
    class Config:
        orm_mode = True

class Boleto(BaseModel):
    id: int = Field(...)
    asiento_id: int
    usuario_id: int
    
    class Config:
        orm_mode = True
    