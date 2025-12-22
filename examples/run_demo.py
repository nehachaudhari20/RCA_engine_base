from core.engine import RCAEngine
from core.utils.data_loader import load_events, load_incident_meta
from core.utils.dependency_loader import load_dependency_graph

if __name__ == "__main__":
    events = load_events("data/raw_events.json")
    incident_meta = load_incident_meta("data/incident_meta.json")
    dependency_graph = load_dependency_graph("data/dependency_graph.json")

    engine = RCAEngine(dependency_graph=dependency_graph)
    engine.run(events, incident_meta)
