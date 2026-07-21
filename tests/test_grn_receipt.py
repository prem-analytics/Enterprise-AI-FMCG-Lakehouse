from pprint import pprint

from utils.grn.receipt import (
    build_receipt,
)

receipt = build_receipt(
    ordered_quantity=100,
)

pprint(receipt)