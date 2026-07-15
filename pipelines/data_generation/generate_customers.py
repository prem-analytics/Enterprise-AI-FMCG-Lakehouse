"""
Enterprise Customer Master Generator
"""
import time
import random
from datetime import datetime

import pandas as pd

from configs.settings import CUSTOMER_COUNT
from utils.faker_utils import random_customer
from utils.id_generator import generate_id
from utils.logger import logger

from utils.file_utils import save_dataset
from utils.validation import validate_dataset
from utils.metadata import create_metadata
from utils.sample_generator import create_sample

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

def main():

    start_time = time.time()
    customers = []

    logger.info("Customer generation started")

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

    logger.info("Creating DataFrame")
    df = pd.DataFrame(customers)

    logger.info("Validating dataset")
    validate_dataset(
        df,
        id_column="customer_id",
        required_columns=[
            "customer_id",
            "first_name",
            "last_name"
        ]
    )

    logger.info("Saving dataset")
    save_dataset(
        dataframe=df,
        folder="customers",
        filename="customers"
    )

    logger.info("Creating metadata")
    create_metadata(
        dataframe=df,
        folder="customers",
        filename="customers"
    )

    logger.info("Creating sample dataset")
    create_sample(
        dataframe=df,
        folder="customers",
        filename="customers"
    )

    print("\n" + "=" * 60)
    print("Enterprise Customer Master Generated")
    print("=" * 60)
    print(f"Rows Generated : {len(df):,}")
    print("Validation     : PASSED")
    print("CSV File       : data/generated/customers/customers.csv")
    print("Parquet File   : data/generated/customers/customers.parquet")
    print("Metadata File  : data/generated/customers/customers_metadata.json")
    print("Sample File    : data/sample_data/customers_sample.csv")
    print("=" * 60)

    logger.info(f"Generated {len(df):,} customer records successfully")

    elapsed_time = time.time() - start_time

    print(f"Execution Time : {elapsed_time:.2f} seconds")

    logger.info(
        f"Execution completed in {elapsed_time:.2f} seconds"
    )


if __name__ == "__main__":
    main()