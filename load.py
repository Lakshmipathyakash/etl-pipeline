import pandas as pd
import sqlite3
import os
import logging

logger = logging.getLogger(__name__)

def load(df: pd.DataFrame, db_path: str, csv_output_path: str) -> None:
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    os.makedirs(os.path.dirname(csv_output_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    df.to_sql("sales", conn, if_exists="replace", index=False)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM sales")
    count = cursor.fetchone()[0]
    conn.close()
    logger.info(f"[LOAD] SQLite → {db_path} | Rows: {count}")
    df.to_csv(csv_output_path, index=False)
    logger.info(f"[LOAD] CSV → {csv_output_path}")

def query_db(db_path: str, sql: str) -> pd.DataFrame:
    conn = sqlite3.connect(db_path)
    result = pd.read_sql(sql, conn)
    conn.close()
    return result

if __name__ == "__main__":
    from extract import extract_from_csv
    from transform import transform
    logging.basicConfig(level=logging.INFO)
    raw = extract_from_csv("data/superstore.csv")
    clean = transform(raw)
    load(clean, db_path="output/sales.db", csv_output_path="output/clean_sales.csv")
    print(query_db("output/sales.db", "SELECT order_id, customer_name, sales, value_tier FROM sales ORDER BY sales DESC LIMIT 5"))
