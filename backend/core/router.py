# backend/core/router.py

from typing import Any, Dict

# Core types
from backend.core.types import OrganOutput

# Core organs
from backend.organs.metabolism.metabolism import MetabolismOrgan
from backend.organs.signaling.signaling import SignalingOrgan
from backend.organs.rhythms.rhythms import RhythmsOrgan
from backend.organs.prediction.prediction import PredictionOrgan
from backend.organs.environment.environment import EnvironmentOrgan
from backend.organs.ecosystem.ecosystem import EcosystemOrgan
from backend.organs.diplomacy.diplomacy import DiplomacyOrgan
from backend.organs.world.world import WorldOrgan
from backend.organs.organism.organism import OrganismOrgan

# New Red/Blue Ops organ
from backend.organs.red_blue_ops.api import RedBlueOps


class Router:
    """
    Central signal router for the LLM_Organism.
    Every signal entering the organism passes through here.
    """

    def __init__(self):
        # Instantiate all organs
        self.organs = {
            "metabolism": MetabolismOrgan(),
            "signaling": SignalingOrgan(),
            "rhythms": RhythmsOrgan(),
            "prediction": PredictionOrgan(),
            "environment": EnvironmentOrgan(),
            "ecosystem": EcosystemOrgan(),
            "diplomacy": DiplomacyOrgan(),
            "world": WorldOrgan(),
            "organism": OrganismOrgan(),

            # New subsystem
            "red_blue_ops": RedBlueOps(),
            "red_team": RedBlueOps().red,
            "blue_team": RedBlueOps().blue,
        }

    def route(self, signal: Dict[str, Any]) -> OrganOutput:
        """
        Routes a signal to the correct organ.
        If no target is specified, defaults to 'organism'.
        """

        if not isinstance(signal, dict):
            raise ValueError("Router received non-dict signal")

        target = signal.get("target", "organism")

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
