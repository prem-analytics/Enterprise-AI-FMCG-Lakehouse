"""
Goods Receipt Date Utility
Enterprise AI FMCG Lakehouse

Generates realistic Goods Receipt dates.
"""

from datetime import timedelta


# ==========================================================
# RECEIPT DATE
# ==========================================================

def generate_receipt_date(
    order_date,
    expected_delivery_date,
):
    """
    Generate the actual receipt date.

    Business Rules
    --------------
    - Goods cannot be received before the order date.
    - Goods are usually received on or after the expected delivery date.
    - Delays of up to 5 days are allowed.
    """

    receipt_date = expected_delivery_date + timedelta(days=2)

    return receipt_date


# ==========================================================
# POSTING DATE
# ==========================================================

def generate_posting_date(
    receipt_date,
):
    """
    Financial posting date.

    Normally same day as receipt.
    """

    return receipt_date


# ==========================================================
# INVENTORY UPDATE DATE
# ==========================================================

def generate_inventory_date(
    posting_date,
):
    """
    Inventory is updated after posting.

    Normally same day.
    """

    return posting_date