import os
from pathlib import Path
import shutil

INCOMING = Path("conversation_intake/incoming")

ROUTES = {
    "organ": "backend/organs",
    "agent": "backend/agents",
    "panel": "cockpit/panels",
    "terraform": "cloud/terraform",
    "pipeline": "pipelines/github-actions",
    "core": "backend/core",
    "mind": "backend/mind",
    "api": "backend/api",
}

def classify(filename: str):
    name = filename.lower()

    if "agent" in name:
        return "agent"
    if "panel" in name:
        return "panel"
    if name.endswith(".tf"):
        return "terraform"
    if "pipeline" in name or "ci" in name:
        return "pipeline"
    if "organ" in name:
        return "organ"
    if "memory" in name or "reasoning" in name:
        return "mind"
    if "route" in name:
        return "api"
    return "core"

def main():
    for file in INCOMING.iterdir():
        target_type = classify(file.name)
        target_dir = Path(ROUTES[target_type])

        target_dir.mkdir(parents=True, exist_ok=True)
        shutil.move(str(file), target_dir / file.name)

        print(f"Moved {file.name} → {target_dir}")

if __name__ == "__main__":
    main()
