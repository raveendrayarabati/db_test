import sqlite3
import pandas as pd

conn = sqlite3.connect("sample.db")

print(pd.read_sql("select * from customers", conn))

conn.close()