from pprint import pprint

from utils.procurement.purchase_order import build_purchase_order
from utils.grn.builder import build_grn

purchase_order = build_purchase_order()

grn = build_grn(purchase_order)

print("=" * 80)
print("METADATA")
print("=" * 80)
pprint(grn["metadata"])

print("\n" + "=" * 80)
print("GRN HEADER")
print("=" * 80)
pprint(grn["header"])

print("\n" + "=" * 80)
print("GRN SUMMARY")
print("=" * 80)
pprint(grn["summary"])

print("\n" + "=" * 80)
print("GRN LINES")
print("=" * 80)

for line in grn["lines"]:
    pprint(line)
    print("-" * 80)