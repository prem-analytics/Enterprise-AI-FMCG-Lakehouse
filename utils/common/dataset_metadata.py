"""
Enterprise Dataset Metadata Utility
"""

import json
import os
from datetime import datetime


def create_metadata(
    dataframe,
    folder,
    filename,
    version="1.0"
):

    metadata = {

        "dataset": filename,

        "generated_at": datetime.now().isoformat(),

        "rows": len(dataframe),

        "columns": list(dataframe.columns),

        "column_count": len(dataframe.columns),

        "version": version

    }

    output_folder = os.path.join(
        "data",
        "generated",
        folder
    )

    os.makedirs(output_folder, exist_ok=True)

    metadata_path = os.path.join(
        output_folder,
        f"{filename}_metadata.json"
    )

    with open(
        metadata_path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            metadata,
            f,
            indent=4
        )

    return metadata_path