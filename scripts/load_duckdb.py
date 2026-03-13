from src.warehouse.load_gold_into_duckdb import load_gold_tables_into_duckdb


def main() -> None:
    load_gold_tables_into_duckdb(
        gold_dir="data/lake/gold",
        db_path="data/warehouse/analytics.duckdb",
    )


if __name__ == "__main__":
    main()