from fastapi import FastAPI

app = FastAPI()

@app.post("/align")
def align(payload: dict):
    text = payload["text"]
    aligned = text.strip().lower()
    return {"aligned_text": aligned}
