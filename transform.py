import pandas as pd
import logging

logger = logging.getLogger(__name__)

def transform(df: pd.DataFrame) -> pd.DataFrame:
    logger.info(f"[TRANSFORM] Starting with {len(df)} rows")
    df = df.rename(columns={
        "Order ID": "order_id", "Order Date": "order_date",
        "Ship Date": "ship_date", "Ship Mode": "ship_mode",
        "Customer Name": "customer_name", "Segment": "segment",
        "City": "city", "State": "state", "Region": "region",
        "Category": "category", "Sub-Category": "sub_category",
        "Product Name": "product_name", "Sales": "sales",
        "Quantity": "quantity", "Discount": "discount", "Profit": "profit"
    })
    df = df.dropna(subset=["order_id", "sales", "category"])
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["ship_date"]  = pd.to_datetime(df["ship_date"],  errors="coerce")
    df["sales"]      = pd.to_numeric(df["sales"],    errors="coerce")
    df["profit"]     = pd.to_numeric(df["profit"],   errors="coerce")
    df["revenue_after_discount"] = df["sales"] * (1 - df["discount"])
    df["profit_margin_pct"]      = (df["profit"] / df["sales"] * 100).round(2)
    df["value_tier"] = pd.cut(df["sales"],
        bins=[0, 200, 500, 1000, float("inf")],
        labels=["Low", "Medium", "High", "Premium"])
    df["days_to_ship"] = (df["ship_date"] - df["order_date"]).dt.days
    df["order_month"]  = df["order_date"].dt.to_period("M").astype(str)
    df = df[df["sales"] > 0]
    logger.info(f"[TRANSFORM] Done — {len(df)} clean rows ready")
    return df

if __name__ == "__main__":
    from extract import extract_from_csv
    logging.basicConfig(level=logging.INFO)
    raw = extract_from_csv("data/superstore.csv")
    clean = transform(raw)
    print(clean.head(5))
    print(f"\nValue tiers:\n{clean['value_tier'].value_counts()}")
