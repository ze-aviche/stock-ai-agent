import sqlite3

def init_trades_db(db_path="trades.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT NOT NULL,
            action TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER DEFAULT 0,
            timestamp TEXT NOT NULL
        )
    """)

    # Insert sample data
    cursor.executemany("""
        INSERT INTO trades (ticker, action, price, quantity, date)
        VALUES (?, ?, ?, ?, ?)
    """, [
        ("AAPL", "buy", 170.0, 10, "2024-06-01"),
        ("TSLA", "sell", 620.0, 5, "2024-06-15"),
        ("MSFT", "buy", 300.5, 20, "2024-07-01")
    ])

    conn.commit()
    conn.close()
    print(f"✅ trades.db initialized with sample data.")

if __name__ == "__main__":
    init_trades_db()
