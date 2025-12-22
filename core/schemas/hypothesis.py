from dataclasses import dataclass
from typing import List

@dataclass
class Hypothesis:
    hypothesis_id: str
    category: str
    description: str
    generated_by: str  # rules | llm
    related_pattern_ids: List[str]
