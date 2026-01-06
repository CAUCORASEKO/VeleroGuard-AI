# backend/app/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional
from collections import defaultdict, deque
import statistics

app = FastAPI(
    title="VeleroGuard AI",
    description="Offline-first predictive monitoring backend for sailing vessels",
    version="0.1.0"
)

# -------------------------------------------------------------------
# In-memory storage (MVP only)
# -------------------------------------------------------------------
sensor_readings: List["SensorReading"] = []

# Sliding window per sensor_id
WINDOW_SIZE = 20
sensor_windows = defaultdict(lambda: deque(maxlen=WINDOW_SIZE))

# -------------------------------------------------------------------
# Pydantic models
# -------------------------------------------------------------------
class SensorReading(BaseModel):
    sensor_id: str = Field(..., example="mast_accelerometer_01")
    sensor_type: str = Field(..., example="vibration")
    value: float = Field(..., example=4.82)
    unit: Optional[str] = Field(default=None, example="m/s2")
    timestamp: datetime = Field(default_factory=datetime.utcnow)


class AnomalyResult(BaseModel):
    is_anomaly: bool
    mean: Optional[float] = None
    std_dev: Optional[float] = None
    z_score: Optional[float] = None
    threshold: float = 3.0


# -------------------------------------------------------------------
# System endpoints
# -------------------------------------------------------------------
@app.get("/", tags=["System"])
def root():
    return {"message": "VeleroGuard AI backend is running"}


@app.get("/health", tags=["System"])
def health_check():
    return {
        "status": "ok",
        "service": "veleroguard-backend",
        "timestamp": datetime.utcnow().isoformat()
    }


# -------------------------------------------------------------------
# Anomaly detection logic (MVP)
# -------------------------------------------------------------------
def detect_anomaly(sensor_id: str, value: float) -> AnomalyResult:
    window = sensor_windows[sensor_id]

    # Not enough data yet
    if len(window) < 5:
        window.append(value)
        return AnomalyResult(is_anomaly=False)

    mean = statistics.mean(window)
    std_dev = statistics.stdev(window)

    if std_dev == 0:
        window.append(value)
        return AnomalyResult(is_anomaly=False, mean=mean, std_dev=std_dev)

    z_score = abs((value - mean) / std_dev)
    is_anomaly = z_score > 3.0

    # Append AFTER evaluation
    window.append(value)

    return AnomalyResult(
        is_anomaly=is_anomaly,
        mean=mean,
        std_dev=std_dev,
        z_score=z_score
    )


# -------------------------------------------------------------------
# Sensor ingestion endpoint
# -------------------------------------------------------------------
@app.post("/sensors/ingest", tags=["Sensors"])
def ingest_sensor_data(reading: SensorReading):
    """
    Ingest a single sensor reading.

    MVP behavior:
    - Validate incoming data
    - Store it in memory
    - Run basic anomaly detection
    """

    if reading.value < 0:
        raise HTTPException(
            status_code=400,
            detail="Sensor value must be non-negative"
        )

    sensor_readings.append(reading)

    anomaly_result = detect_anomaly(
        sensor_id=reading.sensor_id,
        value=reading.value
    )

    response = {
        "status": "accepted",
        "sensor_id": reading.sensor_id,
        "value": reading.value,
        "timestamp": reading.timestamp.isoformat(),
        "anomaly": anomaly_result.dict()
    }

    if anomaly_result.is_anomaly:
        response["alert_level"] = "warning"

    return response


# -------------------------------------------------------------------
# Debug / inspection endpoints (MVP only)
# -------------------------------------------------------------------
@app.get("/sensors/readings", tags=["Sensors"])
def list_sensor_readings():
    """Return all ingested sensor readings."""
    return sensor_readings


@app.get("/sensors/windows", tags=["Sensors"])
def list_sensor_windows():
    """Return current sliding windows per sensor."""
    return {
        sensor_id: list(values)
        for sensor_id, values in sensor_windows.items()
    }