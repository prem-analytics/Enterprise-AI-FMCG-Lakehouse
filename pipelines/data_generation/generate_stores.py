"""
Enterprise Store Master Generator
"""

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
    random_opening_time,
    random_closing_time,
    random_channel,
    random_floor_area,
    random_franchise
)

from utils.pipeline_runner import run_pipeline
from utils.logger import logger


def main():

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

    run_pipeline(
        dataframe=df,
        folder="stores",
        filename="stores",
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
        ],
        title="Enterprise Store Master Generated"
    )


if __name__ == "__main__":
    main()