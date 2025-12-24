from core.normalization.normalizer import EventNormalizer
from core.pattern_detection.temporal import TemporalPatternDetector
class RCAEngine:
    def __init__(self, dependency_graph):
        self.dependency_graph = dependency_graph
        self.normalizer = EventNormalizer()
        self.temporal_detector = TemporalPatternDetector()

    def run(self, events, incident_meta):
        normalized_events = self.normalizer.normalize(events)
        temporal_patterns = self.temporal_detector.detect(normalized_events)

        print(f"Temporal patterns: {len(temporal_patterns)}")
        return normalized_events, temporal_patterns
