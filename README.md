# LLM_Organism

A modular, multi-organism architecture combining physics engines and cognitive organs.

## Structure

- `backend/organs/`
  - `attention.py`
  - `symbolic.py`
  - `decision.py`
  - `memory.py`
  - `pipeline.py`
  - `hive.py`
  - `organism.py`
- `backend/api/router.py`
- `frontend/`
  - `panels/`
  - `main.js`
- `backend/tests/test_organs.py`

## Cognitive Organs

- **AttentionOrgan**: salience, weighting, gating  
- **SymbolicOrgan**: pairs, triples, graph structures  
- **DecisionOrgan**: policy-based action selection  
- **MemoryOrgan**: episodic + semantic storage  
- **PipelineOrgan**: multi-step reasoning chains  
- **HiveRegistry**: multi-organism coordination  

## Running

- Start backend (FastAPI + Uvicorn)
- Serve frontend (Vite/webpack/dev server)
- Visit cockpit UI to interact with organs.
