import os


def save_dataset(dataframe, folder, filename):

    output_folder = os.path.join(
        "data",
        "generated",
        folder
    )

    os.makedirs(output_folder, exist_ok=True)

    csv_path = os.path.join(
        output_folder,
        f"{filename}.csv"
    )

    parquet_path = os.path.join(
        output_folder,
        f"{filename}.parquet"
    )

    dataframe.to_csv(
        csv_path,
        index=False
    )

    dataframe.to_parquet(
        parquet_path,
        index=False
    )

    return csv_path, parquet_path

    return csv_path, parquet_path