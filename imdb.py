import pandas as pd

df = pd.read_csv('imdb.csv')



result = df
result = df.columns
result = df.head() # ilk 5 kayıt
result = df.head(10) # ilk 10 kayıt
result = df.tail() # son 5 kayıt
result = df.tail(10)  # son 10 kayıt
result = df["Movie_Title"]
result = df["Movie_Title"].head()
result = df[["Movie_Title","Rating"]].head()
result = df[["Movie_Title","Rating"]].tail(7)
result = df[5:10][["Movie_Title","Rating"]]
result = df[df["Rating"] >= 8.0][["Movie_Title","Rating"]].head(50)

result = df[(df["YR_Released"] >= 2014) & (df["YR_Released"] <= 2015)][["Movie_Title", "YR_Released"]]

result = df[(df["Num_Reviews"] > 100000) | ((df["Rating"] >= 8) & (df["Rating"] <= 9))][["Movie_Title","Num_Reviews","Rating"]].head(10)
result = df[(df["Rating"] >= 9)]

print(result)