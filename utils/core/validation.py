"""
Enterprise Dataset Validation Utility
Enterprise AI FMCG Lakehouse
"""

import pandas as pd


def validate_dataset(
    df: pd.DataFrame,
    id_column: str = None,
    required_columns=None,
    nullable_columns=None,
):
    """
    Enterprise Dataset Validation

    Parameters
    ----------
    df : pd.DataFrame
        Dataset to validate

    id_column : str
        Primary Key column

    required_columns : list
        Columns that must exist and must not contain NULLs

    nullable_columns : list
        Columns that are allowed to contain NULL values
    """

    if required_columns is None:
        required_columns = []

    if nullable_columns is None:
        nullable_columns = []

    print("\nRunning validation...")

    # =====================================================
    # Empty Dataset
    # =====================================================

    if df.empty:
        raise ValueError("Dataset is empty.")

    # =====================================================
    # Required Columns Exist
    # =====================================================

    for col in required_columns:

        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # =====================================================
    # Duplicate Primary Keys
    # =====================================================

    if id_column:

        duplicates = df[id_column].duplicated().sum()

        if duplicates > 0:
            raise ValueError(
                f"Duplicate IDs found in '{id_column}': {duplicates}"
            )

    # =====================================================
    # NULL Validation
    # Only required columns are checked.
    # =====================================================

    null_errors = {}

    for col in required_columns:

        if col in nullable_columns:
            continue

        null_count = df[col].isnull().sum()

        if null_count > 0:
            null_errors[col] = int(null_count)

    if null_errors:

        print("\nValidation Errors (NULL Values):")

        for col, count in null_errors.items():
            print(f"  {col}: {count}")

        raise ValueError(
            "Required columns contain NULL values."
        )

    print("Validation Passed")