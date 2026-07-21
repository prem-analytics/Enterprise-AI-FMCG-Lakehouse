"""
Enterprise Location Utility
"""

import random

from configs.location_master import LOCATION_HIERARCHY
from configs.city_master import CITY_MASTER


def random_location():
    """
    Generate random Region -> State -> City
    """

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


def get_city_details(city):
    """
    Return city details.
    """

    return CITY_MASTER[city]