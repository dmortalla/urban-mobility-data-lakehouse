
# Urban Mobility Data Lakehouse

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Status](https://img.shields.io/badge/status-in--progress-yellow)
![License](https://img.shields.io/badge/license-MIT-green)

A production-style data engineering project that ingests, validates, transforms, and serves NYC taxi trip data through a medallion-style lakehouse pipeline using Python, PySpark, DuckDB, and local orchestration.

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

```text
Raw Data -> Bronze -> Silver -> Gold -> DuckDB Analytics Layer
```

## Tech Stack

* Python
* PySpark
* DuckDB
* Pandas
* PyArrow
* YAML configuration
* Pytest

## Repository Structure

```text
src/        application logic
scripts/    entry-point scripts
config/     runtime configuration
sql/        Gold mart SQL
tests/      validation and unit tests
docs/       architecture notes and screenshots
```

## Current Milestone

Milestone 1: Project scaffolding and environment setup.

Included in this milestone:

* repo structure
* configuration loading
* logging setup
* bootstrap script
* raw data download script
* starter tests
* placeholder pipeline modules

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
