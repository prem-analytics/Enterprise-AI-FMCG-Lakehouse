"""
Enterprise Customer Master Generator
"""

import random
from datetime import datetime

import pandas as pd

from configs.settings import CUSTOMER_COUNT

from utils.faker_utils import random_customer
from utils.id_generator import generate_id
from utils.logger import logger
from utils.pipeline_runner import run_pipeline


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

    run_pipeline(
        dataframe=df,
        folder="customers",
        filename="customers",
        id_column="customer_id",
        required_columns=[
            "customer_id",
            "first_name",
            "last_name"
        ],
        title="Enterprise Customer Master Generated"
    )


if __name__ == "__main__":
    main()