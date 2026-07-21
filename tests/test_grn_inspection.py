from pprint import pprint

from utils.grn.inspection import (
    build_inspection,
)

for i in range(10):

    print(f"\nInspection {i+1}")

    pprint(
        build_inspection()
    )