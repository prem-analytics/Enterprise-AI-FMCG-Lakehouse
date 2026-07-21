"""
Enterprise GRN Line Builder

Enterprise AI FMCG Lakehouse
"""

from utils.grn.receipt import build_receipt
from utils.grn.inspection import build_inspection
from utils.grn.inventory import update_inventory


def build_grn_line(po_line):
    """
    Build one GRN line from one Purchase Order line.
    """

    receipt = build_receipt(
        ordered_quantity=po_line["quantity"],
    )

    inspection = build_inspection()

    inventory = update_inventory(
        accepted_quantity=receipt["accepted_quantity"],
        inspection_status=inspection["inspection_status"],
    )

    return {

        # -------------------------
        # PO Information
        # -------------------------

        "line_number": po_line["line_number"],

        "product_id": po_line["product_id"],

        "product_name": po_line["product_name"],

        "sku": po_line["sku"],

        # -------------------------
        # Receipt
        # -------------------------

        "ordered_quantity": receipt["ordered_quantity"],

        "received_quantity": receipt["received_quantity"],

        "accepted_quantity": receipt["accepted_quantity"],

        "damaged_quantity": receipt["damaged_quantity"],

        "short_quantity": receipt["short_quantity"],

        "over_delivery": receipt["over_delivery"],

        # -------------------------
        # Inspection
        # -------------------------

        "inspection_status": inspection["inspection_status"],

        "quality_score": inspection["quality_score"],

        "inspection_reason": inspection["reason"],

        # -------------------------
        # Inventory
        # -------------------------

        "available_stock": inventory["available_stock"],

        "quality_hold_stock": inventory["quality_hold_stock"],

        "rejected_stock": inventory["rejected_stock"],

        "returned_to_vendor": inventory["returned_to_vendor"],

    }