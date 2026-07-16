from utils.warehouse_utils import *

print("Testing Warehouse Utility\n")

for i in range(1, 11):

    warehouse = random_warehouse_name()

    print({

        "Warehouse": warehouse,

        "Code": random_warehouse_code(i),

        "Type": random_warehouse_type(),

        "Temperature": random_temperature_zone(),

        "Capacity": random_capacity(),

        "Utilization": random_utilization(),

        "Manager": random_manager(),

        "Email": random_email(warehouse),

        "Phone": random_phone(),

        "Hours": random_operating_hours(),

        "Status": random_status()

    })