from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict
from .engine import SymbolicExecEngine

router = APIRouter(prefix="/symexec", tags=["SymbolicExecution"])

class SymExecRequest(BaseModel):
    semantics: List[Dict]
    graph: Dict

class SymExecDiffRequest(BaseModel):
    left_semantics: List[Dict]
    right_semantics: List[Dict]
    left_graph: Dict
    right_graph: Dict

@router.post("/analyze")
def analyze(req: SymExecRequest):
    eng = SymbolicExecEngine(req.semantics, req.graph)
    return {"paths": eng.run()}

@router.post("/diff")
def diff(req: SymExecDiffRequest):
    left = SymbolicExecEngine(req.left_semantics, req.left_graph).run()
    right = SymbolicExecEngine(req.right_semantics, req.right_graph).run()
    diff = SymbolicExecEngine([], {}).diff_paths(left, right)
    return {"path_diff": diff}
