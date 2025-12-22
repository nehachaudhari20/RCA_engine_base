from dataclasses import dataclass
from typing import Dict, List
from datetime import datetime

@dataclass
class NormalizedEvent:
    normalized_event_id: str
    entity: str
    failure_type: str
    severity: str
    time_window_start: datetime
    time_window_end: datetime
    dimensions: Dict[str, str]
    raw_event_ids: List[str]
