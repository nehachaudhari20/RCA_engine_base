from dataclasses import dataclass
from typing import List

@dataclass
class Pattern:
    pattern_id: str
    pattern_type: str  # temporal | correlation | dependency
    description: str
    confidence: float
    supporting_event_ids: List[str]
