"""
Enterprise Supplier Master Generator
"""

from datetime import datetime

import pandas as pd

from configs.settings import SUPPLIER_COUNT

from utils.id_generator import generate_id
from utils.location_utils import (
    random_location,
    get_city_details
)
from utils.faker_utils import random_name

from utils.supplier_utils import (
    random_supplier_name,
    random_supplier_type,
    random_supplier_email,
    random_supplier_phone,
    random_payment_term,
    random_currency,
    random_supplier_status,
    random_supplier_rating,
    random_lead_time,
    random_preferred_supplier,
    random_pan,
    random_gstin
)

from utils.pipeline_runner import run_pipeline
from utils.logger import logger


def main():

    suppliers = []

    logger.info("Supplier generation started")

    for i in range(1, SUPPLIER_COUNT + 1):

        location = random_location()

        city = location["city"]

        city_details = get_city_details(city)

        supplier_name = random_supplier_name()

        supplier = {

            # ==================================================
            # IDENTIFICATION
            # ==================================================

            "supplier_id": generate_id("SUP", i),

            "supplier_code": f"SUP-{i:05d}",

            # ==================================================
            # BASIC DETAILS
            # ==================================================

            "supplier_name": supplier_name,

            "supplier_type": random_supplier_type(),

            "contact_person": random_name(),

            # ==================================================
            # CONTACT
            # ==================================================

            "email": random_supplier_email(supplier_name),

            "phone": random_supplier_phone(),

            # ==================================================
            # LOCATION
            # ==================================================

            "region": location["region"],

            "state": location["state"],

            "city": city,

            "address": (
                f"{city_details['postal_code']} "
                f"{city}, {location['state']}"
            ),

            "postal_code": city_details["postal_code"],

            "latitude": city_details["latitude"],

            "longitude": city_details["longitude"],

            # ==================================================
            # TAX DETAILS
            # ==================================================

            "gst_number": random_gstin(),

            "pan_number": random_pan(),

            # ==================================================
            # PROCUREMENT
            # ==================================================

            "payment_terms": random_payment_term(),

            "lead_time_days": random_lead_time(),

            # ==================================================
            # BUSINESS
            # ==================================================

            "currency": random_currency(),

            "supplier_rating": random_supplier_rating(),

            "preferred_supplier": random_preferred_supplier(),

            "status": random_supplier_status(),

            # ==================================================
            # AUDIT
            # ==================================================

            "created_at": datetime.now(),

            "updated_at": datetime.now()

        }

        suppliers.append(supplier)

    logger.info("Creating DataFrame")

    df = pd.DataFrame(suppliers)

    run_pipeline(
        dataframe=df,
        folder="suppliers",
        filename="suppliers",
        id_column="supplier_id",
        required_columns=[
            "supplier_id",
            "supplier_name",
            "city"
        ],
        title="Enterprise Supplier Master Generated"
    )


if __name__ == "__main__":
    main()