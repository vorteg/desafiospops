import logging
import pytest
from sqlalchemy import text,inspect

logger = logging.getLogger(__name__)

#Smoke: Test DB Connection
@pytest.mark.skip(reason="La conexión a la base de datos ha sido verificada.")
def test_db_connection(db_session):
    result = db_session.execute(text('SELECT version();'))
    version_info = result.fetchone()
    logger.info("Hola desde Tests")
    logger.info(f"\n Esta es la version: {version_info[0]}")
    assert result is not None, "La conexión a la base de datos falló"
    
def test_create_tables(db_session):
    inspector = inspect(db_session.bind)
    tables = inspector.get_table_names()
    assert 'usuarios' in tables, "La tabla 'usuarios' no existe en la base de datos"
    assert 'asientos' in tables, "La tabla 'asientos' no existe en la base de datos"
    assert 'boletos' in tables, "La tabla 'boletos' no existe en la base de datos"