from utils.factory_utils import *

print("Testing Factory Utility\n")

for i in range(1, 11):

    factory = random_factory_name()

    print({

        "Factory": factory,

        "Code": random_factory_code(i),

        "Type": random_factory_type(),

        "Shift": random_shift(),

        "Production Lines": random_production_lines(),

        "Daily Capacity": random_daily_capacity(),

        "Manager": random_factory_manager(),

        "Email": random_email(factory),

        "Phone": random_phone(),

        "Status": random_status()

    })