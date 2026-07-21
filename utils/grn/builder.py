"""
Enterprise Goods Receipt Builder

Enterprise AI FMCG Lakehouse
"""

from utils.grn.numbering import generate_grn_number

from utils.grn.dates import (
    generate_receipt_date,
    generate_posting_date,
    generate_inventory_date,
)

from utils.grn.line_builder import build_grn_line
from utils.grn.summary import build_grn_summary

from utils.common.document import build_document


def build_grn(purchase_order):
    """
    Build a complete GRN from a Purchase Order.
    """

    # ==========================================================
    # PURCHASE ORDER REFERENCES
    # ==========================================================

    po_header = purchase_order["header"]
    po_lines = purchase_order["lines"]

    # ==========================================================
    # DATES
    # ==========================================================

    receipt_date = generate_receipt_date(
        po_header["order_date"],
        po_header["expected_delivery_date"],
    )

    posting_date = generate_posting_date(
        receipt_date,
    )

    inventory_date = generate_inventory_date(
        posting_date,
    )

    # ==========================================================
    # GRN LINES
    # ==========================================================

    grn_lines = []

    for po_line in po_lines:

        grn_line = build_grn_line(po_line)

        grn_lines.append(grn_line)

    # ==========================================================
    # SUMMARY
    # ==========================================================

    summary = build_grn_summary(
        grn_lines
    )

    # ==========================================================
    # HEADER
    # ==========================================================

    header = {

        "grn_number": generate_grn_number(),

        "po_number": po_header["po_number"],

        "supplier_id": po_header["supplier_id"],
        "supplier_name": po_header["supplier_name"],

        "factory_id": po_header["factory_id"],
        "factory_name": po_header["factory_name"],

        "warehouse_id": po_header["warehouse_id"],
        "warehouse_name": po_header["warehouse_name"],

        "receipt_date": receipt_date,

        "posting_date": posting_date,

        "inventory_date": inventory_date,

        # Business Status
        "business_status": "Accepted",

    }

    # ==========================================================
    # DOCUMENT
    # ==========================================================

    return build_document(

        document_type="GRN",

        header=header,

        lines=grn_lines,

        summary=summary,

        document_status="POSTED",

        approval_status="APPROVED",

    )