"""
Enterprise Customer Master Generator
"""

import os
import random
from datetime import datetime

import pandas as pd

from configs.settings import CUSTOMER_COUNT
from utils.faker_utils import random_customer
from utils.id_generator import generate_id

LOYALTY_TIERS = [
    "Bronze",
    "Silver",
    "Gold",
    "Platinum"
]

STATUS = [
    "Active",
    "Inactive"
]

OUTPUT_FOLDER = os.path.join(
    "data",
    "generated",
    "customers"
)

os.makedirs(
    OUTPUT_FOLDER,
    exist_ok=True
)

customers = []

for i in range(1, CUSTOMER_COUNT + 1):

    customer = random_customer()

    customer["customer_id"] = generate_id("CUST", i)

    customer["loyalty_tier"] = random.choices(
        LOYALTY_TIERS,
        weights=[60, 25, 10, 5],
        k=1
    )[0]

    customer["status"] = random.choices(
        STATUS,
        weights=[95, 5],
        k=1
    )[0]

    customer["join_date"] = datetime.now().date()

    customers.append(customer)

df = pd.DataFrame(customers)
csv_file = os.path.join(
    OUTPUT_FOLDER,
    "customers.csv"
)

parquet_file = os.path.join(
    OUTPUT_FOLDER,
    "customers.parquet"
)

df.to_csv(csv_file, index=False)

df.to_parquet(parquet_file, index=False)
print("=" * 60)
print("Enterprise Customer Master Generated")
print("=" * 60)
print(f"Rows Generated : {len(df):,}")
print(f"CSV File       : {csv_file}")
print(f"Parquet File   : {parquet_file}")