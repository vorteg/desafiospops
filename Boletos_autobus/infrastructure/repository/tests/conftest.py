import pytest
from infrastructure.repository.repository_postgresql import PostgreSQLRepository
from infrastructure.repository.config import TestConfig 

@pytest.fixture(scope='module')
def test_db():
    repo = PostgreSQLRepository(config=TestConfig)
    engine = repo.engine
    
    with engine.connect() as con:
        con.exec_driver_sql("CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, name VARCHAR(50));")
    
    yield repo
    
    
    # Eliminar todas las tablas después de las pruebas
    with engine.connect() as con:
        con.exec_driver_sql("DROP TABLE IF EXISTS test;")
        
        

@pytest.fixture(scope='module')
def db_session(test_db):
    session = test_db.get_session()
    yield session
    session.close()