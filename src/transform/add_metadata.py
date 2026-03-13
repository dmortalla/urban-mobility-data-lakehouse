"""
Metadata enrichment utilities for Bronze ingestion.
"""

from __future__ import annotations

from datetime import datetime
from uuid import uuid4

import pandas as pd


def add_ingestion_metadata(df: pd.DataFrame, source_file: str) -> pd.DataFrame:
    """
    Add ingestion metadata columns to a dataframe.

    Args:
        df: Input dataframe.
        source_file: Name of the raw source file.

    Returns:
        A copy of the dataframe with ingestion metadata columns added.
    """
    enriched_df = df.copy()

    enriched_df["source_file"] = source_file
    enriched_df["ingestion_timestamp"] = datetime.utcnow().isoformat()
    enriched_df["batch_id"] = str(uuid4())

    return enriched_df