"""
Enterprise Product Master Generator
"""

import random

import pandas as pd

from configs.settings import PRODUCT_COUNT
from configs.product_master import (
    PRODUCT_CATEGORIES,
    BRANDS,
    PACKAGE_SIZES,
    UOMS,
    GST,
    SHELF_LIFE,
)

from utils.id_generator import generate_id
from utils.pricing import generate_pricing
from utils.logger import logger
from utils.pipeline_runner import run_pipeline


def main():

    products = []

    logger.info("Product generation started")

    for i in range(1, PRODUCT_COUNT + 1):

        category = random.choice(
            list(PRODUCT_CATEGORIES.keys())
        )

        subcategory = random.choice(
            PRODUCT_CATEGORIES[category]
        )

        brand = random.choice(BRANDS)

        package_size = random.choice(PACKAGE_SIZES)

        uom = random.choice(UOMS)

        gst = random.choice(GST)

        shelf_life = random.choice(SHELF_LIFE)

        cost_price, selling_price, margin = generate_pricing()

        product = {

            # ==================================================
            # IDENTIFICATION
            # ==================================================

            "product_id": generate_id("PROD", i),

            "sku": generate_id("SKU", i),

            # ==================================================
            # PRODUCT DETAILS
            # ==================================================

            "product_name": (
                f"{brand} "
                f"{subcategory} "
                f"{package_size}{uom}"
            ),

            "brand": brand,

            "category": category,

            "subcategory": subcategory,

            "package_size": package_size,

            "uom": uom,

            # ==================================================
            # PRICING
            # ==================================================

            "cost_price": cost_price,

            "selling_price": selling_price,

            "margin_percent": margin,

            "gst_percent": gst,

            # ==================================================
            # INVENTORY
            # ==================================================

            "shelf_life_months": shelf_life,

            "status": "Active"

        }

        products.append(product)

    logger.info("Creating DataFrame")

    df = pd.DataFrame(products)

    run_pipeline(
        dataframe=df,
        folder="products",
        filename="products",
        id_column="product_id",
        required_columns=[
            "product_id",
            "product_name",
            "brand",
            "category"
        ],
        title="Enterprise Product Master Generated"
    )


if __name__ == "__main__":
    main()