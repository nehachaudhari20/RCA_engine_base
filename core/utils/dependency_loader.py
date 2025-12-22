import json
from typing import Dict, List

def load_dependency_graph(path: str) -> Dict[str, List[str]]:
    with open(path, "r") as f:
        return json.load(f)
