from utils.procurement_selection import *

print("\nSupplier")
print(get_supplier())

print("\nBuyer")
print(get_buyer())

print("\nFactory")
print(get_factory())

print("\nWarehouse")
print(get_warehouse())

print("\nProducts")

for product in get_products():
    print(product["product_name"])