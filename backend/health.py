# backend/health.py

import importlib

ORGANS = [
    "backend.organs.metabolism.metabolism",
    "backend.organs.rhythms.rhythms",
    "backend.organs.prediction.prediction",
    "backend.organs.signaling.signaling",
    "backend.organs.diplomacy.diplomacy",
    "backend.organs.environment.environment",
    "backend.organs.world.world",
    "backend.organs.ecosystem.ecosystem",
    "backend.organs.organism.organism",
]

MIND = [
    "backend.mind.identity.identity",
    "backend.mind.memory.memory",
    "backend.mind.reasoning.reasoning",
    "backend.mind.timeline.timeline",
    "backend.mind.workflow.workflow",
    "backend.mind.cognitive_graph.cognitive_graph",
]

CORE = [
    "backend.core.engine",
    "backend.core.router",
    "backend.core.types",
    "backend.core.loop",
]

def check_module(path):
    try:
        module = importlib.import_module(path)
        print(f"[OK] {path}")
        return module
    except Exception as e:
        print(f"[FAIL] {path} — {e}")
        return None

def run_health_check():
    print("\n=== CORE CHECK ===")
    for m in CORE:
        check_module(m)

    print("\n=== ORGAN CHECK ===")
    for m in ORGANS:
        check_module(m)

    print("\n=== MIND CHECK ===")
    for m in MIND:
        check_module(m)

if __name__ == "__main__":
    run_health_check()
