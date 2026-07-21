"""
Procurement Date Utility
Enterprise AI FMCG Lakehouse
"""

import random
from datetime import datetime, timedelta

from configs.purchase_order_master import (
    LEAD_TIME_DAYS,
    PAYMENT_TERMS
)

# ==========================================================
# ORDER DATE
# ==========================================================

def generate_order_date(
    start_year: int = 2024,
    end_year: int = 2026
) -> datetime:
    """
    Generate a random purchase order date.
    """

    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)

    total_days = (end - start).days

    return start + timedelta(
        days=random.randint(0, total_days)
    )


# ==========================================================
# EXPECTED DELIVERY DATE
# ==========================================================

def generate_expected_delivery_date(
    order_date: datetime
) -> datetime:
    """
    Delivery Date >= Order Date
    """

    lead_time = random.randint(
        LEAD_TIME_DAYS[0],
        LEAD_TIME_DAYS[1]
    )

    return order_date + timedelta(days=lead_time)


# ==========================================================
# GOODS RECEIPT DATE
# ==========================================================

def generate_receipt_date(
    expected_delivery_date: datetime
) -> datetime:
    """
    Receipt can occur a few days before/after expected delivery.
    """

    delay = random.randint(-2, 5)

    receipt_date = expected_delivery_date + timedelta(days=delay)

    return max(receipt_date, expected_delivery_date)


# ==========================================================
# SUPPLIER INVOICE DATE
# ==========================================================

def generate_invoice_date(
    receipt_date: datetime
) -> datetime:
    """
    Invoice is generated after receipt.
    """

    return receipt_date + timedelta(
        days=random.randint(0, 5)
    )


# ==========================================================
# PAYMENT DUE DATE
# ==========================================================

def generate_due_date(
    invoice_date: datetime,
    payment_term: str
) -> datetime:
    """
    Due Date = Invoice Date + Payment Terms
    """

    days = PAYMENT_TERMS[payment_term]

    return invoice_date + timedelta(days=days)


# ==========================================================
# PAYMENT DATE
# ==========================================================

def generate_payment_date(
    due_date: datetime
) -> datetime:
    """
    Vendor may be paid before or after due date.
    """

    variation = random.randint(-5, 10)

    payment_date = due_date + timedelta(days=variation)

    return payment_date