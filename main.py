from agents.agent import root_agent
from agents.gap_up_listing_agent import gap_up_listing_agent
from agents.trades_history_agent import trade_history_agent
from agents.data_agent import data_agent
from agents.trade_planning_agent import trade_planning_agent
#from agents.loop_agent import loop_agent
from agents.execution_agent import execution_agent
from db.trades_db import get_trade_history

# Dummy trades DB (in-memory for now)
trades_db = {
    "AAPL": [{"date": "2024-06-01", "action": "buy", "price": 170}],
    "TSLA": [{"date": "2024-06-15", "action": "sell", "price": 620}]
}

def check_trade_history(ticker):
    history = get_trade_history(ticker)
    if history:
        print(f"🧾 Trade history found for {ticker} ({len(history)} entries).")
        return trade_history_agent.run(f"Get history for {ticker}")
    else:
        print(f"📭 No previous trades for {ticker}.")
        return None

def fetch_gap_up_tickers():
    print("📡 Running gap_up_listing_agent...")
    tickers = gap_up_listing_agent.run("Fetch today's gap-up tickers from Polygon")
    if isinstance(tickers, list):
        return tickers
    return ["AAPL", "MSFT", "NVDA"]  # fallback dummy list

def main():
    print("📊 Welcome to the AI Stock Trading System (Multi-Agent)")
    user_prompt = input("🧠 What would you like to do today? (e.g., 'Find trades', 'Plan trades', etc.): ")

    # Start root agent
    root_agent.run(user_prompt)

    # Step 1: Get gap-up tickers
    tickers = fetch_gap_up_tickers()
    print(f"📈 Today's gap-up tickers: {tickers}")

    for ticker in tickers:
        print(f"\n=== Processing {ticker} ===")

        # Step 2: Trade history check
        check_trade_history(ticker)

        # Step 3: Fetch market data
        print(f"🔍 Getting data for {ticker}...")
        data_agent.run(f"Get market data for {ticker}")

        # Step 4: Trade planning loop (risk + backtesting)
        print(f"🧠 Planning trade for {ticker}...")
        trade_planning_agent.run(f"Generate and validate trade plan for {ticker}")

        # Step 5: Execute trade
        print(f"🚀 Executing trade for {ticker}...")
        execution_agent.run(f"Execute final trade for {ticker}")

    print("\n✅ All tickers processed.")

if __name__ == "__main__":
    main()
