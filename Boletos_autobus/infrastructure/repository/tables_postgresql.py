from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import declarative_base
from domain.models import TipoUsuario, ProfesionUsuario, UbicacionAsiento

Base = declarative_base()

class UsuariosTable(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True,  autoincrement=True)
    nombre = Column(String(50))
    tipo = Column(Enum(TipoUsuario))
    profesion = Column(Enum(ProfesionUsuario))
    boleto_id = Column(Integer, ForeignKey('boletos.id'), nullable=True) 

class AsientosTable(Base):
    __tablename__ = 'asientos'
    id = Column(Integer, primary_key=True,  autoincrement=True)
    numero = Column(Integer)
    fila = Column(String(1))
    disponible = Column(Boolean)
    ubicacion = Column(Enum(UbicacionAsiento))

class BoletosTable(Base):
    __tablename__ = 'boletos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    asiento_id = Column(Integer, ForeignKey('asientos.id'))
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
   