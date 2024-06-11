import logging
import pytest
from sqlalchemy import text

logger = logging.getLogger(__name__)

@pytest.mark.skip(reason="La conexión a la base de datos ha sido verificada.")
def test_db_connection(db_session):
    result = db_session.execute(text('SELECT version();'))
    version_info = result.fetchone()
    logger.info("Hola desde Tests")
    logger.info(f"\n Esta es la version: {version_info[0]}")
    assert result is not None, "La conexión a la base de datos falló"