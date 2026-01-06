# backend/simulator/sensor_simulator.py

import time
import random
import requests
from datetime import datetime

# -------------------------------------------------
# Configuration
# -------------------------------------------------
API_URL = "http://127.0.0.1:8000/sensors/ingest"

SENSOR_ID = "mast_accelerometer_01"
SENSOR_TYPE = "vibration"
UNIT = "m/s2"

BASELINE_MEAN = 4.5
BASELINE_STD = 0.15

BASELINE_SAMPLES = 10
NORMAL_SAMPLES = 10

ANOMALY_VALUE = 60.0

INTERVAL_SECONDS = 1


# -------------------------------------------------
# Helper functions
# -------------------------------------------------
def send_reading(value: float):
    payload = {
        "sensor_id": SENSOR_ID,
        "sensor_type": SENSOR_TYPE,
        "value": round(value, 3),
        "unit": UNIT,
        "timestamp": datetime.utcnow().isoformat()
    }

    response = requests.post(API_URL, json=payload)
    response.raise_for_status()

    data = response.json()

    print(
        f"[{datetime.utcnow().isoformat()}] "
        f"value={value} | "
        f"anomaly={data['anomaly']['is_anomaly']} | "
        f"z_score={data['anomaly']['z_score']}"
    )


# -------------------------------------------------
# Simulation phases
# -------------------------------------------------
def baseline_phase():
    print("\n--- Baseline phase ---")
    for _ in range(BASELINE_SAMPLES):
        value = random.normalvariate(BASELINE_MEAN, BASELINE_STD)
        send_reading(value)
        time.sleep(INTERVAL_SECONDS)


def normal_operation_phase():
    print("\n--- Normal operation phase ---")
    for _ in range(NORMAL_SAMPLES):
        value = random.normalvariate(BASELINE_MEAN, BASELINE_STD)
        send_reading(value)
        time.sleep(INTERVAL_SECONDS)


def anomaly_phase():
    print("\n--- Anomaly injected ---")
    send_reading(ANOMALY_VALUE)


# -------------------------------------------------
# Main
# -------------------------------------------------
if __name__ == "__main__":
    print("Starting VeleroGuard sensor simulator")

    baseline_phase()
    normal_operation_phase()
    anomaly_phase()

    print("\nSimulation completed")