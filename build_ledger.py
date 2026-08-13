"""
build_ledger.py
Builds ledger.db from schema.sql, then stocks it with sample data so
LedgerLite has a business to actually track.

Run it with:  python3 build_ledger.py
"""

import sqlite3

DB_FILE = "ledger.db"
SCHEMA_FILE = "schema.sql"


def build_schema():
    """Read schema.sql and lay down the tables."""
    connection = sqlite3.connect(DB_FILE)
    with open(SCHEMA_FILE, "r") as f:
        connection.executescript(f.read())
    connection.commit()
    connection.close()
    print(f"📒 LedgerLite structure built in {DB_FILE}")


def stock_sample_data():
    """Add sample customers, products, and sales to bring the ledger to life."""
    connection = sqlite3.connect(DB_FILE)
    cursor = connection.cursor()

    customers = [
        ("Ava Johnson", "ava@example.com", "Chicago"),
        ("Liam Chen", "liam@example.com", "Austin"),
        ("Maya Patel", "maya@example.com", "Seattle"),
        ("Noah Garcia", "noah@example.com", "Miami"),
    ]
    cursor.executemany(
        "INSERT INTO customers (name, email, city) VALUES (?, ?, ?)",
        customers,
    )

    products = [
        ("Wireless Mouse", "Electronics", 19.99),
        ("Notebook", "Office Supplies", 3.49),
        ("Desk Lamp", "Home", 24.99),
        ("Water Bottle", "Accessories", 12.50),
        ("Backpack", "Accessories", 39.99),
    ]
    cursor.executemany(
        "INSERT INTO products (product_name, category, price) VALUES (?, ?, ?)",
        products,
    )

    sales = [
        (1, 1, 2, "2026-01-05"),
        (2, 3, 1, "2026-01-06"),
        (1, 4, 3, "2026-01-10"),
        (3, 5, 1, "2026-01-11"),
        (4, 2, 5, "2026-01-12"),
        (2, 1, 1, "2026-01-15"),
        (3, 4, 2, "2026-01-18"),
    ]
    cursor.executemany(
        "INSERT INTO sales (customer_id, product_id, quantity, sale_date) VALUES (?, ?, ?, ?)",
        sales,
    )

    connection.commit()
    connection.close()
    print(f"📦 Stocked the ledger: {len(customers)} customers, "
          f"{len(products)} products, {len(sales)} sales")


if __name__ == "__main__":
    build_schema()
    stock_sample_data()