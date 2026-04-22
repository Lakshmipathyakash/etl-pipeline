import pandas as pd
import logging

logger = logging.getLogger(__name__)

def extract_from_csv(filepath: str) -> pd.DataFrame:
    logger.info(f"[EXTRACT] Reading file: {filepath}")
    try:
        df = pd.read_csv(filepath)
        logger.info(f"[EXTRACT] Success — {len(df)} rows, {len(df.columns)} columns loaded")
        return df
    except FileNotFoundError:
        logger.error(f"[EXTRACT] File not found: {filepath}")
        raise

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    df = extract_from_csv("data/superstore.csv")
    print(df.head(3))
