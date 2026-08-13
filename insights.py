"""
insights.py
Turns raw LedgerLite data into answers: best sellers, top customers,
and revenue trends. Run build_ledger.py first if ledger.db doesn't exist.

Run it with:  python3 insights.py
"""

import sqlite3

DB_FILE = "ledger.db"


def show(connection, title, sql):
    print(f"\n📊 {title}")
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    col_names = [description[0] for description in cursor.description]
    print(col_names)
    for row in rows:
        print(row)


def main():
    connection = sqlite3.connect(DB_FILE)

    show(connection, "Revenue by Product", """
        SELECT p.product_name,
               SUM(p.price * s.quantity) AS total_revenue
        FROM sales s
        JOIN products p ON s.product_id = p.product_id
        GROUP BY p.product_name
        ORDER BY total_revenue DESC;
    """)

    show(connection, "Top Spending Customers", """
        SELECT c.name,
               SUM(p.price * s.quantity) AS total_spent
        FROM sales s
        JOIN customers c ON s.customer_id = c.customer_id
        JOIN products p ON s.product_id = p.product_id
        GROUP BY c.name
        ORDER BY total_spent DESC;
    """)

    show(connection, "Units Sold by Category", """
        SELECT p.category,
               SUM(s.quantity) AS units_sold
        FROM sales s
        JOIN products p ON s.product_id = p.product_id
        GROUP BY p.category
        ORDER BY units_sold DESC;
    """)

    connection.close()


if __name__ == "__main__":
    main()