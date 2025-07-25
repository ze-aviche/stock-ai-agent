from polygon import RESTClient
from api_helper.polygon_api_get_historical_data import (
    analyze, get_gap_up_day_stats, get_daily_high_low_data,
    get_premarket_high_low_data, get_premarket_volume, count_vwap_crosses
)

API_KEY = "5TcX1iTW6Fu2vysfbRbw60oW3PLWsdPT"

def analyze_tool(tickers):
    polygon_client = RESTClient(API_KEY)
    return analyze(tickers, polygon_client)

def get_gap_up_day_stats_tool(ticker):
    polygon_client = RESTClient(API_KEY)
    return get_gap_up_day_stats(ticker, polygon_client)

def get_daily_high_low_data_tool(ticker, date_str):
    polygon_client = RESTClient(API_KEY)
    return get_daily_high_low_data(ticker, polygon_client, date_str)

def get_premarket_high_low_data_tool(ticker, date_str):
    polygon_client = RESTClient(API_KEY)
    return get_premarket_high_low_data(ticker, polygon_client, date_str)

def get_premarket_volume_tool(ticker, date_str):
    polygon_client = RESTClient(API_KEY)
    return get_premarket_volume(polygon_client, ticker, date_str)

def count_vwap_crosses_tool(ticker, date_str):
    polygon_client = RESTClient(API_KEY)
    return count_vwap_crosses(polygon_client, ticker, date_str)
