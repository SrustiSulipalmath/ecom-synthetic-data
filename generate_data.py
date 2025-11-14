from faker import Faker
import csv
import random

fake = Faker()

def generate_users(n=50):
    with open("users.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["user_id", "name", "email"])
        for i in range(1, n+1):
            writer.writerow([
                i,
                fake.name(),
                fake.email()
            ])

def generate_products(n=30):
    with open("products.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["product_id", "name", "price"])
        for i in range(1, n+1):
            writer.writerow([
                i,
                fake.word(),
                round(random.uniform(100, 2000), 2)
            ])

def generate_orders(n=40):
    with open("orders.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["order_id", "user_id", "order_date"])
        for i in range(1, n+1):
            writer.writerow([
                i,
                random.randint(1, 50),
                fake.date()
            ])

def generate_order_items(n=80):
    with open("order_items.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["order_item_id", "order_id", "product_id", "quantity"])
        for i in range(1, n+1):
            writer.writerow([
                i,
                random.randint(1, 40),
                random.randint(1, 30),
                random.randint(1, 5)
            ])

def generate_payments(n=40):
    with open("payments.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["payment_id", "order_id", "amount"])
        for i in range(1, n+1):
            writer.writerow([
                i,
                i,
                round(random.uniform(200, 5000), 2)
            ])

generate_users()
generate_products()
generate_orders()
generate_order_items()
generate_payments()

print("Synthetic e-commerce data created!")
