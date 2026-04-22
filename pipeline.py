import logging, os, sys
from datetime import datetime
from extract import extract_from_csv
from transform import transform
from load import load, query_db

CONFIG = {
    "source_csv": "data/superstore.csv",
    "db_path":    "output/sales.db",
    "csv_output": "output/clean_sales.csv",
    "log_dir":    "logs",
}

def setup_logging(log_dir):
    os.makedirs(log_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(f"{log_dir}/pipeline_{ts}.log"),
        ]
    )

def run_pipeline():
    logger = logging.getLogger(__name__)
    start  = datetime.now()
    logger.info("=" * 50)
    logger.info("  ETL PIPELINE STARTED")
    logger.info("=" * 50)
    try:
        logger.info("--- STEP 1: EXTRACT ---")
        raw_df = extract_from_csv(CONFIG["source_csv"])
        logger.info("--- STEP 2: TRANSFORM ---")
        clean_df = transform(raw_df)
        logger.info("--- STEP 3: LOAD ---")
        load(clean_df, CONFIG["db_path"], CONFIG["csv_output"])
        elapsed = (datetime.now() - start).total_seconds()
        logger.info("=" * 50)
        logger.info(f"  PIPELINE COMPLETE | Rows: {len(clean_df)} | Time: {elapsed:.2f}s")
        logger.info("=" * 50)
        print("\nTop 5 by sales:")
        print(query_db(CONFIG["db_path"],
            "SELECT order_id, customer_name, category, sales, value_tier FROM sales ORDER BY sales DESC LIMIT 5"
        ).to_string(index=False))
        print("\nSales by category:")
        print(query_db(CONFIG["db_path"],
            "SELECT category, COUNT(*) as orders, ROUND(SUM(sales),2) as total_sales FROM sales GROUP BY category ORDER BY total_sales DESC"
        ).to_string(index=False))
    except Exception as e:
        logger.error(f"PIPELINE FAILED: {e}", exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    setup_logging(CONFIG["log_dir"])
    run_pipeline()
