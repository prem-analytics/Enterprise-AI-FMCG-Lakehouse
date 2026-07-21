from datetime import datetime
from pprint import pprint

from utils.grn.numbering import (
    generate_grn_number,
)

from utils.grn.dates import (
    generate_receipt_date,
    generate_posting_date,
    generate_inventory_date,
)

from utils.grn.receipt import (
    build_receipt,
)


# ============================================
# Test GRN Number
# ============================================

grn_number = generate_grn_number()


# ============================================
# Test Dates
# ============================================

order_date = datetime(2026, 7, 1)
expected_delivery = datetime(2026, 7, 5)

receipt_date = generate_receipt_date(
    order_date,
    expected_delivery,
)

posting_date = generate_posting_date(
    receipt_date,
)

inventory_date = generate_inventory_date(
    posting_date,
)


# ============================================
# Test Receipt
# ============================================

receipt = build_receipt(
    ordered_quantity=100,
)


# ============================================
# Display Result
# ============================================

print("=" * 60)
print("GOODS RECEIPT NOTE TEST")
print("=" * 60)

print(f"GRN Number       : {grn_number}")
print(f"Order Date       : {order_date}")
print(f"Expected Date    : {expected_delivery}")
print(f"Receipt Date     : {receipt_date}")
print(f"Posting Date     : {posting_date}")
print(f"Inventory Date   : {inventory_date}")

print("\nReceipt Summary")
print("-" * 60)

pprint(receipt)

print("=" * 60)