"""
Enterprise Pipeline Runner
"""

import time

from utils.validation import validate_dataset
from utils.file_utils import save_dataset
from utils.metadata import create_metadata
from utils.sample_generator import create_sample
from utils.logger import logger


def run_pipeline(
    dataframe,
    folder,
    filename,
    id_column=None,
    required_columns=None,
    nullable_columns=None,
    title=""
):
    """
    Execute the standard enterprise data generation pipeline.
    """

    start_time = time.time()

    logger.info(f"{title} started")

    validate_dataset(
        dataframe,
        id_column=id_column,
        required_columns=required_columns,
        nullable_columns=nullable_columns,
    )

    save_dataset(
        dataframe=dataframe,
        folder=folder,
        filename=filename,
    )

    create_metadata(
        dataframe=dataframe,
        folder=folder,
        filename=filename,
    )

    create_sample(
        dataframe=dataframe,
        folder=folder,
        filename=filename,
    )

    elapsed = time.time() - start_time

    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)
    print(f"Rows Generated : {len(dataframe):,}")
    print("Validation     : PASSED")
    print(f"CSV File       : data/generated/{folder}/{filename}.csv")
    print(f"Parquet File   : data/generated/{folder}/{filename}.parquet")
    print(
        f"Metadata File  : data/generated/{folder}/{filename}_metadata.json"
    )
    print(f"Sample File    : data/sample_data/{filename}_sample.csv")
    print("=" * 60)
    print(f"Execution Time : {elapsed:.2f} seconds")

    logger.info(
        f"{title} completed successfully "
        f"({len(dataframe):,} rows)"
    )

    return dataframe