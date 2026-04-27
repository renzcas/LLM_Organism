from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional, Tuple
import math
import hashlib
import json
import time


# =========================
# NDNA: Neural-Digital Nucleic Architecture
# =========================

@dataclass
class NDNA:
    """
    NDNA = Neural-Digital Nucleic Architecture

    This is the "genome" for an organ/agent/module in the organism.
    It is intentionally generic and serializable so it can be:
    - stored in registry
    - diffed over time
    - used as input to synthesis + complexity engines
    """
    id: str
    name: str
    version: str = "0.1.0"

    # High-level role / phenotype
    role: str = "generic-organ"

    # Structural genes: what this organ is made of
    modules: List[str] = field(default_factory=list)          # python modules, panels, routers, etc.
    interfaces: List[str] = field(default_factory=list)       # API routes, event bus channels, topics
    dependencies: List[str] = field(default_factory=list)     # other NDNA ids or external libs

    # Behavioral genes: how it behaves
    capabilities: List[str] = field(default_factory=list)     # "ingest", "analyze", "render", "route"
    constraints: List[str] = field(default_factory=list)      # "read-only", "no-network", "sandboxed"

    # Signals for cockpit + observability
    telemetry_channels: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)

    # Arbitrary metadata for future evolution
    metadata: Dict[str, Any] = field(default_factory=dict)

    # Integrity + lineage
    created_at: float = field(default_factory=time.time)
    lineage_hash: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def compute_lineage_hash(self) -> str:
        """
        Stable hash of the NDNA content (minus lineage_hash itself).
        This lets you track mutations over time.
        """
        data = self.to_dict().copy()
        data.pop("lineage_hash", None)
        payload = json.dumps(data, sort_keys=True).encode("utf-8")
        h = hashlib.sha256(payload).hexdigest()
        self.lineage_hash = h
        return h

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "NDNA":
        return cls(**data)


# =========================
# Synthesis Engine
# =========================

class SynthesisEngine:
    """
    Takes NDNA + environment context and produces a "synthesized" view:
    - what should be activated
    - which modules should be wired
    - which interfaces should be exposed
    This is the planning layer before actual integration.
    """

    def __init__(self, global_context: Optional[Dict[str, Any]] = None) -> None:
        self.global_context = global_context or {}

    def synthesize(self, ndna: NDNA) -> Dict[str, Any]:
        """
        Produce a synthesis plan for this NDNA.
        This is intentionally simple and mechanical for now.
        """
        # Example: treat tags and capabilities as drivers for activation priority
        priority = self._compute_activation_priority(ndna)
        activation_plan = {
            "id": ndna.id,
            "name": ndna.name,
            "role": ndna.role,
            "version": ndna.version,
            "priority": priority,
            "modules_to_load": ndna.modules,
            "interfaces_to_expose": ndna.interfaces,
            "dependencies": ndna.dependencies,
            "telemetry_channels": ndna.telemetry_channels,
            "constraints": ndna.constraints,
            "tags": ndna.tags,
        }
        return activation_plan

    def _compute_activation_priority(self, ndna: NDNA) -> int:
        """
        Very simple heuristic:
        - more capabilities + more interfaces + more telemetry = higher priority
        - can be replaced later with a proper policy engine
        """
        base = 10
        base += len(ndna.capabilities) * 3
        base += len(ndna.interfaces) * 2
        base += len(ndna.telemetry_channels)
        if "critical" in ndna.tags:
            base += 10
        if "experimental" in ndna.tags:
            base -= 3
        return max(base, 1)


# =========================
# Complexity Calculator
# =========================

@dataclass
class ComplexityReport:
    ndna_id: str
    structural_complexity: float
    interface_complexity: float
    dependency_complexity: float
    behavioral_complexity: float
    total_complexity: float
    details: Dict[str, Any]


class ComplexityCalculator:
    """
    Computes a few simple complexity metrics for an NDNA.
    This is not about "good" or "bad"—just a quantitative feel for:
    - how big
    - how entangled
    - how interface-heavy
    """

    def __init__(self, weights: Optional[Dict[str, float]] = None) -> None:
        self.weights = weights or {
            "structural": 1.0,
            "interface": 1.2,
            "dependency": 1.5,
            "behavioral": 1.3,
        }

    def analyze(self, ndna: NDNA) -> ComplexityReport:
        structural = self._structural_complexity(ndna)
        interface = self._interface_complexity(ndna)
        dependency = self._dependency_complexity(ndna)
        behavioral = self._behavioral_complexity(ndna)

        total = (
            structural * self.weights["structural"]
            + interface * self.weights["interface"]
            + dependency * self.weights["dependency"]
            + behavioral * self.weights["behavioral"]
        )

        details = {
            "modules": len(ndna.modules),
            "interfaces": len(ndna.interfaces),
            "dependencies": len(ndna.dependencies),
            "capabilities": len(ndna.capabilities),
            "constraints": len(ndna.constraints),
            "tags": ndna.tags,
        }

        return ComplexityReport(
            ndna_id=ndna.id,
            structural_complexity=structural,
            interface_complexity=interface,
            dependency_complexity=dependency,
            behavioral_complexity=behavioral,
            total_complexity=total,
            details=details,
        )

    def _structural_complexity(self, ndna: NDNA) -> float:
        # log-like growth with module count
        n = max(len(ndna.modules), 1)
        return math.log2(n + 1)

    def _interface_complexity(self, ndna: NDNA) -> float:
        n = max(len(ndna.interfaces), 1)
        return math.sqrt(n)

    def _dependency_complexity(self, ndna: NDNA) -> float:
        n = max(len(ndna.dependencies), 1)
        return math.log10(n + 9)  # smoother curve

    def _behavioral_complexity(self, ndna: NDNA) -> float:
        n = max(len(ndna.capabilities) + len(ndna.constraints), 1)
        return math.log2(n + 1)


# =========================
# Ecosystem: NDNA-aware Organism Registry + Upgrade Path
# =========================

@dataclass
class EcosystemState:
    """
    Snapshot of the whole organism:
    - all NDNA genomes
    - their synthesis plans
    - their complexity reports
    """
    ndna_registry: Dict[str, NDNA] = field(default_factory=dict)
    synthesis_plans: Dict[str, Dict[str, Any]] = field(default_factory=dict)
    complexity_reports: Dict[str, ComplexityReport] = field(default_factory=dict)


class Ecosystem:
    """
    NDNA-aware ecosystem manager.

    Responsibilities:
    - register NDNA genomes
    - run synthesis engine
    - compute complexity
    - expose a simple upgrade path that the rest of the backend can call
    """

    def __init__(self) -> None:
        self.state = EcosystemState()
        self.synthesis_engine = SynthesisEngine()
        self.complexity_calculator = ComplexityCalculator()

    # ---------- NDNA Registry ----------

    def register_ndna(self, ndna: NDNA) -> None:
        ndna.compute_lineage_hash()
        self.state.ndna_registry[ndna.id] = ndna

    def get_ndna(self, ndna_id: str) -> Optional[NDNA]:
        return self.state.ndna_registry.get(ndna_id)

    def list_ndna(self) -> List[NDNA]:
        return list(self.state.ndna_registry.values())

    # ---------- Synthesis + Complexity ----------

    def synthesize_all(self) -> None:
        for ndna_id, ndna in self.state.ndna_registry.items():
            plan = self.synthesis_engine.synthesize(ndna)
            self.state.synthesis_plans[ndna_id] = plan

    def analyze_all_complexity(self) -> None:
        for ndna_id, ndna in self.state.ndna_registry.items():
            report = self.complexity_calculator.analyze(ndna)
            self.state.complexity_reports[ndna_id] = report

    # ---------- Ecosystem Upgrade ----------

    def full_ecosystem_upgrade(self) -> Dict[str, Any]:
        """
        High-level "upgrade" operation:
        - re-synthesize all NDNA
        - recompute complexity
        - return a summary that can be sent to cockpit / logs / registry
        """
        self.synthesize_all()
        self.analyze_all_complexity()

        summary = {
            "ndna_count": len(self.state.ndna_registry),
            "plans": self.state.synthesis_plans,
            "complexity": {
                ndna_id: {
                    "total": report.total_complexity,
                    "structural": report.structural_complexity,
                    "interface": report.interface_complexity,
                    "dependency": report.dependency_complexity,
                    "behavioral": report.behavioral_complexity,
                    "details": report.details,
                }
                for ndna_id, report in self.state.complexity_reports.items()
            },
        }
        return summary


# =========================
# Convenience: bootstrap a default ecosystem
# =========================

def bootstrap_default_ecosystem() -> Ecosystem:
    """
    Create an Ecosystem with a few example NDNA genomes.
    This is safe to call from FastAPI/Flask startup or a CLI tool.
    """
    eco = Ecosystem()

    # Example: backend core organ
    core_ndna = NDNA(
        id="backend-core",
        name="Backend Core",
        role="core-backend",
        modules=[
            "backend.core.router",
            "backend.core.models",
            "backend.core.services",
        ],
        interfaces=[
            "/health",
            "/intake",
            "/ecosystem/upgrade",
        ],
        dependencies=[
            "database",
            "message_bus",
        ],
        capabilities=[
            "route",
            "intake",
            "status",
        ],
        constraints=[
            "no-direct-user-ui",
        ],
        telemetry_channels=[
            "core.health",
            "core.intake",
        ],
        tags=["critical", "stable"],
    )

    # Example: cockpit organ
    cockpit_ndna = NDNA(
        id="cockpit-panel",
        name="InfoEngine Cockpit",
        role="ui-cockpit",
        modules=[
            "frontend.cockpit",
            "frontend.panels.infoengine",
        ],
        interfaces=[
            "/cockpit",
            "/cockpit/agents",
        ],
        dependencies=[
            "backend-core",
        ],
        capabilities=[
            "render",
            "visualize",
        ],
        constraints=[
            "read-only",
        ],
        telemetry_channels=[
            "cockpit.events",
        ],
        tags=["ui", "experimental"],
    )

    eco.register_ndna(core_ndna)
    eco.register_ndna(cockpit_ndna)

    # Run an initial upgrade so state is populated
    eco.full_ecosystem_upgrade()
    return eco


# Optional: quick manual test when running this file directly
if __name__ == "__main__":
    ecosystem = bootstrap_default_ecosystem()
    summary = ecosystem.full_ecosystem_upgrade()
    print(json.dumps(summary, indent=2))
