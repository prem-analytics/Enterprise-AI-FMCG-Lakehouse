import pandas as pd

from utils.validation import validate_dataset

df = pd.DataFrame({

    "id": ["A1", "A2"],

    "name": ["John", "Mary"]

})

validate_dataset(

    df,

    id_column="id",

    required_columns=["id", "name"]

)