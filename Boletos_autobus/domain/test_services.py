import pytest
from domain.services import AsientosService, UsuariosService, BoletosService
from domain.models import Usuario, TipoUsuario, ProfesionUsuario, Boleto
from infrastructure.repository.repository_postgresql import PostgreSQLRepository
from infrastructure.repository.repository_interface import IRepository
from infrastructure.repository.tables_postgresql import AsientosTable, UsuariosTable, BoletosTable

@pytest.fixture
def repository() -> IRepository:
    return PostgreSQLRepository()

@pytest.fixture
def asientos_service(repository: IRepository):
    return AsientosService(repository)

@pytest.fixture
def usuarios_service(repository: IRepository):
    return UsuariosService(repository)

@pytest.fixture
def boletos_service(repository: IRepository):
    return BoletosService(repository)


def test_generar_asientos_disponibles(asientos_service, repository):
    numero_de_asientos = 10
    asientos_service.generar_asientos_disponibles(numero_de_asientos)

    session = repository.get_session()
    asientos = session.query(AsientosTable).all()
    session.close()

    assert len(asientos) == numero_de_asientos
    for asiento in asientos:
        assert asiento.disponible is True
        assert 1 <= asiento.numero <= numero_de_asientos

def test_disponibilidad_asientos(asientos_service):
    estado_asiento = asientos_service.disponibilidad(1)  
    assert type(estado_asiento) is bool
    
    
def test_actualizar_disponibilidad_asientos(asientos_service, repository):
    asientos_service.actualizar_disponibilidad(1, False)  
    
    session = repository.get_session()
    asiento = session.query(AsientosTable).filter_by(id=1).first()
    session.close()

    assert asiento.disponible is False
        
      
        
def test_crear_usuario(usuarios_service, repository):
    usuario = Usuario(id=None,nombre="Juan Pérez", tipo=TipoUsuario.ADULTO, profesion=ProfesionUsuario.MAESTRO, boleto_id=None)
    usuarios_service.crear_usuario(usuario)

    session = repository.get_session()
    usuario_db = session.query(UsuariosTable).filter_by(nombre="Juan Pérez").first()
    session.close()

    assert usuario_db is not None
    assert usuario_db.nombre == "Juan Pérez"
    
def test_obtener_id_usuario_por_nombre(usuarios_service, repository):
  
    usuario_id = usuarios_service.obtener_id_usuario_por_nombre("Juan Pérez")   
        
    assert usuario_id is not None
    assert usuario_id == 1

#Ideal Test Complentaria, EValua el manejo de errores 
def test_obtener_id_usuario_por_nombre_no_existe(usuarios_service):
    with pytest.raises(ValueError, match="Usuario con nombre .* no encontrado"):
        usuarios_service.obtener_id_usuario_por_nombre("No Existe")
        
        
def test_actualizar_boleto_id(usuarios_service, repository):
    id=1
    boleto_id = 1
    filters = {'id':id}
    data = {"boleto_id":boleto_id}
    # Actualizar el id del boleto en el usuario
    usuarios_service.actualizar_boleto_id(filters,data)

    session = repository.get_session()
    usuario_db = session.query(UsuariosTable).filter_by(id=id).first()
    session.close()

    assert usuario_db is not None
    assert usuario_db.boleto_id == boleto_id
    
def test_crear_boleto(boletos_service, repository):
    boleto = Boleto(id=None, asiento_id=3,usuario_id=1)
    boletos_service.crear_boleto(boleto)

    session = repository.get_session()
    boleto_db = session.query(BoletosTable).filter_by(usuario_id=1).first()
    session.close()

    assert boleto_db is not None
    assert boleto_db.id == 1
    
def test_obtener_boleto_id(boletos_service):
    boleto_id = boletos_service.obtener_boleto_id(usuario_id=1)
    assert boleto_id is not None
    assert boleto_id == 1
    
def test_obtener_boleto_id_no_existe(boletos_service):
    with pytest.raises(ValueError, match="Usuario con id .* no encontrado, en boletos"):
        boletos_service.obtener_boleto_id(usuario_id=50)