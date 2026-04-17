from fastapi import FastAPI
import random

app = FastAPI()

@app.post("/reason")
def reason(payload: dict):
    prompt = payload["prompt"]

    tokens = prompt.split()
    n = len(tokens)

    # Fake reasoning
    reasoning = f"I analyzed the prompt: {prompt}. Here is a mock reasoning chain."

    # Fake attention matrix
    attention = [[random.random() for _ in range(n)] for _ in range(n)]

    return {
        "reasoning": reasoning,
        "attention": attention
    }
