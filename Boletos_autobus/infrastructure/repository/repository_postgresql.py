from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session
from infrastructure.repository.repository_interface import IRepository
from infrastructure.repository.config import Config
from typing import Any, Dict, List

class PostgreSQLRepository(IRepository):
    def __init__(self, config=Config):
        self.engine = create_engine(f"{config.SQLALCHEMY_DATABASE_URI}")
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return scoped_session(self.Session)

    def get_data(self, table: Any, id: int) -> Any:
        session = self.get_session()
        try:
            return session.query(table).filter_by(id=id).first()
        finally:
            session.close()

    def get_data_by(self, table: Any, filters: Dict[str, Any]) -> List[Any]:
        session = self.get_session()
        try:
            return session.query(table).filter_by(**filters).all()
        finally:
            session.close()

    def create_data(self, table: Any, data: Dict[str, Any]) -> Any:
        session = self.get_session()
        try:
            new_record = table(**data)
            session.add(new_record)
            session.commit()
            session.refresh(new_record)
            return new_record
        finally:
            session.close()

    def update_data(self, table: Any, id: int, data: Dict[str, Any]) -> Any:
        session = self.get_session()
        try:
            record = session.query(table).filter_by(id=id).first()
            for key, value in data.items():
                setattr(record, key, value)
            session.commit()
            return record
        finally:
            session.close()

    def update_data_by(self, table: Any, filters: Dict[str, Any], data: Dict[str, Any]) -> Any:
        session = self.get_session()
        try:
            record = session.query(table).filter_by(**filters).first()
            for key, value in data.items():
                setattr(record, key, value)
            session.commit()
            return record
        finally:
            session.close()

    def delete_all_data(self, table: Any) -> None:
        session = self.get_session()
        try:
            session.query(table).delete()
            session.execute(text(f"TRUNCATE TABLE {table.__tablename__} RESTART IDENTITY CASCADE"))
            session.commit()
        finally:
            session.close()

    def delete_all_data_by(self, table: Any, filters: Dict[str, Any]) -> None:
        session = self.get_session()
        try:
            session.query(table).filter_by(**filters).delete()
            session.commit()
        finally:
            session.close()