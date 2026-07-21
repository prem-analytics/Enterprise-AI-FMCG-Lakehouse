"""
Goods Receipt Calculation Utility
Enterprise AI FMCG Lakehouse

Calculates the actual quantities received against
a Purchase Order.
"""

from random import randint


# ==========================================================
# RECEIVED QUANTITY
# ==========================================================

def generate_received_quantity(
    ordered_quantity,
):
    """
    Generate actual received quantity.

    Business Rules
    --------------
    • Usually supplier delivers everything.
    • Sometimes short shipment.
    • Small over-delivery is allowed.
    """

    variation = randint(-5, 3)

    received = ordered_quantity + variation

    if received < 0:
        received = 0

    return received


# ==========================================================
# DAMAGED QUANTITY
# ==========================================================

def generate_damaged_quantity(
    received_quantity,
):
    """
    Random damaged quantity.
    """

    if received_quantity == 0:
        return 0

    return randint(0, min(3, received_quantity))


# ==========================================================
# ACCEPTED QUANTITY
# ==========================================================

def calculate_accepted_quantity(
    received_quantity,
    damaged_quantity,
):
    """
    Accepted stock.
    """

    return max(
        received_quantity - damaged_quantity,
        0,
    )


# ==========================================================
# SHORT QUANTITY
# ==========================================================

def calculate_short_quantity(
    ordered_quantity,
    received_quantity,
):
    """
    Short supplied quantity.
    """

    return max(
        ordered_quantity - received_quantity,
        0,
    )


# ==========================================================
# OVER DELIVERY
# ==========================================================

def calculate_over_delivery(
    ordered_quantity,
    received_quantity,
):
    """
    Quantity received above PO.
    """

    return max(
        received_quantity - ordered_quantity,
        0,
    )


# ==========================================================
# BUILD RECEIPT SUMMARY
# ==========================================================

def build_receipt(
    ordered_quantity,
):
    """
    Generate complete GRN receipt summary.
    """

    received_quantity = generate_received_quantity(
        ordered_quantity,
    )

    damaged_quantity = generate_damaged_quantity(
        received_quantity,
    )

    accepted_quantity = calculate_accepted_quantity(
        received_quantity,
        damaged_quantity,
    )

    short_quantity = calculate_short_quantity(
        ordered_quantity,
        received_quantity,
    )

    over_delivery = calculate_over_delivery(
        ordered_quantity,
        received_quantity,
    )

    return {
        "ordered_quantity": ordered_quantity,
        "received_quantity": received_quantity,
        "accepted_quantity": accepted_quantity,
        "damaged_quantity": damaged_quantity,
        "short_quantity": short_quantity,
        "over_delivery": over_delivery,
    }