import pandas as pd

from utils.metadata import create_metadata

df = pd.DataFrame({

    "id": [1, 2],

    "name": ["A", "B"]

})

path = create_metadata(

    dataframe=df,

    folder="test",

    filename="test_dataset"

)

print(path)