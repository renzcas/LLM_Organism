# backend/core/router.py

from typing import Any, Dict

# Core types
from backend.core.types import OrganOutput

# Body organs
from backend.organs.metabolism.metabolism import MetabolismOrgan
from backend.organs.signaling.signaling import SignalingOrgan
from backend.organs.rhythms.rhythms import RhythmsOrgan
from backend.organs.prediction.prediction import PredictionOrgan
from backend.organs.environment.environment import EnvironmentOrgan
from backend.organs.ecosystem.ecosystem import EcosystemOrgan
from backend.organs.diplomacy.diplomacy import DiplomacyOrgan
from backend.organs.world.world import WorldOrgan
from backend.organs.organism.organism import OrganismOrgan

# Red/Blue Ops
from backend.organs.red_blue_ops.api import RedBlueOps

# Mind subsystems
from backend.mind.field_matrix.field_matrix import FieldMatrix
from backend.mind.neural_spine.neural_spine import NeuralSpine
from backend.mind.cognitive_graph.graph_engine import CognitiveGraphEngine
from backend.mind.conscious_agent.core import ConsciousAgentCore
from backend.mind.cortex_bridge.bridge import CortexBridge


class Router:
    """
    Central signal router for the LLM_Organism.
    """

    def __init__(self):
        self.organs = {
            # Body
            "metabolism": MetabolismOrgan(),
            "signaling": SignalingOrgan(),
            "rhythms": RhythmsOrgan(),
            "prediction": PredictionOrgan(),
            "environment": EnvironmentOrgan(),
            "ecosystem": EcosystemOrgan(),
            "diplomacy": DiplomacyOrgan(),
            "world": WorldOrgan(),
            "organism": OrganismOrgan(),

            # Red/Blue Ops
            "red_blue_ops": RedBlueOps(),
            "red_team": RedBlueOps().red,
            "blue_team": RedBlueOps().blue,

            # Mind subsystems
            "field_matrix": FieldMatrix(),
            "neural_spine": NeuralSpine(),
            "cognitive_graph_engine": CognitiveGraphEngine(),
            "conscious_agent_core": ConsciousAgentCore(),
            "cortex_bridge": CortexBridge(),
        }

    def route(self, signal: Dict[str, Any]) -> OrganOutput:
        """
        Routes a signal to the correct organ.
        """

        if not isinstance(signal, dict):
            raise ValueError("Router received non-dict signal")

        target = signal.get("target", "conscious_agent_core")

        # Reflex fast-path
        if target == "reflex":
            return self.organs["neural_spine"].run(signal)

        organ = self.organs.get(target)
        if organ is None:
            return OrganOutput(
                organ="router",
                state=None,
                data={
                    "error": f"Unknown organ '{target}'",
                    "available_organs": list(self.organs.keys())
                }
            )

        return organ.run(signal)
