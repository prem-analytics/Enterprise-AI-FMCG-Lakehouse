"""
Procurement Line Item Utility
Enterprise AI FMCG Lakehouse

Generates Purchase Order Line Items.
"""

from random import randint, choice

from utils.procurement.selection import (
    get_products,
)

from utils.procurement.pricing import (
    generate_quantity,
)

from utils.procurement.finance import (
    calculate_line_total,
)


# ==========================================================
# GENERATE LINE ITEMS
# ==========================================================

def generate_purchase_order_lines():
    """
    Generate random products for one Purchase Order.
    """

    number_of_lines = randint(1, 8)

    products = get_products(number_of_lines)

    line_items = []

    for line_number, product in enumerate(products, start=1):

        quantity = generate_quantity()

        unit_price = float(product["cost_price"])

        gst_percent = choice([0, 5, 12, 18, 28])

        financials = calculate_line_total(
            quantity=quantity,
            unit_price=unit_price,
            gst_percent=gst_percent,
            discount_percent=None,
            discount_amount=None,       
        )

        line_items.append({

            "line_number": line_number,

            "product_id": product["product_id"],

            "sku": product["sku"],

            "product_name": product["product_name"],

            "brand": product["brand"],

            "category": product["category"],

            "package_size": product["package_size"],

            "uom": product["uom"],

            "quantity": quantity,

            "unit_price": round(unit_price, 2),

            "subtotal": financials["subtotal"],

            "discount": financials["discount"],

            "taxable_amount": financials["taxable_amount"],

            "gst_percent": gst_percent,

            "gst_amount": financials["gst_amount"],

            "line_total": financials["line_total"],

        })

    return line_items