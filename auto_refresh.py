# auto_refresh.py
import os
import time
import random
import string
from datetime import datetime, timedelta
from sqlalchemy import create_engine, text
from dotenv import load_dotenv


load_dotenv()


DB_USER = os.getenv("DB_USER", "mi_user")
DB_PASS = os.getenv("DB_PASS", "strongpass")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "mercadoinsights_db")

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def random_id(prefix, length=8):
    return prefix + "_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def insert_random_data():
    """Insert a random new order with item and payment data."""
    order_id = random_id("order")
    customer_id = random_id("cust")
    product_id = random_id("prod")
    seller_id = random_id("seller")
    now = datetime.now()

    with engine.begin() as conn:  
       
        conn.execute(text("""
            INSERT INTO olist_customers (customer_id, customer_unique_id, customer_zip_code_prefix, customer_city, customer_state)
            VALUES (:cid, :cuid, :zip, :city, :state)
            ON CONFLICT (customer_id) DO NOTHING
        """), {
            "cid": customer_id,
            "cuid": random_id("unique"),
            "zip": random.randint(10000, 99999),
            "city": random.choice(["Astana", "Almaty", "Karaganda", "Shymkent"]),
            "state": random.choice(["KZ", "RU", "UZ"])
        })

        # Insert order
        conn.execute(text("""
            INSERT INTO olist_orders (order_id, customer_id, order_status, order_purchase_timestamp,
                order_approved_at, order_delivered_carrier_date, order_delivered_customer_date, order_estimated_delivery_date)
            VALUES (:oid, :cid, 'delivered', :purch, :appr, :delv, :delv2, :estim)
        """), {
            "oid": order_id,
            "cid": customer_id,
            "purch": now,
            "appr": now + timedelta(minutes=5),
            "delv": now + timedelta(days=1),
            "delv2": now + timedelta(days=2),
            "estim": now + timedelta(days=5)
        })

        # Insert product (correct column names)
        conn.execute(text("""
            INSERT INTO olist_products (product_id, product_category_name, product_name_length, product_description_length,
                product_photos_qty, product_weight_g, product_length_cm, product_height_cm, product_width_cm)
            VALUES (:pid, :cat, 10, 100, 1, 200, 10, 5, 5)
            ON CONFLICT (product_id) DO NOTHING
        """), {
            "pid": product_id,
            "cat": random.choice(["electronics", "books", "toys", "fashion", "sports"])
        })

        # Insert seller
        conn.execute(text("""
            INSERT INTO olist_sellers (seller_id, seller_zip_code_prefix, seller_city, seller_state)
            VALUES (:sid, :zip, :city, :state)
            ON CONFLICT (seller_id) DO NOTHING
        """), {
            "sid": seller_id,
            "zip": random.randint(10000, 99999),
            "city": random.choice(["Astana", "Almaty", "Karaganda", "Shymkent"]),
            "state": random.choice(["KZ", "RU", "UZ"])
        })

        # Insert order item
        price = round(random.uniform(10, 500), 2)
        freight = round(price * random.uniform(0.05, 0.15), 2)
        conn.execute(text("""
            INSERT INTO olist_order_items (order_id, order_item_id, product_id, seller_id,
                shipping_limit_date, price, freight_value)
            VALUES (:oid, 1, :pid, :sid, :ship, :price, :freight)
        """), {
            "oid": order_id,
            "pid": product_id,
            "sid": seller_id,
            "ship": now + timedelta(days=1),
            "price": price,
            "freight": freight
        })

        # Insert payment
        conn.execute(text("""
            INSERT INTO olist_order_payments (order_id, payment_sequential, payment_type, payment_installments, payment_value)
            VALUES (:oid, 1, :ptype, :inst, :val)
        """), {
            "oid": order_id,
            "ptype": random.choice(["credit_card", "boleto", "voucher", "debit_card"]),
            "inst": random.randint(1, 3),
            "val": price + freight
        })

        print(f"[✓] Inserted new order: {order_id} — total {price + freight:.2f} BRL")

def main():
    print("=== Auto Refresh Simulation Started ===")
    print("This script will insert new random orders every 15 seconds.")
    print("Press Ctrl+C to stop.\n")
    while True:
        insert_random_data()
        time.sleep(15)  # Wait 15 seconds between inserts

if __name__ == "__main__":
    main()
