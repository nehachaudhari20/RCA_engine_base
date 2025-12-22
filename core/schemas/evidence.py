from dataclasses import dataclass
from typing import List

@dataclass
class Evidence:
    hypothesis_id: str
    temporal_alignment: float
    correlation_strength: float
    causal_proximity: float
    signal_confidence: float
    facts: List[str]
