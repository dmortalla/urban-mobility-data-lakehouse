"""
Tests for ingestion metadata enrichment.
"""

from __future__ import annotations

import pandas as pd

from src.transform.add_metadata import add_ingestion_metadata


def test_add_ingestion_metadata_adds_expected_columns() -> None:
    """
    Ensure metadata columns are added to the dataframe.
    """
    df = pd.DataFrame({"trip_distance": [1.2, 3.4]})

    result = add_ingestion_metadata(
        df=df,
        source_file="yellow_tripdata_2024-01.parquet",
    )

    assert "source_file" in result.columns
    assert "ingestion_timestamp" in result.columns
    assert "batch_id" in result.columns
    assert (result["source_file"] == "yellow_tripdata_2024-01.parquet").all()