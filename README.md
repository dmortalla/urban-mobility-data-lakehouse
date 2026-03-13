# Urban Mobility Data Lakehouse

![Python](https://img.shields.io/badge/Python-3.11-blue)
![status](https://img.shields.io/badge/status-complete-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

A production-style data engineering project that ingests, validates, transforms, and serves NYC taxi trip data through a medallion-style lakehouse pipeline using Python, Pandas, Parquet, DuckDB, and local orchestration.

## Overview

This project builds an analytics-ready data platform for urban mobility data. Raw taxi trip records are processed into Bronze, Silver, and Gold layers so that downstream users can reliably analyze trip volume, demand, payment behavior, and route patterns.

## Business Problem

Raw transportation data is often too messy for direct analytics. A mobility analytics team needs a reproducible pipeline that can:

* ingest large monthly trip files
* preserve raw lineage
* standardize and validate records
* create trusted business-facing marts

This project solves that by implementing a local-first medallion architecture.

## Architecture

High-level medallion architecture used by the pipeline:
```
Raw NYC Taxi Data
        ↓
   Raw Landing
        ↓
     Bronze Layer
        ↓
     Silver Layer
        ↓
     Gold Analytics Tables
        ↓
   DuckDB Analytics Warehouse
```

## Tech Stack

- Python
- Pandas
- DuckDB (analytics warehouse)
- Parquet (lakehouse storage format)
- YAML (pipeline configuration)
- Pytest (testing framework)
- Modular ETL pipeline architecture

## Repository Structure

```text
src/       pipeline and transformation logic
scripts/   pipeline entry points
config/    runtime configuration files
sql/       analytics queries for DuckDB
tests/     unit and validation tests
docs/      architecture notes and screenshots
```

## Reproducibility

The entire pipeline can be reproduced locally using the provided scripts.

```bash
# 1. Clone the repository
git clone https://github.com/dmortalla/urban-mobility-data-lakehouse.git
cd urban-mobility-data-lakehouse

# 2. Create and activate the Python environment
conda create -n lakehouse python=3.11
conda activate lakehouse
pip install -r requirements.txt

# 3. Download the raw dataset
python -m scripts.download_data

# 4. Run the medallion pipeline (Bronze → Silver → Gold)
python -m scripts.run_pipeline

# 5. Load the Gold analytics tables into DuckDB
python -m scripts.load_duckdb

# 6. Run analytics queries
duckdb data/warehouse/analytics.duckdb
.read sql/example_queries.sql
```

## Completed Milestones

✔ **Milestone 1 — Project Scaffolding**
Repository structure, configuration system, and development environment.

✔ **Milestone 2 — Bronze Data Ingestion**
Download NYC taxi parquet datasets and ingest them into the Bronze layer.

✔ **Milestone 3 — Silver Data Transformation**
Clean and standardize Bronze data to create analytics-ready Silver tables.

✔ **Milestone 4 — Gold Analytics Layer**
Generate aggregated business tables including daily demand, hourly demand, and payment-type revenue.

✔ **Milestone 5 — DuckDB Analytics Warehouse**
Load Gold tables into DuckDB to enable SQL-based analytics.

✔ **Milestone 6 — Repository Polish**
Documentation improvements, example SQL queries, architecture explanation, and project presentation.

## Project Status

✔ Pipeline implemented
✔ Tests passing
✔ DuckDB analytics warehouse available
✔ Example SQL queries included

## How to Run

### 1 Install dependencies

```bash
make install
```

### 2 Bootstrap the project

```bash
make bootstrap
```

### 3 Run tests

```bash
make test
```

### 4 Download sample raw data

```bash
make download
```

### 5 Run the placeholder pipeline

```bash
make run
```

## Planned Gold Marts

* daily_trip_summary
* borough_hour_demand
* payment_type_revenue

## Future Improvements

* Bronze ingestion metadata tracking
* Silver cleaning rules
* Gold business marts
* Airflow orchestration
* DuckDB analytics views
* CI/CD validation
* architecture diagrams

## Author

Darrell Mortalla
