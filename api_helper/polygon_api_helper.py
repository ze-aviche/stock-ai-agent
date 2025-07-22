from polygon import RESTClient
import os

POLYGON_API_KEY = os.environ.get("POLYGON_API_KEY")

def get_gap_up_list():
    polygon_client = RESTClient(POLYGON_API_KEY)
    tickers = polygon_client.get_snapshot_direction(
        "stocks",
        direction="gainers",
    )
    all_tickers = []
    # Print the structure of the first item for debugging
    if tickers and isinstance(tickers, list):
        print("First item structure:", tickers[0], "type:", type(tickers[0]))
    for item in tickers:
        # Try to extract ticker symbol from possible attributes or keys
        ticker = None
        if isinstance(item, dict):
            ticker = item.get("ticker") or item.get("symbol")
        elif hasattr(item, "ticker"):
            ticker = getattr(item, "ticker", None)
        elif hasattr(item, "symbol"):
            ticker = getattr(item, "symbol", None)
        if ticker:
            all_tickers.append(ticker)
    print("All tickers:", all_tickers)
    return all_tickers

# if __name__ == "__main__":
#     get_gap_up_list()

