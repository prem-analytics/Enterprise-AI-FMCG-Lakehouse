import os


def save_dataset(df, folder, filename):

    output_folder = os.path.join(
        "data",
        "generated",
        folder
    )

    os.makedirs(output_folder, exist_ok=True)

    csv_path = os.path.join(output_folder, f"{filename}.csv")

    parquet_path = os.path.join(output_folder, f"{filename}.parquet")

    df.to_csv(csv_path, index=False)

    df.to_parquet(parquet_path, index=False)

    return csv_path, parquet_path