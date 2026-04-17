#!/usr/bin/env bash
set -e

echo "🚀 Scaffolding LLM Organism in CURRENT FOLDER..."

#############################################
# 0. Ensure we are NOT inside scripts/
#############################################

if [[ "$PWD" == *"/scripts"* ]]; then
  echo "❌ ERROR: Do NOT run this script from inside the scripts folder."
  echo "Run it from the repo root:"
  echo "   cd /workspaces/LLM_Organism"
  echo "   ./scripts/scaffold.sh"
  exit 1
fi

#############################################
# 1. Create backend structure
#############################################

echo "📁 Creating backend services..."

services=(
  reasoning
  alignment
  memory
  cognitive_graph
  heatmaps
  timeline
  workflow
)

mkdir -p backend

for svc in "${services[@]}"; do
  mkdir -p backend/$svc
  cat > backend/$svc/main.py <<EOF
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"service": "$svc", "status": "ok"}
EOF

  cat > backend/$svc/Dockerfile <<EOF
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn httpx numpy
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
EOF
done

#############################################
# 2. Create cockpit
#############################################

echo "🖥 Creating cockpit UI..."

mkdir -p cockpit
cd cockpit
npm create vite@latest . -- --template react-ts
npm install react-force-graph react-heatmap-grid
cd ..

#############################################
# 3. docker-compose.yml
#############################################

cat > docker-compose.yml <<EOF
version: "3.9"
services:
  workflow:
    build: ./backend/workflow
    ports: ["8000:8000"]
  reasoning:
    build: ./backend/reasoning
    ports: ["8001:8000"]
  alignment:
    build: ./backend/alignment
    ports: ["8002:8000"]
  memory:
    build: ./backend/memory
    ports: ["8003:8000"]
  cognitive_graph:
    build: ./backend/cognitive_graph
    ports: ["8004:8000"]
  heatmaps:
    build: ./backend/heatmaps
    ports: ["8005:8000"]
  timeline:
    build: ./backend/timeline
    ports: ["8006:8000"]
EOF

#############################################
# 4. Makefile
#############################################

cat > Makefile <<EOF
build:
\tdocker compose build

up:
\tdocker compose up

down:
\tdocker compose down

clean:
\tdocker compose down -v
EOF

#############################################
# 5. README
#############################################

cat > README.md <<EOF
# LLM Organism Minimal Slice
EOF

#############################################
# 6. Git init
#############################################

git add .
git commit -m "Initial scaffold"

echo "🎉 Scaffold complete in repo root!"
