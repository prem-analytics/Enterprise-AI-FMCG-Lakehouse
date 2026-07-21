"""
Quality Inspection Utility

Enterprise AI FMCG Lakehouse
"""

from random import choices


# ==========================================================
# INSPECTION STATUS
# ==========================================================

def generate_inspection_status():
    """
    Generate inspection result.

    PASS  : Goods accepted
    HOLD  : Waiting for QA
    FAIL  : Rejected
    RTV   : Return to Vendor
    """

    return choices(
        population=[
            "PASS",
            "HOLD",
            "FAIL",
            "RTV",
        ],
        weights=[
            88,   # Most deliveries pass
            6,
            4,
            2,
        ],
        k=1,
    )[0]


# ==========================================================
# QUALITY SCORE
# ==========================================================

def generate_quality_score(status):
    """
    Quality score (0-100)
    """

    if status == "PASS":
        return 100

    if status == "HOLD":
        return 85

    if status == "FAIL":
        return 45

    return 20


# ==========================================================
# REJECTION REASON
# ==========================================================

def generate_rejection_reason(status):

    if status == "PASS":
        return None

    reasons = [
        "Packaging Damaged",
        "Expired Product",
        "Wrong Product",
        "Wrong Quantity",
        "Leakage",
        "Broken Seal",
        "Failed Quality Test",
    ]

    from random import choice

    return choice(reasons)


# ==========================================================
# BUILD INSPECTION
# ==========================================================

def build_inspection():

    status = generate_inspection_status()

    return {
        "inspection_status": status,
        "quality_score": generate_quality_score(status),
        "reason": generate_rejection_reason(status),
    }