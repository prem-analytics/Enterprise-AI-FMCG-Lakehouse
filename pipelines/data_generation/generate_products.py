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
from utils.file_utils import save_dataset
from utils.pricing import generate_pricing
from utils.logger import logger

logger.info("Product generation started")

products = []

for i in range(1, PRODUCT_COUNT + 1):

    category = random.choice(list(PRODUCT_CATEGORIES.keys()))
    subcategory = random.choice(PRODUCT_CATEGORIES[category])

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

df = pd.DataFrame(products)

save_dataset(
    df=df,
    folder="products",
    filename="products"
)
logger.info("Product generation completed")

print("=" * 60)
print("Enterprise Product Master Generated")
print("=" * 60)
print(f"Rows Generated : {len(df):,}")
print("CSV File       : data/generated/products/products.csv")
print("Parquet File   : data/generated/products/products.parquet")