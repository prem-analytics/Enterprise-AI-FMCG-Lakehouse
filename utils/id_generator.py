"""
ID Generator Utility

Generates enterprise-standard IDs.
"""


def generate_id(prefix: str, number: int, width: int = 6) -> str:
    """
    Generate formatted IDs.

    Example:
        generate_id("CUST", 1)
        -> CUST000001
    """

    return f"{prefix}{number:0{width}d}"