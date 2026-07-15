import pandas as pd

from utils.sample_generator import create_sample

df = pd.DataFrame({

    "id": range(500),

    "name": [f"Item{i}" for i in range(500)]

})

path = create_sample(

    dataframe=df,

    folder="test",

    filename="sample"

)

print(path)