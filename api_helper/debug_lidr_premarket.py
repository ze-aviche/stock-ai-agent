import os
from polygon import RESTClient
from polygon_api_get_historical_data import get_premarket_volume, get_gap_up_day_stats

# Set API key
os.environ["POLYGON_API_KEY"] = "5TcX1iTW6Fu2vysfbRbw60oW3PLWsdPT"

def debug_lidr_premarket():
    polygon_client = RESTClient("5TcX1iTW6Fu2vysfbRbw60oW3PLWsdPT")
    
    # Test with a recent date
    test_date = "2024-01-15"  # You can change this to any recent date
    
    print("=" * 50)
    print(f"DEBUGGING PREMARKET VOLUME FOR LIDR ON {test_date}")
    print("=" * 50)
    
    # Test premarket volume function
    premarket_vol = get_premarket_volume(polygon_client, "LIDR", test_date)
    print(f"\nRaw premarket volume: {premarket_vol}")
    print(f"Premarket volume in millions: {premarket_vol / 1000000}")
    
    # Test gap up stats to see the full context
    print("\n" + "=" * 50)
    print("TESTING GAP UP STATS FOR LIDR")
    print("=" * 50)
    
    gap_up_stats = get_gap_up_day_stats("LIDR", polygon_client)
    
    if gap_up_stats:
        print(f"Found {len(gap_up_stats)} gap up days for LIDR")
        for i, day in enumerate(gap_up_stats[:3]):  # Show first 3 days
            print(f"\nDay {i+1}: {day['date']}")
            print(f"  Premarket volume(M): {day['premarket volume(M)']}")
            print(f"  Total volume(M): {day['total volume(M)']}")
            print(f"  Total $ vol: {day['total $ vol']}")
    else:
        print("No gap up days found for LIDR")

if __name__ == "__main__":
    debug_lidr_premarket() 