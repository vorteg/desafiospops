from domain.services import BoletosService, AsientosService,UsuariosService
from domain.models import Boleto
from infrastructure.repository.repository_interface import IRepository

def verificar_disponibilidad(repository:IRepository, asiento_id:int) -> bool:
    asientos = AsientosService(repository)
    return asientos.disponibilidad(asiento_id)

def comprar_boleto(repository:IRepository, usuario_id:int, asiento_id:int) -> bool:
  boleto_service =  BoletosService(repository)
  asiento_disponible = verificar_disponibilidad(repository,asiento_id)
  if asiento_disponible:
    boleto = Boleto(id = None,asiento_id=asiento_id, usuario_id=usuario_id)
    boleto_service.crear_boleto(boleto)
    return True
  return False
     