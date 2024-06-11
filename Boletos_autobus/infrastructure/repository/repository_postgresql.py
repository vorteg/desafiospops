from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from infrastructure.repository.repository_interface import IRepository
from infrastructure.repository.config import Config

class PostgreSQLRepository(IRepository):
    def __init__(self, config=Config):
        self.engine = create_engine(f"{config.SQLALCHEMY_DATABASE_URI}")
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()
