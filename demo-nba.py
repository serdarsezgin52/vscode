import numpy as np
import pandas as pd

df = pd.read_csv("nba.csv")

result = df
result = df.head(10)
result = df["Salary"].sum()
result = df["Salary"].mean()
result = df[["Salary","Name"]].max()
result =len(df.index)
result = df[df["Salary"]==df["Salary"].max()]["Name"].iloc[0]

result = df[(df["Age"] >= 20) & (df["Age"] < 25)][["Name","Team","Age"]].sort_values("Age", ascending=False)
result = df[df["Name"]=="John Holland"]["Team"].iloc[0]
result = df.groupby("Team").mean()["Salary"]

result = len(df.groupby("Team"))
result = df["Team"].nunique()
result = df["Team"].value_counts()
df = df.dropna()
result = df[df["Name"].str.contains("and")]

def str_find(name):
    if "and" in name.lower():
        return True
    return False

result = df[df["Name"].apply(str_find )]


print(result)