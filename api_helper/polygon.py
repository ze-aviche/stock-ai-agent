from polygon import RESTClient
from polygon.rest.models import (
    TickerSnapshot,
)

POLYGON_API_KEY = os.environ.get("POLYGON_API_KEY")

def get_gap_up_list():
    
    polygon_client = RESTClient(POLYGON_API_KEY)

    tickers = client.get_snapshot_direction(
        "stocks",
        direction="gainers",
        )

    #print(tickers)
    #gainers = [ticker for ticker in tickers]
    # print ticker with % change
    for item in tickers:
        # verify this is a TickerSnapshot
        if isinstance(item, TickerSnapshot):
            # verify this is a float
            if isinstance(item.todays_change_percent, float):
                #print("{:<15}{:.2f} %".format(item.ticker, item.todays_change_percent))
                gainers.append[item.ticker]
    
    return gainers

