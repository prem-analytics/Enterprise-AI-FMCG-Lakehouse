"""
Utility functions for generating realistic Indian customer data.
"""

from faker import Faker
import random

fake = Faker("en_IN")

REGIONS = {
    "North": [
        "Delhi", "Punjab", "Haryana",
        "Uttar Pradesh", "Uttarakhand"
    ],
    "South": [
        "Tamil Nadu", "Karnataka",
        "Kerala", "Telangana",
        "Andhra Pradesh"
    ],
    "East": [
        "West Bengal",
        "Odisha",
        "Bihar",
        "Jharkhand"
    ],
    "West": [
        "Maharashtra",
        "Gujarat",
        "Rajasthan",
        "Goa"
    ]
}


def random_region():
    region = random.choice(list(REGIONS.keys()))
    state = random.choice(REGIONS[region])
    return region, state


def random_customer():
    region, state = random_region()

    return {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "gender": random.choice(["Male", "Female"]),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "address": fake.street_address(),
        "city": fake.city(),
        "state": state,
        "region": region,
        "pincode": fake.postcode(),
    }

def random_name():
    """
    Generate a random full name.
    """

    return fake.name()