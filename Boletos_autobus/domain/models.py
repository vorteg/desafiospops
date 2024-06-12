# domain/models.py
from pydantic import BaseModel, Field, ConfigDict
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
    id: Optional[int] = Field(None, alias="id")
    nombre: str = Field(..., max_length=50)
    tipo: TipoUsuario
    profesion: ProfesionUsuario
    boleto_id:Optional[int] = Field(None)
    
    model_config = ConfigDict(from_attributes=True)

class Asiento(BaseModel):
    id: Optional[int] = Field(None, alias="id")
    numero: int
    disponible: bool
    ubicacion:UbicacionAsiento
    
    model_config = ConfigDict(from_attributes=True)

class Boleto(BaseModel):
    id: Optional[int] = Field(None, alias="id")
    asiento_id: int
    usuario_id: int
    
    model_config = ConfigDict(from_attributes=True)
    