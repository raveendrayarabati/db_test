import sqlite3

conn = sqlite3.connect("sample.db")

cur = conn.cursor()

cur.execute("""
CREATE TABLE customers (
    customer_id INTEGER,
    customer_name TEXT
)
""")

cur.execute("""
INSERT INTO customers VALUES
(1,'john'),
(2,'ravi'),
(3,'smith')
""")

conn.commit()
conn.close()

print("done")