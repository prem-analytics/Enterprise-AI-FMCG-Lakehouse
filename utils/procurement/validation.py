"""
Procurement Validation Utility
Enterprise AI FMCG Lakehouse
"""

from configs.purchase_order_master import (
    PURCHASE_ORDER_STATUS,
    APPROVAL_STATUS,
    SHIPPING_METHODS,
    PAYMENT_TERMS,
    GST_RATES,
)


# ==========================================================
# SUPPLIER
# ==========================================================

def validate_supplier(supplier):

    if supplier is None:
        raise ValueError("Supplier cannot be None")

    if "supplier_id" not in supplier:
        raise ValueError("supplier_id missing")


# ==========================================================
# BUYER
# ==========================================================

def validate_buyer(employee):

    if employee is None:
        raise ValueError("Buyer cannot be None")

    if "employee_id" not in employee:
        raise ValueError("employee_id missing")


# ==========================================================
# FACTORY
# ==========================================================

def validate_factory(factory):

    if factory is None:
        raise ValueError("Factory cannot be None")

    if "factory_id" not in factory:
        raise ValueError("factory_id missing")


# ==========================================================
# WAREHOUSE
# ==========================================================

def validate_warehouse(warehouse):

    if warehouse is None:
        raise ValueError("Warehouse cannot be None")

    if "warehouse_id" not in warehouse:
        raise ValueError("warehouse_id missing")


# ==========================================================
# DATES
# ==========================================================

def validate_dates(order_date, delivery_date):

    if delivery_date < order_date:
        raise ValueError(
            "Delivery date cannot be before Order Date."
        )


# ==========================================================
# QUANTITY
# ==========================================================

def validate_quantity(quantity):

    if quantity <= 0:
        raise ValueError(
            "Quantity must be greater than zero."
        )


# ==========================================================
# UNIT PRICE
# ==========================================================

def validate_unit_price(price):

    if price <= 0:
        raise ValueError(
            "Unit price must be greater than zero."
        )


# ==========================================================
# STATUS
# ==========================================================

def validate_status(status):

    if status not in PURCHASE_ORDER_STATUS:
        raise ValueError(
            f"Invalid PO Status : {status}"
        )


# ==========================================================
# APPROVAL
# ==========================================================

def validate_approval(status):

    if status not in APPROVAL_STATUS:
        raise ValueError(
            f"Invalid Approval Status : {status}"
        )


# ==========================================================
# SHIPPING
# ==========================================================

def validate_shipping(method):

    if method not in SHIPPING_METHODS:
        raise ValueError(
            f"Invalid Shipping Method : {method}"
        )


# ==========================================================
# PAYMENT TERMS
# ==========================================================

def validate_payment_terms(term):

    if term not in PAYMENT_TERMS:
        raise ValueError(
            f"Invalid Payment Term : {term}"
        )


# ==========================================================
# GST
# ==========================================================

def validate_gst(rate):

    if rate not in GST_RATES:
        raise ValueError(
            f"Invalid GST Rate : {rate}"
        )


# ==========================================================
# TOTALS
# ==========================================================

def validate_total(total):

    if total <= 0:
        raise ValueError(
            "PO Total must be greater than zero."
        )