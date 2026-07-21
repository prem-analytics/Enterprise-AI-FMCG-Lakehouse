"""
GRN Summary Utility

Enterprise AI FMCG Lakehouse
"""


def build_grn_summary(grn_lines):
    """
    Calculate GRN Summary.
    """

    summary = {

        "line_count": len(grn_lines),

        "total_ordered_quantity": 0,

        "total_received_quantity": 0,

        "total_accepted_quantity": 0,

        "total_damaged_quantity": 0,

        "total_short_quantity": 0,

        "total_over_delivery": 0,

        "total_available_stock": 0,

        "total_quality_hold_stock": 0,

        "total_rejected_stock": 0,

        "total_returned_to_vendor": 0,

    }

    for line in grn_lines:

        summary["total_ordered_quantity"] += line["ordered_quantity"]

        summary["total_received_quantity"] += line["received_quantity"]

        summary["total_accepted_quantity"] += line["accepted_quantity"]

        summary["total_damaged_quantity"] += line["damaged_quantity"]

        summary["total_short_quantity"] += line["short_quantity"]

        summary["total_over_delivery"] += line["over_delivery"]

        summary["total_available_stock"] += line["available_stock"]

        summary["total_quality_hold_stock"] += line["quality_hold_stock"]

        summary["total_rejected_stock"] += line["rejected_stock"]

        summary["total_returned_to_vendor"] += line["returned_to_vendor"]

    return summary