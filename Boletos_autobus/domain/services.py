# domain/services.py
from domain.models import UbicacionAsiento,Usuario, Boleto
from infrastructure.repository.tables_postgresql import AsientosTable, UsuariosTable, BoletosTable
from infrastructure.repository.repository_interface import IRepository
from string import ascii_uppercase
from typing import Dict



class AsientosService:
    def __init__(self,repository: IRepository) -> None:
        self.repository = repository
        
    def generar_asientos_disponibles(self, numero_de_asientos: int) -> None:
        # Borrar todos los datos existentes de AsientoTable
        self.repository.delete_all_data(AsientosTable)

        # Crear nuevos asientos
        for i in range(1, numero_de_asientos + 1):
            fila = ascii_uppercase[(i - 1) // 4]
            ubicacion = UbicacionAsiento.PASILLO if i % 2 == 0 else UbicacionAsiento.VENTANA
            asiento_data = {
                'numero': i,
                'disponible': True,
                'ubicacion': ubicacion,
                'fila': fila
            }
            self.repository.create_data(AsientosTable, asiento_data)
class UsuariosService:
    def __init__(self,repository: IRepository) -> None:
        self.repository = repository
        
    def crear_usuario(self,user:Usuario):
        self.repository.create_data(table=UsuariosTable,data=user.model_dump())
        
    def obtener_id_usuario_por_nombre(self, nombre: str) -> int:
        usuario = self.repository.get_data_by(table=UsuariosTable, filters={'nombre': nombre})
        if usuario:
            return usuario.id
        else:
            raise ValueError(f"Usuario con nombre {nombre} no encontrado")
    def actualizar_boleto_id(self, filters:Dict, data:Dict):
        self.repository.update_data_by(table=UsuariosTable,filters=filters, data=data)


class BoletosService:
    def __init__(self,repository: IRepository) -> None:
        self.repository = repository
    
    def crear_boleto(self,boleto:Boleto):
        self.repository.create_data(table=BoletosTable,data=boleto.model_dump())
        
    def obtener_boleto_id(self,usuario_id:int) -> int:
        boleto = self.repository.get_data_by(table=BoletosTable,filters={'usuario_id':usuario_id})
        if boleto:
            return boleto.id
        else:
            raise ValueError(f"Usuario con id {usuario_id} no encontrado, en boletos")