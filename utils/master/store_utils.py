"""
Enterprise Store Utility
"""

import random

from configs.store_master import (
    STORE_TYPES,
    STORE_PREFIX,
    STORE_SUFFIX,
    STORE_STATUS,
    STORE_CHANNELS,
    OPENING_TIME,
    CLOSING_TIME,
    FLOOR_AREA
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


def random_store_status():
    """
    Random store status.
    """

    return random.choice(STORE_STATUS)


def random_store_code(number):
    """
    Generate enterprise store code.
    """

    return f"STR-{number:05d}"


def random_address():
    """
    Generate sample address.
    """

    road = random.randint(1, 250)

    return f"{road}, MG Road"


def random_postal_code():
    """
    Generate Indian postal code.
    """

    return random.randint(100001, 999999)


def random_opening_time():
    """
    Generate opening time.
    """

    return random.choice(OPENING_TIME)


def random_closing_time():
    """
    Generate closing time.
    """

    return random.choice(CLOSING_TIME)


def random_channel():
    """
    Generate business channel.
    """

    return random.choice(STORE_CHANNELS)


def random_floor_area():
    """
    Generate floor area.
    """

    return random.choice(FLOOR_AREA)


def random_franchise():
    """
    Franchise or company owned.
    """

    return random.choice([True, False])


def random_coordinates():
    """
    Generate approximate India coordinates.
    """

    latitude = round(
        random.uniform(8.0, 35.0),
        6
    )

    longitude = round(
        random.uniform(68.0, 97.0),
        6
    )

    return latitude, longitude