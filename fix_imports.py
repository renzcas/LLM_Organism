import os
import re

ROOT = "backend"

REWRITE_MAP = {
    r"from engine": "from backend.core.engine",
    r"from router": "from backend.core.router",
    r"from types": "from backend.core.types",
    r"from loop": "from backend.core.loop",

    r"from metabolism": "from backend.organs.metabolism.metabolism",
    r"from rhythms": "from backend.organs.rhythms.rhythms",
    r"from prediction": "from backend.organs.prediction.prediction",
    r"from signaling": "from backend.organs.signaling.signaling",
    r"from diplomacy": "from backend.organs.diplomacy.diplomacy",
    r"from environment": "from backend.organs.environment.environment",
    r"from world": "from backend.organs.world.world",
    r"from ecosystem": "from backend.organs.ecosystem.ecosystem",
    r"from organism": "from backend.organs.organism.organism",

    r"from identity": "from backend.mind.identity.identity",
    r"from memory": "from backend.mind.memory.memory",
    r"from reasoning": "from backend.mind.reasoning.reasoning",
    r"from timeline": "from backend.mind.timeline.timeline",
    r"from workflow": "from backend.mind.workflow.workflow",
    r"from cognitive_graph": "from backend.mind.cognitive_graph.cognitive_graph",

    r"from routes": "from backend.api.routes.routes",
    r"from alignment": "from backend.api.alignment.alignment",
}

def rewrite_file(path):
    with open(path, "r") as f:
        content = f.read()

    original = content
    for pattern, replacement in REWRITE_MAP.items():
        content = re.sub(pattern, replacement, content)

    if content != original:
        with open(path, "w") as f:
            f.write(content)
        print(f"Updated imports in {path}")

for root, dirs, files in os.walk(ROOT):
    for file in files:
        if file.endswith(".py"):
            rewrite_file(os.path.join(root, file))
