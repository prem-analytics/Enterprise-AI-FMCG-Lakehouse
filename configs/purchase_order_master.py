"""
Purchase Order Master Configuration
Enterprise AI FMCG Lakehouse

This file centralizes all procurement business rules.
"""

# ==========================================================
# PURCHASE ORDER STATUS
# ==========================================================

PURCHASE_ORDER_STATUS = [
    "Draft",
    "Pending Approval",
    "Approved",
    "Released",
    "Partially Received",
    "Received",
    "Closed",
    "Cancelled"
]

# ==========================================================
# APPROVAL STATUS
# ==========================================================

APPROVAL_STATUS = [
    "Pending",
    "Approved",
    "Rejected"
]

# ==========================================================
# PAYMENT TERMS
# ==========================================================

PAYMENT_TERMS = {

    "Advance 100%": 0,
    "Net 7": 7,
    "Net 15": 15,
    "Net 30": 30,
    "Net 45": 45,
    "Net 60": 60,
    "Net 90": 90

}

# ==========================================================
# CURRENCY
# ==========================================================

CURRENCIES = [

    "INR"

]

# ==========================================================
# SHIPPING METHODS
# ==========================================================

SHIPPING_METHODS = [

    "Road",
    "Rail",
    "Air",
    "Sea"

]

# ==========================================================
# INCOTERMS
# ==========================================================

INCOTERMS = [

    "EXW",
    "FCA",
    "FOB",
    "CIF",
    "DAP",
    "DDP"

]

# ==========================================================
# TAX RATES
# ==========================================================

GST_RATES = [

    0,
    5,
    12,
    18,
    28

]

# ==========================================================
# FREIGHT RANGE
# ==========================================================

FREIGHT_RANGE = (

    0,
    25000

)

# ==========================================================
# DISCOUNT RANGE (%)
# ==========================================================

DISCOUNT_RANGE = (

    0,
    15

)

# ==========================================================
# PURCHASE PRIORITY
# ==========================================================

PURCHASE_PRIORITY = [

    "Low",
    "Medium",
    "High",
    "Critical"

]

# ==========================================================
# DELIVERY STATUS
# ==========================================================

DELIVERY_STATUS = [

    "Pending",
    "In Transit",
    "Delivered",
    "Delayed"

]

# ==========================================================
# PROCUREMENT CATEGORY
# ==========================================================

PROCUREMENT_CATEGORY = [

    "Raw Material",
    "Packaging Material",
    "Finished Goods",
    "Consumables",
    "Engineering",
    "Office Supplies",
    "Services"

]

# ==========================================================
# PURCHASE TYPE
# ==========================================================

PURCHASE_TYPE = [

    "Local",
    "Import"

]

# ==========================================================
# QUALITY INSPECTION
# ==========================================================

QUALITY_STATUS = [

    "Pending",
    "Passed",
    "Failed",
    "Partially Passed"

]

# ==========================================================
# RECEIVING TYPE
# ==========================================================

RECEIVING_STATUS = [

    "Pending",
    "Partial",
    "Completed"

]

# ==========================================================
# PROCUREMENT CONSTANTS
# ==========================================================

MIN_PO_LINES = 3
MAX_PO_LINES = 20

MIN_QTY_PER_LINE = 10
MAX_QTY_PER_LINE = 5000

LEAD_TIME_DAYS = (

    2,
    45

)

PO_NUMBER_PREFIX = "PO"

GRN_NUMBER_PREFIX = "GRN"

INVOICE_PREFIX = "PINV"

DEFAULT_COUNTRY = "India"

DEFAULT_CURRENCY = "INR"