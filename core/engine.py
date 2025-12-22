from typing import List, Dict
from core.schemas.event import Event

class RCAEngine:
    def __init__(self, dependency_graph: Dict[str, List[str]]):
        self.dependency_graph = dependency_graph

    def run(self, events: List[Event], incident_meta: dict):
        """
        Phase 1: Just accept structured inputs.
        Later phases will add logic here.
        """
        print(f"Running RCA for incident: {incident_meta['incident_id']}")
        print(f"Loaded {len(events)} events")
        print(f"Dependency graph nodes: {list(self.dependency_graph.keys())}")
