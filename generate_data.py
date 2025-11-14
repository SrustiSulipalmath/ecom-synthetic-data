from collections import defaultdict
from faker import Faker
import csv
import random

fake = Faker()

NUM_USERS = 50
NUM_PRODUCTS = 30
NUM_ORDERS = 40
NUM_ORDER_ITEMS = 80


def generate_users(count=NUM_USERS, path="users.csv"):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["user_id", "name", "email"])
        for user_id in range(1, count + 1):
            writer.writerow([user_id, fake.name(), fake.email()])


def generate_products(count=NUM_PRODUCTS, path="products.csv"):
    product_prices = {}
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["product_id", "name", "price"])
        for product_id in range(1, count + 1):
            price = round(random.uniform(100, 2000), 2)
            product_prices[product_id] = price
            writer.writerow([product_id, fake.word(), price])
    return product_prices


def generate_orders(user_count=NUM_USERS, order_count=NUM_ORDERS, path="orders.csv"):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["order_id", "user_id", "order_date"])
        for order_id in range(1, order_count + 1):
            writer.writerow([
                order_id,
                random.randint(1, user_count),
                fake.date()
            ])


def generate_order_items(
    product_prices,
    order_count=NUM_ORDERS,
    total_items=NUM_ORDER_ITEMS,
    path="order_items.csv"
):
    if total_items < order_count:
        raise ValueError("total_items must be greater than or equal to order_count")

    product_ids = list(product_prices.keys())
    order_totals = defaultdict(float)

    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["order_item_id", "order_id", "product_id", "quantity"])

        order_item_id = 1

        # Ensure every order has at least one line item
        for order_id in range(1, order_count + 1):
            product_id = random.choice(product_ids)
            quantity = random.randint(1, 5)
            price = product_prices[product_id]
            writer.writerow([order_item_id, order_id, product_id, quantity])
            order_totals[order_id] += quantity * price
            order_item_id += 1

        # Add remaining random line items
        for _ in range(total_items - order_count):
            order_id = random.randint(1, order_count)
            product_id = random.choice(product_ids)
            quantity = random.randint(1, 5)
            price = product_prices[product_id]
            writer.writerow([order_item_id, order_id, product_id, quantity])
            order_totals[order_id] += quantity * price
            order_item_id += 1

    return order_totals


def generate_payments(order_totals, order_count=NUM_ORDERS, path="payments.csv"):
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["payment_id", "order_id", "amount"])
        for order_id in range(1, order_count + 1):
            amount = round(order_totals.get(order_id, 0.0), 2)
            writer.writerow([order_id, order_id, amount])


def main():
    product_prices = generate_products()
    generate_users()
    generate_orders()
    order_totals = generate_order_items(product_prices)
    generate_payments(order_totals)
    print("Synthetic e-commerce data created!")


if __name__ == "__main__":
    main()
