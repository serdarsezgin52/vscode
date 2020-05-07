import sqlite3
import pandas as pd
import numpy as np

# df = pd.read_csv('sample.csv')
# df = pd.read_json('sample.json')
# df = pd.read_excel('sample.xlsx')
connect = sqlite3.connect('sample.db')
df = pd.read_sql_query("select * from students", connect)

print(df)