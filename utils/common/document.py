"""
Common ERP Document Builder
Enterprise AI FMCG Lakehouse
"""

from utils.common.document_metadata import (
    build_document_metadata,
)


def build_document(
    document_type,
    header,
    lines,
    summary,
    document_status="POSTED",
    approval_status="APPROVED",
):

    metadata = build_document_metadata(
        document_type=document_type,
        document_status=document_status,
        approval_status=approval_status,
    )

    return {

        "metadata": metadata,

        "header": header,

        "lines": lines,

        "summary": summary,

    }