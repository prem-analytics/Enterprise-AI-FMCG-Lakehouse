"""
Inventory Update Utility

Enterprise AI FMCG Lakehouse
"""


# ==========================================================
# INVENTORY UPDATE
# ==========================================================

def update_inventory(
    accepted_quantity,
    inspection_status,
):
    """
    Determine how inventory should be updated
    after quality inspection.
    """

    inventory = {
        "available_stock": 0,
        "quality_hold_stock": 0,
        "rejected_stock": 0,
        "returned_to_vendor": 0,
    }

    if inspection_status == "PASS":
        inventory["available_stock"] = accepted_quantity

    elif inspection_status == "HOLD":
        inventory["quality_hold_stock"] = accepted_quantity

    elif inspection_status == "FAIL":
        inventory["rejected_stock"] = accepted_quantity

    elif inspection_status == "RTV":
        inventory["returned_to_vendor"] = accepted_quantity

    return inventory