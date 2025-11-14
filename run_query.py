import sqlite3
import pandas as pd

conn = sqlite3.connect("ecom.db")

query = """
SELECT 
    o.order_id,
    u.name AS customer,
    p.name AS product,
    oi.quantity,
    pay.amount,
    o.order_date
FROM orders o
JOIN users u ON o.user_id = u.user_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
JOIN payments pay ON o.order_id = pay.order_id;
"""

df = pd.read_sql_query(query, conn)
print(df)

conn.close()
