"""
Purchase Order Generation Pipeline
Enterprise AI FMCG Lakehouse
"""

import pandas as pd
from pathlib import Path

from utils.purchase_order_utils import build_purchase_order

from utils.validation import validate_dataset
from utils.metadata import generate_metadata
from utils.sample_generator import save_sample_dataset
from utils.file_utils import (
    save_csv,
    save_parquet
)

# ==========================================================
# CONFIGURATION
# ==========================================================

NUMBER_OF_PURCHASE_ORDERS = 1000

OUTPUT_PATH = Path(
    "data/generated/procurement"
)

OUTPUT_PATH.mkdir(
    parents=True,
    exist_ok=True
)

# ==========================================================
# GENERATE PURCHASE ORDERS
# ==========================================================

purchase_orders = []

print("Generating Purchase Orders...")

for _ in range(NUMBER_OF_PURCHASE_ORDERS):

    purchase_orders.append(
        build_purchase_order()
    )

df = pd.DataFrame(
    purchase_orders
)

# ==========================================================
# VALIDATION
# ==========================================================

validate_dataset(
    df,
    id_column="po_number"
)

# ==========================================================
# SAVE
# ==========================================================

csv_path = OUTPUT_PATH / "purchase_orders.csv"

parquet_path = OUTPUT_PATH / "purchase_orders.parquet"

save_csv(
    df,
    csv_path
)

save_parquet(
    df,
    parquet_path
)

generate_metadata(
    df,
    OUTPUT_PATH / "purchase_orders_metadata.json"
)

save_sample_dataset(
    df,
    OUTPUT_PATH / "purchase_orders_sample.csv"
)

print()

print("=" * 60)
print("Purchase Orders Generated Successfully")
print("=" * 60)
print(f"Rows : {len(df):,}")
print(f"CSV : {csv_path}")
print(f"Parquet : {parquet_path}")