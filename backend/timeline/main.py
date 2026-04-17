from fastapi import FastAPI

app = FastAPI()

TIMELINE = []

@app.post("/event")
def event(payload: dict):
    TIMELINE.append(payload)
    return {"status": "added", "count": len(TIMELINE)}

@app.get("/timeline")
def get_timeline():
    return {"events": TIMELINE}
