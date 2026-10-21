# 🌐 OmniScope AI

OmniScope AI is an enterprise-grade corporate sustainability engine built to track, calculate, and audit Scope 3 (Value Chain) greenhouse gas emissions. It automates supply chain data collection and maps compliance metrics to meet global disclosure laws like Europe's CSRD and California's SB 253.

## ✨ Key Features
- **🧮 Math Engine:** Mapped directly to GHG Protocol Value Chain standards.
- **📂 Data Ingestion:** Automated pipelines for logistics and ERP data.
- **🛡️ Audit Trails:** Relational tracking history for third-party verifications.

## 🏗️ Architecture Overview
```text
omniscope-ai/
├── backend/       # FastAPI Core Computational Service
├── frontend/      # Next.js Compliance Dashboard
└── data/          # Regulatory Factor Mirrors (JSON/Parquet)
```

## ⚡ Quick Start

### Prerequisites
- Python 3.11+ | Node.js 18+ | PostgreSQL 15+

### 1. Spin Up the Backend Engine
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```
API docs will run at `http://127.0.0`.

### 2. Run Local Validation Test
```bash
python app/engines/GHG_protocol_core.py
```

## 🔒 Security & Licensing
OmniScope AI utilizes transport-layer encryption (TLS 1.3) and Role-Based Access Control (RBAC) to isolate sensitive supplier business metrics. 

This repository operates under a multi-tiered commercial licensing structure. Core data orchestration modules are open-core, while multi-tenant components require corporate enterprise agreements. Contact `licensing@omniscope.ai` for details.
