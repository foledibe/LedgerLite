# LedgerLite 📒

A lightweight sales ledger for small businesses built with **Python** and **SQL (SQLite)**.

LedgerLite keeps track of who's buying, what's selling, and how the
business is doing, then turns that raw data into answers: best sellers,
top customers, and revenue by category all with a few lines of SQL.

## Overview

This project simulates a small retail business. It models three core
pieces of any sales operation (customers, products, and the sales
transactions) that connect them using a relational SQLite database.
Python scripts handle building the database, filling it with sample
data, and running SQL queries that turn that raw data into useful
business insights.

## Tech Stack

- **Python** — scripts to build the database and run queries
- **SQLite** — a lightweight, file-based SQL database (via Python's built-in `sqlite3` module)
- **SQL** — used for schema design and all data queries (JOINs, GROUP BY, aggregates)

## Project Structure

Here's what each file in this repo does:

```
ledger-lite/
├── schema.sql # Defines the tables (customers, products, sales)
├── build_ledger.py # Builds ledger.db and stocks it with sample data
├── insights.py # Turns raw data into business insights
└── README.md # Project documentation (this file)
```

- **schema.sql** is the blueprint for the database. It defines three tables — customers, products, and sales — and links them together using primary and foreign keys.
- **build_ledger.py** reads schema.sql to create the actual database file (ledger.db), then inserts sample customers, products, and sales transactions so there's real data to work with.
- **insights.py** connects to ledger.db and runs a set of SQL queries that answer real business questions, printing the results to the terminal.

## How to Run

1. Clone this repo:
   git clone https://github.com/foledibe/LedgerLite.git
   cd ledger-lite
2. Build the ledger (creates the database and fills it with sample data):
   python build_ledger.py
3. Get insights (runs the queries and prints the results):
   python insights.py

## Example Insights

Running insights.py answers questions like:

- Which products bring in the most revenue?
- Who are the top spending customers?
- How many units sell in each product category?

## What I Learned

Building LedgerLite helped me practice:

- Designing a relational database schema, including primary keys and foreign keys
- Writing SQL JOIN and GROUP BY queries to turn raw data into insights
- Using Python's sqlite3 module to build, seed, and query a database
- Using git and GitHub to track project history and share my work
