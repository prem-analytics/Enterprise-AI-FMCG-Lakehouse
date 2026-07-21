"""
Enterprise AI FMCG Lakehouse
Master Data Generator Runner
"""

import time
import traceback

from pipelines.data_generation.generate_customers import main as customers
from pipelines.data_generation.generate_products import main as products
from pipelines.data_generation.generate_stores import main as stores
from pipelines.data_generation.generate_suppliers import main as suppliers
from pipelines.data_generation.generate_warehouses import main as warehouses
from pipelines.data_generation.generate_factories import main as factories


PIPELINES = [

    ("Customers", customers),

    ("Products", products),

    ("Stores", stores),

    ("Suppliers", suppliers),

    ("Warehouses", warehouses),

    ("Factories", factories)

]


def main():

    print("=" * 70)
    print("Enterprise AI FMCG Lakehouse")
    print("Master Data Generation")
    print("=" * 70)

    start = time.time()

    success = 0

    failed = 0

    for name, pipeline in PIPELINES:

        print(f"\nRunning {name}...")

        try:

            pipeline()

            print(f"{name} : SUCCESS")

            success += 1

        except Exception:

            failed += 1

            print(f"{name} : FAILED")

            traceback.print_exc()

    elapsed = time.time() - start

    print("\n" + "=" * 70)

    print("MASTER DATA GENERATION COMPLETED")

    print("=" * 70)

    print(f"Successful Pipelines : {success}")

    print(f"Failed Pipelines     : {failed}")

    print(f"Execution Time       : {elapsed:.2f} seconds")

    print("=" * 70)


if __name__ == "__main__":
    main()