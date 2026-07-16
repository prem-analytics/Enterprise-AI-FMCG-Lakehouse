"""
Enterprise Warehouse Master Generator
"""

from datetime import datetime

import pandas as pd

from configs.settings import WAREHOUSE_COUNT

from utils.id_generator import generate_id

from utils.location_utils import (
    random_location,
    get_city_details
)

from utils.warehouse_utils import (
    random_warehouse_name,
    random_warehouse_code,
    random_warehouse_type,
    random_temperature_zone,
    random_operating_hours,
    random_capacity,
    random_utilization,
    random_manager,
    random_email,
    random_phone,
    random_status
)

from utils.pipeline_runner import run_pipeline
from utils.logger import logger


def main():

    warehouses = []

    logger.info("Warehouse generation started")

    for i in range(1, WAREHOUSE_COUNT + 1):

        location = random_location()

        city = location["city"]

        city_details = get_city_details(city)

        warehouse_name = random_warehouse_name()

        warehouse = {

            # ==================================================
            # IDENTIFICATION
            # ==================================================

            "warehouse_id": generate_id("WH", i),

            "warehouse_code": random_warehouse_code(i),

            # ==================================================
            # BASIC DETAILS
            # ==================================================

            "warehouse_name": warehouse_name,

            "warehouse_type": random_warehouse_type(),

            # ==================================================
            # LOCATION
            # ==================================================

            "region": location["region"],

            "state": location["state"],

            "city": city,

            "address": (
                f"{city_details['postal_code']} "
                f"MG Road, "
                f"{city}, "
                f"{location['state']}"
            ),

            "postal_code": city_details["postal_code"],

            "latitude": city_details["latitude"],

            "longitude": city_details["longitude"],

            # ==================================================
            # MANAGEMENT
            # ==================================================

            "manager_name": random_manager(),

            "email": random_email(warehouse_name),

            "phone": random_phone(),

            # ==================================================
            # OPERATIONS
            # ==================================================

            "storage_capacity_mt": random_capacity(),

            "current_utilization_percent": random_utilization(),

            "temperature_zone": random_temperature_zone(),

            "operating_hours": random_operating_hours(),

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

        warehouses.append(warehouse)

    logger.info("Creating DataFrame")

    df = pd.DataFrame(warehouses)

    run_pipeline(
        dataframe=df,
        folder="warehouses",
        filename="warehouses",
        id_column="warehouse_id",
        required_columns=[
            "warehouse_id",
            "warehouse_code",
            "warehouse_name",
            "city"
        ],
        title="Enterprise Warehouse Master Generated"
    )


if __name__ == "__main__":
    main()