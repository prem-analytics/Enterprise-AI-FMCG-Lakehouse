from utils.procurement_finance import (
    calculate_discount
)

print("--------------------------------")
print("Percentage Discount")
print("--------------------------------")

print(calculate_discount(
    subtotal=1000,
    discount_percent=10
))

print(calculate_discount(
    subtotal=9999.99,
    discount_percent=5
))

print("--------------------------------")
print("Fixed Discount")
print("--------------------------------")

print(calculate_discount(
    subtotal=1000,
    discount_amount=250
))

print(calculate_discount(
    subtotal=5000,
    discount_amount=999.95
))

print("--------------------------------")
print("No Discount")
print("--------------------------------")

print(calculate_discount(
    subtotal=1000
))

print("--------------------------------")
print("Error Test")
print("--------------------------------")

try:

    print(
        calculate_discount(
            subtotal=1000,
            discount_percent=10,
            discount_amount=100
        )
    )

except Exception as e:

    print(type(e).__name__)
    print(e)

from utils.procurement_finance import calculate_taxable_amount

print("--------------------------------")
print("Taxable Amount")
print("--------------------------------")

print(calculate_taxable_amount(
    subtotal=1000,
    discount=100
))

print(calculate_taxable_amount(
    subtotal=999.99,
    discount=99.99
))

print(calculate_taxable_amount(
    subtotal=500,
    discount=0
))

print("--------------------------------")
print("Negative Protection")
print("--------------------------------")

print(calculate_taxable_amount(
    subtotal=100,
    discount=250
))

from utils.procurement_finance import calculate_gst

print("--------------------------------")
print("GST Calculation")
print("--------------------------------")

print(calculate_gst(
    taxable_amount=1000,
    gst_percent=18
))

print(calculate_gst(
    taxable_amount=999.99,
    gst_percent=5
))

print(calculate_gst(
    taxable_amount=2500,
    gst_percent=12
))

print(calculate_gst(
    taxable_amount=100,
    gst_percent=0
))

print("--------------------------------")
print("GST Validation")
print("--------------------------------")

try:
    print(calculate_gst(
        taxable_amount=1000,
        gst_percent=-5
    ))
except Exception as e:
    print(type(e).__name__)
    print(e)

try:
    print(calculate_gst(
        taxable_amount=1000,
        gst_percent=150
    ))
except Exception as e:
    print(type(e).__name__)
    print(e)

from utils.procurement_finance import calculate_line_total

print("--------------------------------")
print("Line Total - Percentage Discount")
print("--------------------------------")

result = calculate_line_total(
    quantity=100,
    unit_price=25,
    gst_percent=18,
    discount_percent=10
)

for key, value in result.items():
    print(f"{key:20} : {value}")

print("--------------------------------")
print("Line Total - Fixed Discount")
print("--------------------------------")

result = calculate_line_total(
    quantity=20,
    unit_price=99.99,
    gst_percent=5,
    discount_amount=100
)

for key, value in result.items():
    print(f"{key:20} : {value}")

print("--------------------------------")
print("Line Total - No Discount")
print("--------------------------------")

result = calculate_line_total(
    quantity=5,
    unit_price=100,
    gst_percent=12
)

for key, value in result.items():
    print(f"{key:20} : {value}")

from utils.procurement_finance import (
    calculate_line_total,
    calculate_po_totals
)

print("--------------------------------")
print("Purchase Order Totals")
print("--------------------------------")

lines = []

lines.append(
    calculate_line_total(
        quantity=100,
        unit_price=25,
        gst_percent=18,
        discount_percent=10
    )
)

lines.append(
    calculate_line_total(
        quantity=20,
        unit_price=99.99,
        gst_percent=5,
        discount_amount=100
    )
)

lines.append(
    calculate_line_total(
        quantity=5,
        unit_price=100,
        gst_percent=12
    )
)

po_totals = calculate_po_totals(lines)

for key, value in po_totals.items():
    print(f"{key:25} : {value}")