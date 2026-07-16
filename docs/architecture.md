# Enterprise AI FMCG Lakehouse Architecture

## Overview

The Enterprise AI FMCG Lakehouse is an end-to-end enterprise data platform that simulates a real FMCG organization's data ecosystem.

The project generates realistic master data and transactional data for analytics, reporting, machine learning, and forecasting.

---

## High Level Architecture

```
ERP
CRM
POS
Inventory
Marketing
HR
Supplier Portal
IoT
        │
        ▼
Raw Data
        │
        ▼
Bronze Layer
        │
        ▼
Silver Layer
        │
        ▼
Gold Layer
        │
        ▼
Analytics
        │
        ▼
Power BI
DuckDB
ClickHouse
Machine Learning
Forecasting
```

---

## Pipeline Flow

Source Systems

↓

Master Data Generation

↓

Transaction Data Generation

↓

Validation

↓

Metadata Generation

↓

CSV / Parquet

↓

Bronze

↓

Silver

↓

Gold

↓

Analytics

---

## Technology Stack

- Python
- Pandas
- DuckDB
- ClickHouse
- Apache Spark (Future)
- Airflow (Future)
- dbt (Future)
- Power BI
- Streamlit
- Git
- GitHub

---

## Design Principles

- Modular
- Reusable
- Config Driven
- Scalable
- Enterprise Ready