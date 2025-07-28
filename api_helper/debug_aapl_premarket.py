import os
from polygon import RESTClient
from polygon_api_get_historical_data import get_premarket_volume

# Set API key
os.environ["POLYGON_API_KEY"] = "5TcX1iTW6Fu2vysfbRbw60oW3PLWsdPT"

def debug_aapl_premarket():
    polygon_client = RESTClient("5TcX1iTW6Fu2vysfbRbw60oW3PLWsdPT")
    
    # Test with a recent date
    test_date = "2024-01-15"
    
    print("=" * 50)
    print(f"DEBUGGING PREMARKET VOLUME FOR AAPL ON {test_date}")
    print("=" * 50)
    
    # Test premarket volume function
    premarket_vol = get_premarket_volume(polygon_client, "AAPL", test_date)
    print(f"\nRaw premarket volume: {premarket_vol}")
    print(f"Premarket volume in millions: {premarket_vol / 1000000}")

if __name__ == "__main__":
    debug_aapl_premarket() 