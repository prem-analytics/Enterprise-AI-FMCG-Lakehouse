"""
Enterprise Product Master Generator
"""

import time
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
from utils.file_utils import save_dataset
from utils.validation import validate_dataset
from utils.metadata import create_metadata
from utils.sample_generator import create_sample
from utils.pricing import generate_pricing
from utils.logger import logger


def main():

    start_time = time.time()

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

            "product_id": generate_id("PROD", i),

            "sku": generate_id("SKU", i),

            "product_name": f"{brand} {subcategory} {package_size}{uom}",

            "brand": brand,

            "category": category,

            "subcategory": subcategory,

            "package_size": package_size,

            "uom": uom,

            "cost_price": cost_price,

            "selling_price": selling_price,

            "margin_percent": margin,

            "gst_percent": gst,

            "shelf_life_months": shelf_life,

            "status": "Active"

        }

        products.append(product)

    logger.info("Creating DataFrame")

    df = pd.DataFrame(products)

    logger.info("Validating dataset")

    validate_dataset(
        df,
        id_column="product_id",
        required_columns=[
            "product_id",
            "product_name",
            "brand",
            "category"
        ]
    )

    logger.info("Saving dataset")

    save_dataset(
        dataframe=df,
        folder="products",
        filename="products"
    )

    logger.info("Creating metadata")

    create_metadata(
        dataframe=df,
        folder="products",
        filename="products"
    )

    logger.info("Creating sample dataset")

    create_sample(
        dataframe=df,
        folder="products",
        filename="products"
    )

    elapsed_time = time.time() - start_time

    print("\n" + "=" * 60)
    print("Enterprise Product Master Generated")
    print("=" * 60)
    print(f"Rows Generated : {len(df):,}")
    print("Validation     : PASSED")
    print("CSV File       : data/generated/products/products.csv")
    print("Parquet File   : data/generated/products/products.parquet")
    print("Metadata File  : data/generated/products/products_metadata.json")
    print("Sample File    : data/sample_data/products_sample.csv")
    print("=" * 60)
    print(f"Execution Time : {elapsed_time:.2f} seconds")

    logger.info(
        f"Generated {len(df):,} product records successfully"
    )

    logger.info(
        f"Execution completed in {elapsed_time:.2f} seconds"
    )


if __name__ == "__main__":
    main()