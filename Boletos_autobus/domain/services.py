# domain/services.py
from domain.models import UbicacionAsiento
from infrastructure.repository.tables_postgresql import AsientosTable
from infrastructure.repository.repository_interface import IRepository
from string import ascii_uppercase



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