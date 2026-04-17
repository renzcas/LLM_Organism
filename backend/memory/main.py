from fastapi import FastAPI

app = FastAPI()

MEMORY = []

@app.post("/store")
def store(payload: dict):
    MEMORY.append(payload["text"])
    return {"status": "stored", "count": len(MEMORY)}
