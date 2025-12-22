from dataclasses import dataclass
from typing import List

@dataclass
class RankedRootCause:
    rank: int
    hypothesis_id: str
    confidence: float
    summary: str

@dataclass
class RCAResult:
    incident_id: str
    ranked_root_causes: List[RankedRootCause]
    llm_explanation: str
