from polygon import RESTClient
import os
from config.api_keys import POLYGON_API_KEY


def get_gap_up_list():
    #POLYGON_API_KEY = api_keys.POLYGON_API_KEY
    print("POLYGON_API_KEY:", POLYGON_API_KEY)
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
            details = polygon_client.get_ticker_details(ticker)
            issue_type = details.get("type")
            if issue_type == "CS":
                all_tickers.append(ticker)
    print("All tickers:", all_tickers)
    return all_tickers

def get_ticker_details(ticker_list):
    #POLYGON_API_KEY = api_keys.POLYGON_API_KEY
    print("POLYGON_API_KEY:", POLYGON_API_KEY)
    polygon_client = RESTClient(POLYGON_API_KEY)
    details_list = []
    for ticker in ticker_list:
        try:
            # Fetch ticker details from Polygon
            details = polygon_client.get_ticker_details(ticker)
            # details is likely a dict; extract relevant fields
            print("details:", details)
            sector = details.get("sic_description")
            market_cap = details.get("market_cap")
            #avg_vol = details.get("avg_vol") or details.get("average_volume")
            details_list.append({
                "ticker": ticker,
                "sector": sector,
                "market_cap": market_cap,
                #"avg_volume": avg_vol
            })
        except Exception as e:
            print(f"Error fetching details for {ticker}: {e}")
    print("Ticker details:", details_list)
    return details_list

if __name__ == "__main__":
    #get_gap_up_list()
    gainers = get_gap_up_list()
    get_ticker_details(gainers)

