from adapters.base import DatasetAdapter
from core.normalization.normalizer import EventNormalizer
from core.pattern_detection.temporal_basic import TemporalPatternDetector
from core.pattern_detection.correlation_basic import CorrelationPatternDetector
from core.pattern_detection.dependency_basic import DependencyAnalyzer


class RCAEngine:
    def __init__(self, adapter: DatasetAdapter):
        self.adapter = adapter
        self.normalizer = EventNormalizer()
        self.pattern_detectors = [
            TemporalPatternDetector(),
            CorrelationPatternDetector(),
        ]

    def run(self):
        events = self.adapter.load_events()
        dependency_graph = self.adapter.load_dependency_graph()
        incident_meta = self.adapter.load_incident_meta()

        normalized_events = self.normalizer.normalize(events)

        patterns = []
        for detector in self.pattern_detectors:
            patterns.extend(detector.detect(normalized_events))

        print(f"Incident: {incident_meta['incident_id']}")
        print(f"Normalized events: {len(normalized_events)}")
        print(f"Detected patterns: {len(patterns)}")

        return normalized_events, patterns
