from utils.location_utils import (
    random_location,
    get_city_details
)

print("Testing Enterprise Location Utility\n")

for _ in range(10):

    location = random_location()

    city = location["city"]

    details = get_city_details(city)

    print({
        "Region": location["region"],
        "State": location["state"],
        "City": city,
        "Postal Code": details["postal_code"],
        "Latitude": details["latitude"],
        "Longitude": details["longitude"]
    })