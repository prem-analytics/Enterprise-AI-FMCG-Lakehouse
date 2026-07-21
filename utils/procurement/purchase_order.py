"""
Purchase Order Utility
Enterprise AI FMCG Lakehouse
"""

# ==========================================================
# IMPORTS
# ==========================================================

from random import choice

from configs.purchase_order_master import (
    PAYMENT_TERMS,
    SHIPPING_METHODS,
    CURRENCIES,
)

from utils.common.document import build_document

from utils.procurement.lines import (
    generate_purchase_order_lines,
)

from utils.procurement.numbering import (
    generate_po_number,
)

from utils.procurement.selection import (
    get_supplier,
    get_buyer,
    get_factory,
    get_warehouse,
)

from utils.procurement.dates import (
    generate_order_date,
    generate_expected_delivery_date,
)

from utils.procurement.status import (
    generate_status,
)

from utils.procurement.finance import (
    calculate_po_totals,
)

# ==========================================================
# PURCHASE ORDER BUILDER
# ==========================================================


def build_purchase_order():

    supplier = get_supplier()
    buyer = get_buyer()
    factory = get_factory()
    warehouse = get_warehouse()

    order_date = generate_order_date()

    delivery_date = generate_expected_delivery_date(
        order_date
    )

    payment_term = choice(
        list(PAYMENT_TERMS.keys())
    )

    status = generate_status()

    lines = generate_purchase_order_lines()

    totals = calculate_po_totals(lines)

    # ======================================================
    # HEADER
    # ======================================================

    header = {

        "po_number": generate_po_number(),

        # Supplier

        "supplier_id": supplier["supplier_id"],
        "supplier_name": supplier["supplier_name"],

        # Buyer

        "buyer_id": buyer["employee_id"],
        "buyer_name": buyer["full_name"],
        "buyer_department": buyer["department"],

        # Factory

        "factory_id": factory["factory_id"],
        "factory_name": factory["factory_name"],

        # Warehouse

        "warehouse_id": warehouse["warehouse_id"],
        "warehouse_name": warehouse["warehouse_name"],

        # Dates

        "order_date": order_date,

        "expected_delivery_date": delivery_date,

        # Commercial

        "payment_terms": payment_term,

        "payment_days": PAYMENT_TERMS[payment_term],

        "currency": choice(CURRENCIES),

        "shipping_method": choice(
            SHIPPING_METHODS
        ),

        # Status

        # Business Status

        "business_status": status["po_status"],

    }

    # ======================================================
    # SUMMARY
    # ======================================================

    summary = {

        "line_count": totals["line_count"],

        "total_subtotal": totals["total_subtotal"],

        "total_discount": totals["total_discount"],

        "total_taxable_amount": totals["total_taxable_amount"],

        "total_gst": totals["total_gst"],

        "grand_total": totals["grand_total"],

    }

    # ======================================================
    # DOCUMENT
    # ======================================================

    return build_document(

        document_type="PURCHASE_ORDER",

        header=header,

        lines=lines,

        summary=summary,

        document_status="POSTED",

        approval_status=status["approval_status"],

    )