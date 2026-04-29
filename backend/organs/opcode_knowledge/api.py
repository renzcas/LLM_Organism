from fastapi import APIRouter
from pydantic import BaseModel
from .engine import OpcodeKnowledge

router = APIRouter(prefix="/opcodes", tags=["OpcodeKnowledge"])
db = OpcodeKnowledge()

class Lookup(BaseModel):
    mnemonic: str
    mode: str = "x86_64"

@router.post("/lookup")
def lookup(q: Lookup):
    return {"results": db.lookup(q.mnemonic, q.mode)}

class Normalize(BaseModel):
    ida: str

@router.post("/normalize")
def normalize(q: Normalize):
    return {"canonical": db.normalize_ida(q.ida)}

@router.get("/demo")
def demo():
    # Hard-coded example: show cmp
    return {"results": db.lookup("cmp", "x86_64")}
