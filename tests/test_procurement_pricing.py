from utils.procurement_pricing import *

qty = generate_quantity()

price = generate_unit_price()

subtotal = calculate_line_total(
    qty,
    price
)

discount, discount_pct = calculate_discount(
    subtotal
)

gst, gst_rate = calculate_gst(
    subtotal - discount
)

freight = calculate_freight(
    "Road"
)

total = calculate_po_total(
    subtotal,
    discount,
    gst,
    freight
)

print(f"Quantity        : {qty}")
print(f"Unit Price      : {price}")
print(f"Subtotal        : {subtotal}")
print(f"Discount %      : {discount_pct}")
print(f"Discount Amount : {discount}")
print(f"GST Rate        : {gst_rate}")
print(f"GST Amount      : {gst}")
print(f"Freight         : {freight}")
print(f"Grand Total     : {total}")