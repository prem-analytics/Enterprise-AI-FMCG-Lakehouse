from pprint import pprint

from utils.procurement.purchase_order import build_purchase_order

po = build_purchase_order()

print("=" * 80)
print("METADATA")
print("=" * 80)
pprint(po["metadata"])

print("\n" + "=" * 80)
print("HEADER")
print("=" * 80)
pprint(po["header"])

print("\n" + "=" * 80)
print("SUMMARY")
print("=" * 80)
pprint(po["summary"])

print("\n" + "=" * 80)
print("LINES")
print("=" * 80)

for line in po["lines"]:
    pprint(line)
    print("-" * 80)
