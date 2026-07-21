"""
Goods Receipt Number Generator

Enterprise AI FMCG Lakehouse
"""

from utils.common.id_generator import generate_id

_grn_counter = 1


def generate_grn_number():
    """
    Generate a unique Goods Receipt Number.

    Example:
        GRN000001
    """

    global _grn_counter

    grn_number = generate_id(
        prefix="GRN",
        number=_grn_counter,
    )

    _grn_counter += 1

    return grn_number