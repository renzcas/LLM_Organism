# Dockerfile
FROM python:3.11-slim AS backend

WORKDIR /app
COPY backend/ ./backend/
COPY pyproject.toml poetry.lock* ./  # or requirements.txt

RUN pip install --no-cache-dir fastapi uvicorn[standard] && \
    pip install --no-cache-dir pytest

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
