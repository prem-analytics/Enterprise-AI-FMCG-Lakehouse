"""
Enterprise Dataset Validation Utility
"""

import pandas as pd


def validate_dataset(df: pd.DataFrame,
                     id_column: str = None,
                     required_columns=None):

    if required_columns is None:
        required_columns = []

    print("\nRunning validation...")

    # Empty dataset
    if df.empty:
        raise ValueError("Dataset is empty.")

    # Required columns
    for col in required_columns:

        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Duplicate IDs
    if id_column:

        duplicates = df[id_column].duplicated().sum()

        if duplicates > 0:
            raise ValueError(
                f"Duplicate IDs found in {id_column}: {duplicates}"
            )

    # Missing values
    nulls = df.isnull().sum().sum()

    if nulls > 0:

        raise ValueError(
            f"Dataset contains {nulls} null values."
        )

    print("Validation Passed")