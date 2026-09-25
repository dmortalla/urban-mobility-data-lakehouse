# 🚕 Urban Mobility Data Lakehouse

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Status](https://img.shields.io/badge/status-complete-brightgreen)
![License](https://img.shields.io/badge/license-MIT-green)

A production-style data engineering project that transforms NYC taxi trip data through a reproducible **Bronze → Silver → Gold** medallion pipeline using Python, Pandas, Parquet, DuckDB, and configuration-driven orchestration.

## 📌 Overview

The Urban Mobility Data Lakehouse builds an analytics-ready data platform for NYC taxi trip data.

Raw trip records move through a medallion architecture that separates source ingestion, data cleaning, business transformations, and analytical serving. The resulting Gold marts support analysis of trip activity, demand patterns, and payment behavior, while DuckDB provides a lightweight SQL analytics warehouse for downstream exploration.

The project demonstrates how raw transportation data can be transformed into trusted analytical datasets through a modular and reproducible data engineering workflow.

## 🎯 Business Problem

Raw transportation datasets are not designed for direct business analysis. A mobility analytics team needs a repeatable pipeline that can:

- ingest monthly trip datasets
- preserve raw source data and lineage
- clean and standardize records
- validate data before downstream use
- create trusted business-facing aggregates
- expose analytics-ready datasets through SQL

This project addresses those requirements with a local-first medallion lakehouse architecture.

## ✨ Key Features

- **Medallion Architecture**Implements a Bronze → Silver → Gold data model that separates raw ingestion, cleaned datasets, and analytics-ready aggregates.
- **Parquet-Based Lakehouse Storage**Uses columnar Parquet files for efficient analytical storage across the lakehouse layers.
- **DuckDB Analytics Warehouse**Loads Gold-layer outputs into DuckDB for local SQL analytics and OLAP-style querying.
- **Config-Driven Pipeline Execution**Uses YAML configuration files to control runtime paths and pipeline settings.
- **Modular ETL Design**Separates extraction, transformation, validation, Gold-layer processing, and warehouse functionality into focused modules.
- **Automated Testing**Includes tests covering pipeline components, transformations, validation, and warehouse behavior.
- **Reproducible Workflow**
  Provides scripts and Makefile commands for downloading data, running the medallion pipeline, testing the project, and loading analytical outputs into DuckDB.

## 🏗️ Architecture

The project follows a medallion-style data architecture:

```text
NYC Taxi Trip Data
        │
        ▼
   Raw Landing
        │
        ▼
   Bronze Layer
   Raw-preserving ingestion
        │
        ▼
   Silver Layer
   Cleaned and standardized data
        │
        ▼
   Gold Layer
   Analytics-ready business marts
        │
        ▼
   DuckDB Warehouse
   SQL analytics and exploration
```

The primary pipeline entry point processes data through **Raw → Bronze → Silver → Gold**. Loading the resulting Gold datasets into DuckDB is performed as a separate warehouse step.

## 🥇 Gold Analytics Marts

The Gold layer produces three analytics-ready marts:

- `daily_trip_summary` — daily trip-volume and performance metrics
- `borough_hour_demand` — hourly demand patterns by borough
- `payment_type_revenue` — revenue metrics segmented by payment type

The pipeline writes these analytics-ready datasets to the Gold layer, and the repository includes dedicated SQL queries for downstream DuckDB analytics.

## 🛠️ Tech Stack

| Technology            | Purpose                                     |
| --------------------- | ------------------------------------------- |
| **Python 3.11** | Pipeline implementation and orchestration   |
| **Pandas**      | Data transformation and aggregation         |
| **Parquet**     | Columnar lakehouse storage                  |
| **DuckDB**      | Local analytical warehouse and SQL querying |
| **YAML**        | Pipeline and logging configuration          |
| **Pytest**      | Automated testing                           |
| **Make**        | Development workflow commands               |

## 📁 Repository Structure

```text
urban-mobility-data-lakehouse/
├── config/        # Pipeline and logging configuration
├── data/          # Local raw, lakehouse, and warehouse data
├── docs/          # Architecture notes and project documentation
├── scripts/       # Download, pipeline, bootstrap, and warehouse entry points
├── sql/           # Gold mart definitions and example analytics queries
├── src/
│   ├── bronze/    # Bronze-layer processing
│   ├── extract/   # Source ingestion
│   ├── gold/      # Gold-layer output logic
│   ├── silver/    # Silver-layer processing
│   ├── transform/ # Transformation logic
│   ├── utils/     # Shared utilities
│   ├── validate/  # Data validation
│   └── warehouse/ # DuckDB warehouse loading
├── tests/         # Automated tests
├── Makefile       # Common development commands
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### 📥 1. Clone the Repository

```bash
git clone https://github.com/dmortalla/urban-mobility-data-lakehouse.git
cd urban-mobility-data-lakehouse
```

### 🐍 2. Create the Python Environment

```bash
conda create -n lakehouse python=3.11
conda activate lakehouse
pip install -r requirements.txt
```

### 📦 3. Download the Raw Dataset

```bash
python -m scripts.download_data
```

### 🔄 4. Run the Medallion Pipeline

```bash
python -m scripts.run_pipeline
```

This executes the implemented pipeline:

```text
Raw → Bronze → Silver → Gold
```

If no raw Parquet files are available, the pipeline exits without processing and instructs the user to download the source data first.

### 🦆 5. Load Gold Data into DuckDB

```bash
python -m scripts.load_duckdb
```

This loads Gold-layer outputs into:

```text
data/warehouse/analytics.duckdb
```

### 🔎 6. Query the Analytics Warehouse

Using the DuckDB CLI:

```bash
duckdb data/warehouse/analytics.duckdb
```

Then execute the included example queries:

```sql
.read sql/example_queries.sql
```

## ⚙️ Makefile Workflow

The repository also provides convenient Makefile commands:

```bash
make install
make bootstrap
make test
make download
make run
```

`make run` executes `scripts/run_pipeline.py`, which orchestrates the Raw → Bronze → Silver → Gold processing path.

DuckDB loading remains an explicit downstream warehouse step and can be run with:

```bash
python -m scripts.load_duckdb
```

## 🧪 Testing

Run the automated test suite with:

```bash
python -m pytest
```

or:

```bash
make test
```

The test suite validates key pipeline behaviors across ingestion, transformation, configuration, validation, and warehouse functionality.

## ✅ Implementation Status

The core local data platform is implemented and tested:

- ✅ Bronze data ingestion
- ✅ Silver data transformation
- ✅ Gold analytics layer
- ✅ Three analytics-ready Gold marts
- ✅ DuckDB warehouse loading
- ✅ Example SQL analytics queries
- ✅ Configuration-driven execution
- ✅ Automated test coverage
- ✅ Reproducible local workflow

## 🧠 Engineering Decisions

### 🥉 Medallion Data Modeling

Separating data into Bronze, Silver, and Gold layers keeps raw ingestion independent from cleaning and business aggregation. Each stage has a clear responsibility and produces data appropriate for the next stage.

### 📦 Parquet for Lakehouse Storage

Parquet provides a compact columnar format suited to analytical workloads while keeping the project lightweight enough to reproduce locally.

### 🦆 DuckDB for Analytical Serving

DuckDB provides SQL-based analytical capabilities without requiring an external database server, making the warehouse layer portable and easy to reproduce.

### ⚙️ Configuration-Driven Execution

Runtime paths and pipeline settings are kept outside core transformation logic so the implementation is easier to configure and maintain.

### 🧩 Modular Pipeline Components

Extraction, transformation, validation, layer-specific processing, and warehouse loading are separated into dedicated modules rather than being implemented as one monolithic script.

## 🔭 Potential Extensions

The current implementation provides the core local lakehouse workflow. Natural extensions include:

- workflow orchestration with Apache Airflow
- CI/CD validation for automated pipeline quality gates
- cloud object storage integration
- data observability and pipeline monitoring
- incremental ingestion and partition-aware processing
- expanded analytical marts
- downstream BI/dashboard integration

These are potential extensions rather than requirements of the current implementation.

## 💼 What This Project Demonstrates

This project demonstrates practical data engineering skills across:

- medallion/lakehouse architecture
- ETL pipeline development
- raw-data ingestion
- data cleaning and transformation
- analytical data modeling
- Parquet-based storage
- SQL analytics with DuckDB
- configuration-driven pipelines
- automated testing
- modular Python architecture
- reproducible data workflows

## 👤 Author

**Darrell Mortalla**

GitHub: [dmortalla](https://github.com/dmortalla)
