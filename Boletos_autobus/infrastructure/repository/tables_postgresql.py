from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from domain.models import TipoUsuario, ProfesionUsuario, Ubicacion

Base = declarative_base()

class UsuarioTable(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(50))
    tipo = Column(Enum(TipoUsuario))
    profesion = Column(Enum(ProfesionUsuario))

class AsientoTable(Base):
    __tablename__ = 'asientos'
    id = Column(Integer, primary_key=True)
    numero = Column(Integer)
    fila = Column(String(1))
    disponible = Column(Boolean)
    ubicacion = Column(Enum(Ubicacion))

class BoletoTable(Base):
    __tablename__ = 'boletos'
    id = Column(Integer, primary_key=True)
    asiento_id = Column(Integer, ForeignKey('asientos.id'))
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    tipo = Column(Enum(TipoUsuario))