import pytest
from backend.organs.attention import AttentionOrgan
from backend.organs.symbolic import SymbolicOrgan
from backend.organs.decision import DecisionOrgan
from backend.organs.memory import MemoryOrgan
from backend.organs.pipeline import PipelineOrgan
from backend.organs.hive import HiveRegistry
from backend.organs.organism import Organism

def test_attention():
    organ = AttentionOrgan()
    result = organ.compute({"inputs": [1, 2, 3]})
    assert "weights" in result

def test_symbolic():
    organ = SymbolicOrgan()
    result = organ.compute({"tokens": ["a", "b", "c"], "mode": "pairs"})
    assert len(result["symbols"]) == 2

def test_decision():
    organ = DecisionOrgan()
    result = organ.compute({"symbols": [1, 2, 3], "policy": "max"})
    assert result["action"] == 3

def test_memory_store_and_retrieve():
    organ = MemoryOrgan()
    organ.store({"type": "episodic", "data": "event"})
    out = organ.retrieve({"type": "episodic"})
    assert "event" in out["episodic"]

def test_pipeline():
    organism = Organism()
    organ = PipelineOrgan()
    result = organ.run({
        "steps": [
            {"organ": "attention", "method": "compute", "payload": {"inputs": [1,2,3]}},
            {"organ": "symbolic", "method": "compute", "payload": {"tokens": ["a","b","c"]}}
        ]
    }, organism)
    assert len(result["results"]) == 2

def test_hive():
    organ = HiveRegistry()
    organ.register({"id": "node1", "metadata": {"role": "worker"}})
    out = organ.list()
    assert "node1" in out["members"]
