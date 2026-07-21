"""
Enterprise Factory Utility
"""

import random

from utils.common.faker_utils import random_name

from configs.factory_master import (
    FACTORY_TYPES,
    FACTORY_PREFIX,
    FACTORY_SUFFIX,
    SHIFT_TYPES,
    FACTORY_STATUS,
    PRODUCTION_LINES
)


def random_factory_name():
    """
    Generate factory name.
    """

    return (
        f"{random.choice(FACTORY_PREFIX)} "
        f"{random.choice(FACTORY_SUFFIX)}"
    )


def random_factory_code(number):
    """
    Generate factory code.
    """

    return f"FAC-{number:03d}"


def random_factory_type():
    """
    Factory type.
    """

    return random.choice(FACTORY_TYPES)


def random_shift():
    """
    Factory shift.
    """

    return random.choice(SHIFT_TYPES)


def random_status():
    """
    Factory status.
    """

    return random.choice(FACTORY_STATUS)


def random_production_lines():
    """
    Number of production lines.
    """

    return random.choice(PRODUCTION_LINES)


def random_daily_capacity():
    """
    Daily production capacity.
    """

    return random.choice([
        10000,
        25000,
        50000,
        75000,
        100000,
        150000,
        250000
    ])


def random_factory_manager():
    """
    Factory manager.
    """

    return random_name()


def random_email(factory_name):
    """
    Factory email.
    """

    email = (
        factory_name.lower()
        .replace(" ", "")
        .replace("&", "")
    )

    return f"{email}@enterprisefmcg.com"


def random_phone():
    """
    Factory phone.
    """

    return (
        f"+91 "
        f"{random.randint(6000000000, 9999999999)}"
    )