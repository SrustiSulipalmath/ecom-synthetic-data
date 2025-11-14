import sqlite3
import pandas as pd

conn = sqlite3.connect("ecom.db")

files = {
    "users": "users.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "payments": "payments.csv"
}

for table, file in files.items():
    df = pd.read_csv(file)
    df.to_sql(table, conn, if_exists="replace", index=False)
    print(f"Loaded {table}")

conn.close()
print("All tables loaded into SQLite!")
