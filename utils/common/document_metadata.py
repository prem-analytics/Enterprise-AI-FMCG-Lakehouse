"""
Common Document Metadata
Enterprise AI FMCG Lakehouse
"""

from datetime import datetime


def build_document_metadata(
    document_type,
    document_status="POSTED",
    approval_status="APPROVED",
    company="Enterprise AI FMCG",
    country="India",
    currency="INR",
    created_by="SYSTEM",
):

    now = datetime.now()

    return {

        "document_type": document_type,

        "document_version": "1.0",

        # ======================================================
        # SYSTEM STATUS
        # ======================================================

        "document_status": document_status,

        "approval_status": approval_status,

        # ======================================================
        # COMPANY
        # ======================================================

        "company": company,

        "country": country,

        "currency": currency,

        # ======================================================
        # AUDIT
        # ======================================================

        "created_by": created_by,

        "created_at": now,

        "last_updated": now,

    }