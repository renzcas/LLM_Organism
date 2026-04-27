from fastapi import FastAPI
from backend.api.routes import router as api_router

# Create the FastAPI application
app = FastAPI(
    title="LLM Organism Backend",
    description="Backend engine for NDNA, synthesis, complexity, and cockpit data.",
    version="0.1.0"
)

# Attach all API routes (including /ecosystem/upgrade)
app.include_router(api_router)
