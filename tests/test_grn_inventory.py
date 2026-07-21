from pprint import pprint

from utils.grn.inventory import update_inventory

statuses = [
    "PASS",
    "HOLD",
    "FAIL",
    "RTV",
]

for status in statuses:

    print(f"\nInventory Result ({status})")

    pprint(
        update_inventory(
            accepted_quantity=100,
            inspection_status=status,
        )
    )