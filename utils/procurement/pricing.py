"""
Procurement Pricing Utility
Enterprise AI FMCG Lakehouse
"""

import random


# ==========================================================
# UNIT PRICE
# ==========================================================

def generate_unit_price(
    min_price=50,
    max_price=5000
):
    """
    Generate a random unit price.

    Future:
        Read supplier-product contract pricing.
    """

    return round(
        random.uniform(min_price, max_price),
        2
    )


# ==========================================================
# QUANTITY
# ==========================================================

def generate_quantity(
    min_qty=10,
    max_qty=5000
):
    """
    Generate a random procurement quantity.
    """

    return random.randint(
        min_qty,
        max_qty
    )