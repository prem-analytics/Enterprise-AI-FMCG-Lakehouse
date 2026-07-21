"""
Enterprise Sample Dataset Generator
"""

import os


def create_sample(dataframe, folder, filename, rows=100):

    sample = dataframe.sample(
        n=min(rows, len(dataframe)),
        random_state=42
    )

    output_folder = os.path.join(
        "data",
        "sample_data"
    )

    os.makedirs(output_folder, exist_ok=True)

    sample_path = os.path.join(
        output_folder,
        f"{filename}_sample.csv"
    )

    sample.to_csv(
        sample_path,
        index=False
    )

    return sample_path