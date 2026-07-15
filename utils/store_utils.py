"""
Enterprise Store Utility
"""

import random

from configs.store_master import (
    STORE_TYPES,
    STORE_PREFIX,
    STORE_SUFFIX
)


def random_store_name():
    """
    Generate a realistic store name.
    """

    return (
        f"{random.choice(STORE_PREFIX)} "
        f"{random.choice(STORE_SUFFIX)}"
    )


def random_store_type():
    """
    Random store type.
    """

    return random.choice(STORE_TYPES)


def random_store_email(store_name):
    """
    Generate store email.
    """

    email = (
        store_name.lower()
        .replace(" ", "")
        .replace("&", "")
    )

    return f"{email}@enterprisefmcg.com"


def random_store_phone():
    """
    Generate Indian mobile number.
    """

    return (
        f"+91 "
        f"{random.randint(6000000000, 9999999999)}"
    )