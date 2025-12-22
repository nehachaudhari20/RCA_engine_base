from dataclasses import dataclass
from typing import Dict, Any
from datetime import datetime

@dataclass
class Event:
    event_id: str
    timestamp: datetime
    entity_id: str
    event_type: str
    source: str
    attributes: Dict[str, Any]
