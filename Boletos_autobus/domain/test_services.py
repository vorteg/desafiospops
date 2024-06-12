import pytest
from domain.services import AsientosService
from infrastructure.repository.repository_postgresql import PostgreSQLRepository
from infrastructure.repository.repository_interface import IRepository
from infrastructure.repository.tables_postgresql import AsientosTable

@pytest.fixture
def repository() -> IRepository:
    return PostgreSQLRepository()

@pytest.fixture
def asientos_service(repository: IRepository):
    return AsientosService(repository)

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