"""
Enterprise Procurement Financial Calculations
"""

from decimal import Decimal, ROUND_HALF_UP


def round_money(value):
    """
    Round monetary values to 2 decimal places using
    Decimal arithmetic.
    """
    return float(
        Decimal(str(value)).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP
        )
    )


def calculate_subtotal(quantity, unit_price):
    """
    Calculate line subtotal.

    Formula:
        Quantity × Unit Price
    """

    subtotal = (
        Decimal(str(quantity))
        * Decimal(str(unit_price))
    )

    return round_money(subtotal)

def calculate_discount(
    subtotal,
    discount_percent=None,
    discount_amount=None
):
    """
    Calculate discount for a procurement line.

    Rules
    -----
    1. Only ONE discount type is allowed.
    2. Percentage discount takes subtotal × percent / 100.
    3. Fixed discount uses supplied amount.
    4. If no discount supplied -> 0.00
    """

    if discount_percent is not None and discount_amount is not None:
        raise ValueError(
            "Provide either discount_percent OR discount_amount, not both."
        )

    subtotal = Decimal(str(subtotal))

    if discount_percent is not None:

        discount = (
            subtotal
            * Decimal(str(discount_percent))
            / Decimal("100")
        )

        return round_money(discount)

    if discount_amount is not None:
        return round_money(discount_amount)

    return 0.00

def calculate_taxable_amount(
    subtotal,
    discount=0
):
    """
    Calculate taxable amount after discount.

    Formula:
        Taxable Amount = Subtotal - Discount

    Taxable amount cannot be negative.
    """

    subtotal = Decimal(str(subtotal))
    discount = Decimal(str(discount))

    taxable = subtotal - discount

    if taxable < Decimal("0"):
        taxable = Decimal("0")

    return round_money(taxable)

def calculate_gst(
    taxable_amount,
    gst_percent
):
    """
    Calculate GST amount.

    Formula:
        GST = Taxable Amount × GST % / 100

    Business Rules
    --------------
    - GST cannot be negative.
    - GST percentage cannot exceed 100.
    """

    taxable_amount = Decimal(str(taxable_amount))
    gst_percent = Decimal(str(gst_percent))

    if gst_percent < Decimal("0"):
        raise ValueError(
            "GST percentage cannot be negative."
        )

    if gst_percent > Decimal("100"):
        raise ValueError(
            "GST percentage cannot exceed 100."
        )

    gst = (
        taxable_amount
        * gst_percent
        / Decimal("100")
    )

    return round_money(gst)

def calculate_line_total(
    quantity,
    unit_price,
    gst_percent,
    discount_percent=None,
    discount_amount=None
):
    """
    Calculate complete financial details for one purchase order line.
    """

    subtotal = calculate_subtotal(
        quantity,
        unit_price
    )

    discount = calculate_discount(
        subtotal=subtotal,
        discount_percent=discount_percent,
        discount_amount=discount_amount
    )

    taxable_amount = calculate_taxable_amount(
        subtotal,
        discount
    )

    gst_amount = calculate_gst(
        taxable_amount,
        gst_percent
    )

    line_total = round_money(
        taxable_amount + gst_amount
    )

    return {
        "subtotal": subtotal,
        "discount": discount,
        "taxable_amount": taxable_amount,
        "gst_amount": gst_amount,
        "line_total": line_total
    }

def calculate_po_totals(line_items):
    """
    Calculate overall Purchase Order totals.

    Parameters
    ----------
    line_items : list[dict]
        Each dictionary must contain:
            subtotal
            discount
            taxable_amount
            gst_amount
            line_total

    Returns
    -------
    dict
    """

    total_subtotal = Decimal("0")
    total_discount = Decimal("0")
    total_taxable = Decimal("0")
    total_gst = Decimal("0")
    grand_total = Decimal("0")

    for line in line_items:

        total_subtotal += Decimal(str(line["subtotal"]))
        total_discount += Decimal(str(line["discount"]))
        total_taxable += Decimal(str(line["taxable_amount"]))
        total_gst += Decimal(str(line["gst_amount"]))
        grand_total += Decimal(str(line["line_total"]))

    return {
        "total_subtotal": round_money(total_subtotal),
        "total_discount": round_money(total_discount),
        "total_taxable_amount": round_money(total_taxable),
        "total_gst": round_money(total_gst),
        "grand_total": round_money(grand_total),
        "line_count": len(line_items)
    }