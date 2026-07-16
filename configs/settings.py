"""
Enterprise AI FMCG Lakehouse
Global Project Settings
"""

# ==========================================================
# MASTER DATA CONFIGURATION
# ==========================================================

# Customer Master
CUSTOMER_COUNT = 100_000

# Product Master
PRODUCT_COUNT = 5_000

# Store Master
STORE_COUNT = 1_000

# Supplier Master
SUPPLIER_COUNT = 500

# Factory Master
FACTORY_COUNT = 10

# Warehouse Master
WAREHOUSE_COUNT = 100

# Employee Master
EMPLOYEE_COUNT = 5_000


# ==========================================================
# TRANSACTION DATA CONFIGURATION
# ==========================================================

# Sales Transactions
SALES_COUNT = 5_000_000

# Inventory Records
INVENTORY_COUNT = 1_000_000

# Purchase Orders
PURCHASE_ORDER_COUNT = 500_000

# Shipments
SHIPMENT_COUNT = 500_000

# Production Orders
PRODUCTION_COUNT = 250_000

# Marketing Campaigns
MARKETING_COUNT = 10_000


# ==========================================================
# COUNTRY SETTINGS
# ==========================================================

COUNTRY = "India"

CURRENCY = "INR"

TIMEZONE = "Asia/Kolkata"

DATE_FORMAT = "%Y-%m-%d"


# ==========================================================
# OUTPUT SETTINGS
# ==========================================================

OUTPUT_FORMAT = "parquet"

SAVE_CSV = True

SAVE_PARQUET = True

GENERATE_METADATA = True

GENERATE_SAMPLE = True

VALIDATE_DATA = True


# ==========================================================
# RANDOM SEED
# ==========================================================

# Set to None for different data every run.
# Set to a fixed value (e.g. 42) for reproducible datasets.
RANDOM_SEED = 42