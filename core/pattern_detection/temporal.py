from collections import defaultdict
from typing import List
import uuid

from core.schemas.normalized_event import NormalizedEvent
from core.schemas.pattern import Pattern


class TemporalPatternDetector:
    def detect(self, events: List[NormalizedEvent]) -> List[Pattern]:
        patterns = []
        grouped = defaultdict(list)

        for e in events:
            grouped[e.entity].append(e)

        for entity, evs in grouped.items():
            if len(evs) >= 2:
                patterns.append(
                    Pattern(
                        pattern_id=str(uuid.uuid4()),
                        pattern_type="temporal",
                        description=f"Multiple failures detected close in time for {entity}",
                        confidence=min(1.0, 0.3 * len(evs)),
                        supporting_event_ids=[
                            e.normalized_event_id for e in evs
                        ],
                    )
                )

        return patterns
