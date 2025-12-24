from abc import ABC, abstractmethod
from typing import List, Dict
from core.schemas.event import Event

class DatasetAdapter(ABC):
    @abstractmethod
    def load_events(self) -> List[Event]:
        pass

    @abstractmethod
    def load_dependency_graph(self) -> Dict[str, List[str]]:
        pass

    @abstractmethod
    def load_incident_meta(self) -> dict:
        pass
