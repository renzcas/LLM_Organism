from fastapi import FastAPI

app = FastAPI()

@app.post("/build")
def build(payload: dict):
    reasoning = payload["reasoning"]
    tokens = reasoning.split()

    nodes = [{"id": i, "type": "token", "label": t} for i, t in enumerate(tokens)]
    edges = [{"source": i, "target": i+1, "relation": "next"} for i in range(len(tokens)-1)]

    return {"nodes": nodes, "edges": edges}
