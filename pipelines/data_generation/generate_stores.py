"""
Enterprise Store Master Generator
"""

import time
from datetime import datetime

import pandas as pd

from configs.settings import STORE_COUNT

from utils.id_generator import generate_id
from utils.location_utils import (
    random_location,
    get_city_details
)
from utils.store_utils import (
    random_store_name,
    random_store_type,
    random_store_email,
    random_store_phone,
    random_store_status,
    random_store_code,
    random_address,
    random_postal_code,
    random_opening_time,
    random_closing_time,
    random_channel,
    random_floor_area,
    random_franchise,
    random_coordinates
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

        city_details = get_city_details(
            location["city"]
        )

        store_name = random_store_name()

        store = {

            # ==================================================
            # IDENTIFICATION
            # ==================================================

            "store_id": generate_id("STORE", i),

            "store_code": random_store_code(i),

            "store_name": store_name,

            # ==================================================
            # STORE DETAILS
            # ==================================================

            "store_type": random_store_type(),

            "channel": random_channel(),

            "status": random_store_status(),

            "is_franchise": random_franchise(),

            # ==================================================
            # LOCATION
            # ==================================================

            "region": location["region"],

            "state": location["state"],

            "city": location["city"],

            "address": (
                f"{random_address()}, "
                f"{location['city']}, "
                f"{location['state']}"
            ),

            "postal_code": city_details["postal_code"],

            "latitude": city_details["latitude"],

            "longitude": city_details["longitude"],

            # ==================================================
            # CONTACT
            # ==================================================

            "phone": random_store_phone(),

            "email": random_store_email(store_name),

            # ==================================================
            # OPERATIONS
            # ==================================================

            "opening_time": random_opening_time(),

            "closing_time": random_closing_time(),

            "floor_area_sqft": random_floor_area(),

            "opening_date": datetime.now().date(),

            # ==================================================
            # AUDIT
            # ==================================================

            "created_at": datetime.now(),

            "updated_at": datetime.now()

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
            "store_code",
            "store_name",
            "store_type",
            "channel",
            "region",
            "state",
            "city",
            "phone",
            "email"
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