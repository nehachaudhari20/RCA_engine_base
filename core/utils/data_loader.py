import json
from datetime import datetime
from typing import List
from core.schemas.event import Event

def load_events(path: str) -> List[Event]:
    with open(path, "r") as f:
        raw_events = json.load(f)

    events = []
    for e in raw_events:
        events.append(
            Event(
                event_id=e["event_id"],
                timestamp=datetime.fromisoformat(
                    e["timestamp"].replace("Z", "+00:00")
                ),
                entity_id=e["entity_id"],
                event_type=e["event_type"],
                source=e["source"],
                attributes=e["attributes"],
            )
        )

    return events

def load_incident_meta(path: str) -> dict:
    with open(path, "r") as f:
        return json.load(f)
