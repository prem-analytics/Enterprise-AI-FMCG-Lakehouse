"""
Procurement Selection Utility
Enterprise AI FMCG Lakehouse
"""

import random
from pathlib import Path

import pandas as pd


# ==========================================================
# LOAD MASTER DATA
# ==========================================================


MASTER_PATH = Path("data/generated/master")

BASE_PATH = Path("data/generated")

suppliers = pd.read_csv(
    BASE_PATH / "suppliers" / "suppliers.csv"
)

employees = pd.read_csv(
    BASE_PATH / "master" / "employees.csv"
)

products = pd.read_csv(
    BASE_PATH / "products" / "products.csv"
)

factories = pd.read_csv(
    BASE_PATH / "factories" / "factories.csv"
)

warehouses = pd.read_csv(
    BASE_PATH / "warehouses" / "warehouses.csv"
)


# ==========================================================
# BUYERS
# ==========================================================

buyers = employees[
    employees["department"].isin(
        [
            "Procurement",
            "Supply Chain"
        ]
    )
].copy()

if buyers.empty:
    buyers = employees.copy()


# ==========================================================
# SUPPLIER
# ==========================================================

def get_supplier():

    supplier = suppliers.sample(1).iloc[0]

    return supplier.to_dict()


# ==========================================================
# BUYER
# ==========================================================

def get_buyer():

    buyer = buyers.sample(1).iloc[0]

    return buyer.to_dict()


# ==========================================================
# FACTORY
# ==========================================================

def get_factory():

    factory = factories.sample(1).iloc[0]

    return factory.to_dict()


# ==========================================================
# WAREHOUSE
# ==========================================================

def get_warehouse():

    warehouse = warehouses.sample(1).iloc[0]

    return warehouse.to_dict()


# ==========================================================
# PRODUCTS
# ==========================================================

def get_products(
    min_items=3,
    max_items=20
):
    """
    Random products for one PO.
    """

    item_count = random.randint(
        min_items,
        max_items
    )

    return (
        products
        .sample(item_count)
        .to_dict("records")
    )


# ==========================================================
# SUPPLIER PRODUCTS
# ==========================================================

def get_supplier_products(
    supplier_id=None,
    min_items=3,
    max_items=20
):
    """
    Future enhancement:
    Supplier-wise product mapping.

    Currently returns random products.
    """

    return get_products(
        min_items=min_items,
        max_items=max_items
    )