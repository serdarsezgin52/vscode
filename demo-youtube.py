import pandas as pd
import numpy as np

df = pd.read_csv("youtube-ing.csv")
result = df

result = df.head(10)
result = df[5:10].head()
result = df.columns
result = len(df.columns)



print(result)