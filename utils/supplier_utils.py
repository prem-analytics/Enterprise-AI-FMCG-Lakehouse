"""
Enterprise Supplier Utility
"""

import random
import string

from configs.supplier_master import (
    SUPPLIER_TYPES,
    PAYMENT_TERMS,
    CURRENCIES,
    SUPPLIER_STATUS,
    SUPPLIER_PREFIX,
    SUPPLIER_SUFFIX
)


def random_supplier_name():
    """
    Generate supplier name.
    """

    return (
        f"{random.choice(SUPPLIER_PREFIX)} "
        f"{random.choice(SUPPLIER_SUFFIX)}"
    )


def random_supplier_type():
    """
    Random supplier type.
    """

    return random.choice(SUPPLIER_TYPES)


def random_supplier_email(supplier_name):
    """
    Generate supplier email.
    """

    email = (
        supplier_name.lower()
        .replace(" ", "")
        .replace("&", "")
    )

    return f"{email}@supplier.com"


def random_supplier_phone():
    """
    Generate Indian phone number.
    """

    return (
        f"+91 "
        f"{random.randint(6000000000, 9999999999)}"
    )


def random_payment_term():
    """
    Random payment term.
    """

    return random.choice(PAYMENT_TERMS)


def random_currency():
    """
    Random currency.
    """

    return random.choice(CURRENCIES)


def random_supplier_status():
    """
    Random supplier status.
    """

    return random.choice(SUPPLIER_STATUS)


def random_supplier_rating():
    """
    Supplier rating.
    """

    return round(random.uniform(3.0, 5.0), 1)


def random_lead_time():
    """
    Lead time in days.
    """

    return random.randint(3, 30)


def random_preferred_supplier():
    """
    Preferred supplier flag.
    """

    return random.choice([True, False])


def random_pan():
    """
    Generate PAN number.
    """

    letters = "".join(
        random.choices(string.ascii_uppercase, k=5)
    )

    numbers = "".join(
        random.choices(string.digits, k=4)
    )

    last = random.choice(string.ascii_uppercase)

    return f"{letters}{numbers}{last}"


def random_gstin():
    """
    Generate GSTIN.
    """

    state = str(random.randint(1, 37)).zfill(2)

    pan = random_pan()

    return f"{state}{pan}1Z5"