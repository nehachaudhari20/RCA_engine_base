from abc import ABC, abstractmethod
from typing import List
from core.schemas.normalized_event import NormalizedEvent
from core.schemas.pattern import Pattern

class PatternDetector(ABC):
    @abstractmethod
    def detect(self, events: List[NormalizedEvent]) -> List[Pattern]:
        pass
