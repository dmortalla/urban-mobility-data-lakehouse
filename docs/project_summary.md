
# Urban Mobility Data Lakehouse — Project Summary

This project implements a production-style medallion architecture pipeline for NYC taxi trip data.

The system ingests raw parquet datasets, validates schemas, enriches records with metadata, and transforms them through Bronze, Silver, and Gold data layers. Gold analytics tables are then loaded into a DuckDB warehouse for fast SQL analytics.

## Key Capabilities

- Config-driven pipeline execution
- Schema validation for raw datasets
- Medallion architecture (Bronze → Silver → Gold)
- Parquet-based lakehouse storage
- DuckDB analytics serving layer
- Automated unit tests for pipeline components
- Modular data engineering architecture

## Technology Stack

- Python
- Pandas
- DuckDB
- Pytest
- Parquet data lake

## Example Analytics Use Cases

- Daily trip demand analysis
- Hourly demand patterns
- Payment type revenue breakdown
- SQL analytics through DuckDB warehouse

This project demonstrates practical data engineering skills including pipeline orchestration, data transformation, warehouse integration, and analytics-ready data modeling.
