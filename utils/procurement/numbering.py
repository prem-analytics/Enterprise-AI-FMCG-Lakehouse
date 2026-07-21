"""
Procurement Numbering Utility
Enterprise AI FMCG Lakehouse

Generates unique business document numbers for
Purchase Orders, Goods Receipts, Supplier Invoices,
Vendor Payments and Purchase Requisitions.
"""

from datetime import datetime


# ==========================================================
# DOCUMENT PREFIXES
# ==========================================================

PO_PREFIX = "PO"
PR_PREFIX = "PR"
GRN_PREFIX = "GRN"
PINV_PREFIX = "PINV"
PAY_PREFIX = "PAY"

CURRENT_YEAR = datetime.now().year


# ==========================================================
# INTERNAL COUNTERS
# ==========================================================

_po_counter = 1
_pr_counter = 1
_grn_counter = 1
_invoice_counter = 1
_payment_counter = 1


# ==========================================================
# PRIVATE FORMATTER
# ==========================================================

def _format_document_number(prefix: str, counter: int) -> str:
    """
    Format document numbers.

    Example
    -------
    PO202600000001
    """

    return f"{prefix}{CURRENT_YEAR}{counter:08d}"


# ==========================================================
# PURCHASE REQUISITION
# ==========================================================

def generate_pr_number() -> str:
    global _pr_counter

    number = _format_document_number(
        PR_PREFIX,
        _pr_counter
    )

    _pr_counter += 1

    return number


# ==========================================================
# PURCHASE ORDER
# ==========================================================

def generate_po_number() -> str:
    global _po_counter

    number = _format_document_number(
        PO_PREFIX,
        _po_counter
    )

    _po_counter += 1

    return number


# ==========================================================
# GOODS RECEIPT
# ==========================================================

def generate_grn_number() -> str:
    global _grn_counter

    number = _format_document_number(
        GRN_PREFIX,
        _grn_counter
    )

    _grn_counter += 1

    return number


# ==========================================================
# SUPPLIER INVOICE
# ==========================================================

def generate_supplier_invoice_number() -> str:
    global _invoice_counter

    number = _format_document_number(
        PINV_PREFIX,
        _invoice_counter
    )

    _invoice_counter += 1

    return number


# ==========================================================
# VENDOR PAYMENT
# ==========================================================

def generate_payment_number() -> str:
    global _payment_counter

    number = _format_document_number(
        PAY_PREFIX,
        _payment_counter
    )

    _payment_counter += 1

    return number


# ==========================================================
# RESET COUNTERS
# ==========================================================

def reset_counters():
    """
    Used for testing.
    """

    global _po_counter
    global _pr_counter
    global _grn_counter
    global _invoice_counter
    global _payment_counter

    _po_counter = 1
    _pr_counter = 1
    _grn_counter = 1
    _invoice_counter = 1
    _payment_counter = 1