from core.normalization.normalizer import EventNormalizer

class RCAEngine:
    def __init__(self, dependency_graph):
        self.dependency_graph = dependency_graph
        self.normalizer = EventNormalizer()

    def run(self, events, incident_meta):
        print(f"Running RCA for incident: {incident_meta['incident_id']}")

        normalized_events = self.normalizer.normalize(events)
        print(f"Normalized events: {len(normalized_events)}")

        return normalized_events
