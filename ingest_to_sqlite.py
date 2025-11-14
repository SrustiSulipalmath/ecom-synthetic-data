import sqlite3
import pandas as pd

FILES = {
    "users": "users.csv",
    "products": "products.csv",
    "orders": "orders.csv",
    "order_items": "order_items.csv",
    "payments": "payments.csv",
}


def main(database_path="ecom.db"):
    with sqlite3.connect(database_path) as conn:
        for table, file in FILES.items():
            df = pd.read_csv(file)
            df.to_sql(table, conn, if_exists="replace", index=False)
            print(f"Loaded {table}")
    print("All tables loaded into SQLite!")


if __name__ == "__main__":
    main()
