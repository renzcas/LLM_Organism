from fastapi import APIRouter
from backend.organs.organism import Organism
from backend.organs.network_intel.api import router as network_intel_router

# Initialize organism (loads all organs from organs.json)
organism = Organism()

# Main router for all organ endpoints
router = APIRouter()

# ---------------------------------------------------------
# Include Network Intelligence Organ (NEW)
# ---------------------------------------------------------
router.include_router(network_intel_router)

# ---------------------------------------------------------
# Attention Organ Endpoints
# ---------------------------------------------------------
@router.post("/attention/compute")
async def attention_compute(payload: dict):
    organ = organism.get("attention")
    if not organ:
        return {"error": "AttentionOrgan not loaded"}
    return organ.compute(payload)

@router.get("/attention/health")
async def attention_health():
    organ = organism.get("attention")
    if not organ:
        return {"error": "AttentionOrgan not loaded"}
    return organ.health()

# ---------------------------------------------------------
# Organism Health Endpoint
# ---------------------------------------------------------
@router.get("/organism/health")
async def organism_health():
    return organism.health()

# ---------------------------------------------------------
# Symbolic Organ Endpoints
# ---------------------------------------------------------
@router.post("/symbolic/compute")
async def symbolic_compute(payload: dict):
    organ = organism.get("symbolic")
    if not organ:
        return {"error": "SymbolicOrgan not loaded"}
    return organ.compute(payload)

@router.get("/symbolic/health")
async def symbolic_health():
    organ = organism.get("symbolic")
    if not organ:
        return {"error": "SymbolicOrgan not loaded"}
    return organ.health()

# ---------------------------------------------------------
# Decision Organ Endpoints
# ---------------------------------------------------------
@router.post("/decision/compute")
async def decision_compute(payload: dict):
    organ = organism.get("decision")
    if not organ:
        return {"error": "DecisionOrgan not loaded"}
    return organ.compute(payload)

@router.get("/decision/health")
async def decision_health():
    organ = organism.get("decision")
    if not organ:
        return {"error": "DecisionOrgan not loaded"}
    return organ.health()

# ---------------------------------------------------------
# Memory Organ Endpoints
# ---------------------------------------------------------
@router.post("/memory/store")
async def memory_store(payload: dict):
    organ = organism.get("memory")
    if not organ:
        return {"error": "MemoryOrgan not loaded"}
    return organ.store(payload)

@router.post("/memory/retrieve")
async def memory_retrieve(payload: dict):
    organ = organism.get("memory")
    if not organ:
        return {"error": "MemoryOrgan not loaded"}
    return organ.retrieve(payload)

@router.get("/memory/health")
async def memory_health():
    organ = organism.get("memory")
    if not organ:
        return {"error": "MemoryOrgan not loaded"}
    return organ.health()

# ---------------------------------------------------------
# Pipeline Organ Endpoints
# ---------------------------------------------------------
@router.post("/pipeline/run")
async def pipeline_run(payload: dict):
    organ = organism.get("pipeline")
    if not organ:
        return {"error": "PipelineOrgan not loaded"}
    return organ.run(payload, organism)

@router.get("/pipeline/health")
async def pipeline_health():
    organ = organism.get("pipeline")
    if not organ:
        return {"error": "PipelineOrgan not loaded"}
    return organ.health()

# ---------------------------------------------------------
# Hive Registry Endpoints
# ---------------------------------------------------------
@router.post("/hive/register")
async def hive_register(payload: dict):
    organ = organism.get("hive")
    if not organ:
        return {"error": "HiveRegistry not loaded"}
    return organ.register(payload)

@router.post("/hive/update")
async def hive_update(payload: dict):
    organ = organism.get("hive")
    if not organ:
        return {"error": "HiveRegistry not loaded"}
    return organ.update(payload)

@router.get("/hive/list")
async def hive_list():
    organ = organism.get("hive")
    if not organ:
        return {"error": "HiveRegistry not loaded"}
    return organ.list()
