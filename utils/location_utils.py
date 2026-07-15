"""
Enterprise Location Utility
"""

import random

from configs.location_master import LOCATION_HIERARCHY


def random_location():

    region = random.choice(
        list(LOCATION_HIERARCHY.keys())
    )

    state = random.choice(
        list(LOCATION_HIERARCHY[region].keys())
    )

    city = random.choice(
        LOCATION_HIERARCHY[region][state]
    )

    return {
        "region": region,
        "state": state,
        "city": city
    }