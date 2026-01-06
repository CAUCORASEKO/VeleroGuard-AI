# backend/app/main.py

from fastapi import FastAPI
from datetime import datetime

app = FastAPI(
    title="VeleroGuard AI",
    description="Offline-first predictive monitoring backend for sailing vessels",
    version="0.1.0"
)

@app.get("/health", tags=["System"])
def health_check():
    """
    Basic health check endpoint.
    Used to verify that the backend is running.
    """
    return {
        "status": "ok",
        "service": "veleroguard-backend",
        "timestamp": datetime.utcnow().isoformat()
    }


@app.get("/", tags=["System"])
def root():
    return {
        "message": "VeleroGuard AI backend is running"
    }