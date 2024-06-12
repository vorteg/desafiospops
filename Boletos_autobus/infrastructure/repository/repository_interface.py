from abc import ABC, abstractmethod
from typing import Any, Dict, List

class IRepository(ABC):
    @abstractmethod
    def get_session(self):
        ...
    @abstractmethod
    def get_data(self, table: Any, filters: Dict[str, Any]) -> List[Any]:
        ...
    @abstractmethod
    def get_data_by(self, table: Any, filters: Dict[str, Any]) -> Any:
        ...
    @abstractmethod
    def create_data(self, table: Any, data: Dict[str, Any]) -> Any:
        ...
    @abstractmethod
    def update_data(self, table: Any, id: int, data: Dict[str, Any]) -> Any:
        ...
    @abstractmethod
    def update_data_by(self, table: Any, filters: Dict[str, Any], data: Dict[str, Any]) -> Any:
        ...
        
    @abstractmethod
    def delete_all_data(self, table: Any) -> None:
        ...
        
    @abstractmethod
    def delete_all_data_by(self, table: Any, filters: Dict[str, Any]) -> None:
        ...