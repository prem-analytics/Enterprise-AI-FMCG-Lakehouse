from pprint import pprint

from utils.grn.line_builder import (
    build_grn_line,
)

po_line = {

    "line_number": 1,

    "product_id": "PROD001",

    "product_name": "Milk",

    "sku": "SKU001",

    "quantity": 100,
}

line = build_grn_line(
    po_line,
)

pprint(line)