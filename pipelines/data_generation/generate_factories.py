"""
Enterprise Factory Master Generator
"""

from datetime import datetime

import pandas as pd

from configs.settings import FACTORY_COUNT

from utils.id_generator import generate_id

from utils.location_utils import (
    random_location,
    get_city_details
)

from utils.factory_utils import (
    random_factory_name,
    random_factory_code,
    random_factory_type,
    random_shift,
    random_status,
    random_production_lines,
    random_daily_capacity,
    random_factory_manager,
    random_email,
    random_phone
)

from utils.pipeline_runner import run_pipeline
from utils.logger import logger


def main():

    factories = []

    logger.info("Factory generation started")

    for i in range(1, FACTORY_COUNT + 1):

        location = random_location()

        city = location["city"]

        city_details = get_city_details(city)

        factory_name = random_factory_name()

        factory = {

            # ==================================================
            # IDENTIFICATION
            # ==================================================

            "factory_id": generate_id("FAC", i),

            "factory_code": random_factory_code(i),

            # ==================================================
            # BASIC DETAILS
            # ==================================================

            "factory_name": factory_name,

            "factory_type": random_factory_type(),

            # ==================================================
            # LOCATION
            # ==================================================

            "region": location["region"],

            "state": location["state"],

            "city": city,

            "address":
                f"{city_details['postal_code']} Industrial Estate, "
                f"{city}, {location['state']}",

            "postal_code": city_details["postal_code"],

            "latitude": city_details["latitude"],

            "longitude": city_details["longitude"],

            # ==================================================
            # OPERATIONS
            # ==================================================

            "production_lines": random_production_lines(),

            "daily_capacity": random_daily_capacity(),

            "shift": random_shift(),

            # ==================================================
            # MANAGEMENT
            # ==================================================

            "manager_name": random_factory_manager(),

            "email": random_email(factory_name),

            "phone": random_phone(),

            # ==================================================
            # STATUS
            # ==================================================

            "status": random_status(),

            # ==================================================
            # AUDIT
            # ==================================================

            "created_at": datetime.now(),

            "updated_at": datetime.now()

        }

        factories.append(factory)

    logger.info("Creating DataFrame")

    df = pd.DataFrame(factories)

    run_pipeline(
        dataframe=df,
        folder="factories",
        filename="factories",
        id_column="factory_id",
        required_columns=[
            "factory_id",
            "factory_code",
            "factory_name",
            "city"
        ],
        title="Enterprise Factory Master Generated"
    )


if __name__ == "__main__":
    main()