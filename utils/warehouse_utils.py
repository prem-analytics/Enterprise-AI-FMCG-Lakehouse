"""
Enterprise Warehouse Utility
"""

import random

from utils.faker_utils import random_name

from configs.warehouse_master import (
    WAREHOUSE_TYPES,
    TEMPERATURE_ZONES,
    WAREHOUSE_PREFIX,
    WAREHOUSE_SUFFIX,
    OPERATING_HOURS,
    WAREHOUSE_STATUS
)


def random_warehouse_name():
    """
    Generate warehouse name.
    """

    return (
        f"{random.choice(WAREHOUSE_PREFIX)} "
        f"{random.choice(WAREHOUSE_SUFFIX)}"
    )


def random_warehouse_code(number):
    """
    Generate warehouse code.
    """

    return f"WH-{number:04d}"


def random_warehouse_type():
    """
    Warehouse type.
    """

    return random.choice(WAREHOUSE_TYPES)


def random_temperature_zone():
    """
    Temperature zone.
    """

    return random.choice(TEMPERATURE_ZONES)


def random_operating_hours():
    """
    Operating hours.
    """

    return random.choice(OPERATING_HOURS)


def random_capacity():
    """
    Storage capacity in metric tons.
    """

    return random.choice([
        1000,
        2500,
        5000,
        10000,
        15000,
        25000,
        50000
    ])


def random_utilization():
    """
    Current warehouse utilization.
    """

    return random.randint(40, 95)


def random_manager():
    """
    Warehouse manager.
    """

    return random_name()


def random_email(warehouse_name):
    """
    Warehouse email.
    """

    email = (
        warehouse_name.lower()
        .replace(" ", "")
        .replace("&", "")
    )

    return f"{email}@enterprisefmcg.com"


def random_phone():
    """
    Warehouse phone.
    """

    return (
        f"+91 "
        f"{random.randint(6000000000, 9999999999)}"
    )


def random_status():
    """
    Warehouse status.
    """

    return random.choice(WAREHOUSE_STATUS)