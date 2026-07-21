"""
Procurement Status Utility
Enterprise AI FMCG Lakehouse

Business rules for Purchase Order workflow.
"""

import random


# ==========================================================
# STATUS FLOW
# ==========================================================

STATUS_FLOW = {

    "Pending": [
        "Draft",
        "Pending Approval",
    ],

    "Approved": [
        "Approved",
        "Released",
        "Partially Received",
        "Received",
        "Closed",
    ],

    "Rejected": [
        "Cancelled",
    ],
}


# ==========================================================
# GENERATE STATUS
# ==========================================================

def generate_status():
    """
    Generate a valid Approval Status and
    Purchase Order Status combination.
    """

    approval_status = random.choice(
        list(STATUS_FLOW.keys())
    )

    po_status = random.choice(
        STATUS_FLOW[approval_status]
    )

    return {
        "approval_status": approval_status,
        "po_status": po_status,
    }