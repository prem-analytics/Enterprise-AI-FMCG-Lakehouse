from datetime import datetime

from utils.grn.dates import (
    generate_receipt_date,
    generate_posting_date,
    generate_inventory_date,
)

order_date = datetime(2026, 7, 1)
expected_delivery = datetime(2026, 7, 5)

receipt = generate_receipt_date(
    order_date,
    expected_delivery,
)

posting = generate_posting_date(receipt)

inventory = generate_inventory_date(posting)

print("Order Date       :", order_date)
print("Expected Delivery:", expected_delivery)
print("Receipt Date     :", receipt)
print("Posting Date     :", posting)
print("Inventory Date   :", inventory)