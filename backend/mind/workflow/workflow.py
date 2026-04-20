from fastapi import FastAPI
import httpx

app = FastAPI()

SERVICE_URLS = {
    "reasoning": "http://reasoning:8000",
    "alignment": "http://alignment:8000",
    "memory": "http://memory:8000",
    "graph": "http://cognitive_graph:8000",
    "heatmaps": "http://heatmaps:8000",
    "timeline": "http://timeline:8000",
}

@app.post("/run")
async def run_pipeline(payload: dict):
    prompt = payload["prompt"]

    async with httpx.AsyncClient() as client:

        # 1. Reasoning
        reasoning_res = await client.post(
            f"{SERVICE_URLS['reasoning']}/reason",
            json={"prompt": prompt}
        )
        reasoning = reasoning_res.json()

        # 2. Alignment
        alignment_res = await client.post(
            f"{SERVICE_URLS['alignment']}/align",
            json={"text": reasoning["reasoning"]}
        )
        aligned = alignment_res.json()

        # 3. Memory
        await client.post(
            f"{SERVICE_URLS['memory']}/store",
            json={"text": aligned["aligned_text"]}
        )

        # 4. Graph
        graph_res = await client.post(
            f"{SERVICE_URLS['graph']}/build",
            json={"reasoning": reasoning["reasoning"]}
        )
        graph = graph_res.json()

        # 5. Heatmap
        heatmap_res = await client.post(
            f"{SERVICE_URLS['heatmaps']}/heatmap",
            json={"tokens": prompt.split()}
        )
        heatmap = heatmap_res.json()

        # 6. Timeline
        timeline_res = await client.post(
            f"{SERVICE_URLS['timeline']}/event",
            json={
                "prompt": prompt,
                "reasoning": reasoning["reasoning"],
                "aligned": aligned["aligned_text"]
            }
        )
        timeline = timeline_res.json()

    return {
        "final_output": aligned["aligned_text"],
        "attention": reasoning["attention"],
        "graph": graph,
        "heatmap": heatmap,
        "timeline": timeline
    }
