import random


def generate_pricing():
    """
    Generate realistic FMCG pricing.
    """

    cost = round(random.uniform(20, 500), 2)

    margin = random.uniform(0.15, 0.45)

    selling = round(cost * (1 + margin), 2)

    gst = random.choice([5, 12, 18])

    return {
        "cost_price": cost,
        "selling_price": selling,
        "gst_percent": gst
    }