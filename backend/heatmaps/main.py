from fastapi import FastAPI
import random

app = FastAPI()

@app.post("/heatmap")
def heatmap(payload: dict):
    tokens = payload["tokens"]
    activation = [random.random() for _ in tokens]
    return {"activation": activation}
