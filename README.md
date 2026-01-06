# VeleroGuard-AI
**Offline-first predictive monitoring system for sailing vessels using IoT sensors and Edge AI**

---

## 🚢 Overview

VeleroGuard AI is an open-source project focused on designing and implementing a **predictive monitoring system for sailing vessels**.  
It combines **IoT sensor data**, **edge-based machine learning**, and **real-time dashboards** to detect anomalies and anticipate potential structural, mechanical, and environmental failures during navigation.

The system is designed to operate reliably in **low-connectivity maritime environments**, prioritizing **offline-first operation**, low latency, and energy efficiency.

---

## 🎯 Project Goals

- Detect abnormal behavior in critical vessel components (mast, hull, rigging, mechanical systems)
- Provide early warnings and predictive alerts to support safer navigation
- Explore Edge AI patterns for safety-critical, resource-constrained environments
- Offer a clean, intuitive interface for non-technical users (captains and crew)

---

## 🧠 Key Features (MVP)

### Implemented / In Progress
- Real-time IoT data ingestion via MQTT
- Sensor data simulation (no physical hardware required)
- Backend API built with FastAPI
- Basic anomaly detection on time-series data
- Multi-level alert logic (informational, warning, warning, critical)
- Web-based dashboard for visualization

### Planned
- Predictive maintenance models (remaining useful life estimation)
- Offline data persistence and synchronization
- Mobile application (React Native)
- Integration with marine standards (NMEA 0183/2000)
- Support for real hardware sensors (Raspberry Pi + ESP32)

---

## 🏗️ System Architecture (High Level)

```text
[Sensor Simulator / IoT Devices]
            ↓ (MQTT)
      [Ingestion Service]
            ↓
     [Preprocessing Layer]
            ↓
        [Edge AI Engine]
            ↓
       [Alert Manager]
            ↓
      [Web Dashboard]


---

## 🛠️ Tech Stack

### Backend
- Python
- FastAPI
- MQTT (Mosquitto / public brokers for development)
- Scikit-learn (anomaly detection)
- InfluxDB (planned, time-series storage)
- Redis (planned, real-time alerts/cache)

### Frontend
- Web dashboard (React – planned structure)
- Real-time updates via WebSockets

### DevOps / Tooling
- Docker & Docker Compose
- GitHub for version control and collaboration

---

## 📁 Project Structure

```text
VeleroGuard-AI/
│
├── backend/          # FastAPI backend, AI logic, MQTT ingestion
├── frontend/         # Web dashboard (MVP)
├── docs/             # Architecture, API docs, hardware notes
├── data/             # Sample datasets and simulations
└── README.md


## 🚧 Project Status

> **Early-stage MVP / Proof of Concept**

This project is under active development.  
Initial focus is on **architecture, data flow, and anomaly detection**, before expanding into predictive models and hardware integration.

---

## 🗺️ Roadmap

### Phase 1 — MVP
- Sensor simulation
- Real-time ingestion
- Basic anomaly detection
- Web dashboard

### Phase 2
- Predictive models
- Offline-first data synchronization
- Mobile app (React Native)
- Marine system integration (NMEA)

### Phase 3
- Advanced AI models
- Hardware sensor nodes
- Assisted navigation integrations
- Model marketplace per vessel type

---

## 🤝 Contributing

Contributions, feedback, and ideas are welcome.  
Feel free to open an issue or submit a pull request.

---

## 📄 License

MIT License

---

### 👤 Author

Developed as a personal project to demonstrate skills in **software architecture, IoT systems, edge AI, and full-stack development**.

If you’re interested in maritime technology, AI, or safety-critical systems, feel free to connect on LinkedIn.