import sqlite3

DB_PATH = "trades.db"

def get_trade_history(ticker):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM trades WHERE ticker = ?", (ticker,))
    rows = cursor.fetchall()

    conn.close()
    return rows

def insert_trade_from_alpaca(order_json):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO trades (
            ticker, action, quantity, filled_price, status,
            order_id, submitted_at, filled_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        order_json.get("symbol"),
        order_json.get("side"),
        order_json.get("qty"),
        float(order_json.get("filled_avg_price", 0.0)),
        order_json.get("status"),
        order_json.get("id"),
        order_json.get("submitted_at"),
        order_json.get("filled_at")
    ))

    conn.commit()
    conn.close()