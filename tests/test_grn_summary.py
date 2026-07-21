from pprint import pprint

from utils.grn.line_builder import build_grn_line
from utils.grn.summary import build_grn_summary

po_lines = [
    {
        "line_number": 1,
        "product_id": "PROD001",
        "product_name": "Milk",
        "sku": "SKU001",
        "quantity": 100,
    },
    {
        "line_number": 2,
        "product_id": "PROD002",
        "product_name": "Tea",
        "sku": "SKU002",
        "quantity": 200,
    },
    {
        "line_number": 3,
        "product_id": "PROD003",
        "product_name": "Coffee",
        "sku": "SKU003",
        "quantity": 300,
    },
]

grn_lines = [
    build_grn_line(line)
    for line in po_lines
]

print("GRN Lines")
pprint(grn_lines)

print("\nSummary")
pprint(build_grn_summary(grn_lines))