from utils.store_utils import (
    random_store_name,
    random_store_type,
    random_store_email,
    random_store_phone
)

print("Testing Store Utilities\n")

for _ in range(10):

    name = random_store_name()

    print(
        {
            "Store": name,
            "Type": random_store_type(),
            "Email": random_store_email(name),
            "Phone": random_store_phone()
        }
    )