"""
Enterprise Store Master Generator
"""

import time
from datetime import datetime

import pandas as pd

from configs.settings import STORE_COUNT

from utils.id_generator import generate_id
from utils.location_utils import random_location
from utils.store_utils import (
    random_store_name,
    random_store_type,
    random_store_email,
    random_store_phone
)

from utils.file_utils import save_dataset
from utils.validation import validate_dataset
from utils.metadata import create_metadata
from utils.sample_generator import create_sample
from utils.logger import logger


def main():

    start_time = time.time()
    
    stores = []

    logger.info("Store generation started")

    for i in range(1, STORE_COUNT + 1):
        
        location = random_location()

        store_name = random_store_name()

        store = {

            "store_id": generate_id("STORE", i),

            "store_name": store_name,

            "store_type": random_store_type(),

            "region": location["region"],

            "state": location["state"],

            "city": location["city"],

            "email": random_store_email(store_name),

            "phone": random_store_phone(),

            "status": "Active",

            "opening_date": datetime.now().date()

        }

        stores.append(store)
    
    logger.info("Creating DataFrame")

    df = pd.DataFrame(stores)

    logger.info("Validating dataset")

    validate_dataset(
        df,
        id_column="store_id",
        required_columns=[
            "store_id",
            "store_name",
            "city"
        ]
    )

    logger.info("Saving dataset")

    save_dataset(
        df,
        folder="stores",
        filename="stores"
    )

    logger.info("Creating metadata")

    create_metadata(
        dataframe=df,
        folder="stores",
        filename="stores"
    )

    logger.info("Creating sample dataset")

    create_sample(
        dataframe=df,
        folder="stores",
        filename="stores"
    )

    print("\n" + "=" * 60)
    print("Enterprise Store Master Generated")
    print("=" * 60)
    print(f"Rows Generated : {len(df):,}")
    print("Validation     : PASSED")
    print("CSV File       : data/generated/stores/stores.csv")
    print("Parquet File   : data/generated/stores/stores.parquet")
    print("Metadata File  : data/generated/stores/stores_metadata.json")
    print("Sample File    : data/sample_data/stores_sample.csv")
    print("=" * 60)

    logger.info(
        f"Generated {len(df):,} store records successfully"
    )

    elapsed_time = time.time() - start_time

    print(f"Execution Time : {elapsed_time:.2f} seconds")

    logger.info(
        f"Execution completed in {elapsed_time:.2f} seconds"
    )


if __name__ == "__main__":
    main()