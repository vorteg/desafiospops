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
    
class Ubicacion(str, Enum):
    VENTANA = "V"
    PASILLO = "P"
  


class Usuario(BaseModel):
    id: Optional[int] = Field(None, alias="id")
    nombre: str = Field(..., max_length=50)
    tipo: TipoUsuario
    profesion: ProfesionUsuario

class Asiento(BaseModel):
    id: Optional[int] = Field(None, alias="id")
    numero: int
    disponible: bool

class Boleto(BaseModel):
    id: Optional[int] = Field(None, alias="id")
    asiento_id: int
    usuario_id: int
    