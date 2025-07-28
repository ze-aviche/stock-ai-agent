import datetime
from datetime import datetime, timedelta
import pytz

# --- Helper Functions ---
def count_vwap_crosses(polygon_client, ticker, date):
    """
    Fetches 2-minute bar data for a given ticker and date and counts VWAP crosses.
    """
    try:
        aggs_data = polygon_client.list_aggs(
            ticker=ticker,
            multiplier=2,
            timespan='minute',
            from_=date,
            to=date,
            limit=50000
        )
        aggs_list = list(aggs_data)
    except Exception as e:
        print(f"Error fetching 2-minute bar data for {ticker} on {date}: {e}")
        return None
    if not aggs_list:
        return 0
    cross_count = 0
    previous_close = aggs_list[0].close
    previous_vwap = aggs_list[0].vwap
    for i in range(1, len(aggs_list)):
        current_bar = aggs_list[i]
        current_close = current_bar.close
        current_vwap = current_bar.vwap
        if previous_close is not None and current_close is not None and previous_vwap is not None and current_vwap is not None:
            if (previous_close < previous_vwap and current_close > current_vwap) or \
               (previous_close > previous_vwap and current_close < current_vwap):
                cross_count += 1
        previous_close = current_close
        previous_vwap = current_vwap
    return cross_count

def get_premarket_high_low_data(ticker, polygon_client, date_str):
    """
    Fetches the premarket high/low and their timestamps for a given ticker and date (4:00 AM to 9:30 AM EST).
    """
    try:
        est_timezone = pytz.timezone('America/New_York')
        start_datetime_est = est_timezone.localize(datetime.strptime(f"{date_str} 04:00", '%Y-%m-%d %H:%M'))
        end_datetime_est = est_timezone.localize(datetime.strptime(f"{date_str} 9:30", '%Y-%m-%d %H:%M'))
        start_timestamp_utc_ms = int(start_datetime_est.timestamp() * 1000)
        end_timestamp_utc_ms = int(end_datetime_est.timestamp() * 1000)
        aggs_data = polygon_client.list_aggs(
            ticker=ticker,
            multiplier=1,
            timespan='minute',
            from_=start_timestamp_utc_ms,
            to=end_timestamp_utc_ms,
            limit=50000
        )
        aggs_list = list(aggs_data)
        if not aggs_list:
            print(f"No data available for {ticker} between 4:00 AM and 9:30 AM EST on {date_str}")
            return None, None, None, None
        max_high = -1
        high_timestamp = None
        min_low = float('inf')
        low_timestamp = None
        for bar in aggs_list:
            if bar.high > max_high:
                max_high = bar.high
                high_timestamp = bar.timestamp
            if bar.low < min_low:
                min_low = bar.low
                low_timestamp = bar.timestamp
        high_timestamp_est = None
        if high_timestamp:
            high_datetime_utc = datetime.fromtimestamp(high_timestamp / 1000, tz=pytz.utc)
            high_datetime_est = high_datetime_utc.astimezone(est_timezone)
            high_timestamp_est = high_datetime_est.strftime('%H:%M')
        low_timestamp_est = None
        if low_timestamp:
            low_datetime_utc = datetime.fromtimestamp(low_timestamp / 1000, tz=pytz.utc)
            low_datetime_est = low_datetime_utc.astimezone(est_timezone)
            low_timestamp_est = low_datetime_est.strftime('%H:%M')
        return max_high, high_timestamp_est, min_low, low_timestamp_est
    except Exception as e:
        print(f"Error fetching data for {ticker} on {date_str} between 4:00 AM and 9:30 AM EST: {e}")
        return None, None, None, None

def get_daily_high_low_data(ticker, polygon_client, date_str):
    """
    Fetches the daily high/low and their timestamps for a given ticker and date (9:30 AM to 4:00 PM EST).
    """
    try:
        est_timezone = pytz.timezone('America/New_York')
        start_datetime_est = est_timezone.localize(datetime.strptime(f"{date_str} 09:30", '%Y-%m-%d %H:%M'))
        end_datetime_est = est_timezone.localize(datetime.strptime(f"{date_str} 16:00", '%Y-%m-%d %H:%M'))
        start_timestamp_utc_ms = int(start_datetime_est.timestamp() * 1000)
        end_timestamp_utc_ms = int(end_datetime_est.timestamp() * 1000)
        aggs_data = polygon_client.list_aggs(
            ticker=ticker,
            multiplier=1,
            timespan='minute',
            from_=start_timestamp_utc_ms,
            to=end_timestamp_utc_ms,
            limit=50000
        )
        aggs_list = list(aggs_data)
        if not aggs_list:
            print(f"No data available for {ticker} between 9:30 AM and 4:00 PM EST on {date_str}")
            return None, None, None, None
        max_high = -1
        high_timestamp = None
        min_low = float('inf')
        low_timestamp = None
        for bar in aggs_list:
            if bar.high > max_high:
                max_high = bar.high
                high_timestamp = bar.timestamp
            if bar.low < min_low:
                min_low = bar.low
                low_timestamp = bar.timestamp
        high_timestamp_est = None
        if high_timestamp:
            high_datetime_utc = datetime.fromtimestamp(high_timestamp / 1000, tz=pytz.utc)
            high_datetime_est = high_datetime_utc.astimezone(est_timezone)
            high_timestamp_est = high_datetime_est.strftime('%H:%M')
        low_timestamp_est = None
        if low_timestamp:
            low_datetime_utc = datetime.fromtimestamp(low_timestamp / 1000, tz=pytz.utc)
            low_datetime_est = low_datetime_utc.astimezone(est_timezone)
            low_timestamp_est = low_datetime_est.strftime('%H:%M')
        return max_high, high_timestamp_est, min_low, low_timestamp_est
    except Exception as e:
        print(f"Error fetching data for {ticker} on {date_str} between 9:30 AM and 4:00 PM EST: {e}")
        return None, None, None, None

def get_premarket_volume(polygon_client, ticker, date_str):
    """
    Fetches the total volume for a given ticker and date during the pre-market hours (4:00 AM to 9:30 AM EST).
    """
    try:
        est_timezone = pytz.timezone('America/New_York')
        start_datetime_est = est_timezone.localize(datetime.strptime(f"{date_str} 04:00", '%Y-%m-%d %H:%M'))
        end_datetime_est = est_timezone.localize(datetime.strptime(f"{date_str} 09:30", '%Y-%m-%d %H:%M'))
        start_timestamp_utc_ms = int(start_datetime_est.timestamp() * 1000)
        end_timestamp_utc_ms = int(end_datetime_est.timestamp() * 1000)
        
        aggs_data = polygon_client.list_aggs(
            ticker=ticker,
            multiplier=1,
            timespan='minute',
            from_=start_timestamp_utc_ms,
            to=end_timestamp_utc_ms,
            limit=50000
        )
        aggs_list = list(aggs_data)
        
        if not aggs_list:
            return 0.0
        
        premarket_total_volume = sum(bar.volume for bar in aggs_list)
        return premarket_total_volume
    except Exception as e:
        print(f"Error fetching pre-market data for {ticker} on {date_str}: {e}")
        return 0.0

def get_gap_up_day_stats(ticker, polygon_client):
    """
    Analyzes historical data for a given ticker to identify significant gap-ups.
    """
    user_input_gap_up = 25
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=1095)
    try:
        aggs_data = polygon_client.list_aggs(
            ticker=ticker,
            multiplier=1,
            timespan='day',
            from_=start_date.strftime('%Y-%m-%d'),
            to=end_date.strftime('%Y-%m-%d'),
            adjusted='true',
            limit=10000
        )
        aggs_list = list(aggs_data)
    except Exception as e:
        print(f"Error fetching daily data for {ticker}: {e}")
        return []
    gap_up_days = []
    for i in range(1, len(aggs_list)):
        previous_day_agg = aggs_list[i - 1]
        current_day_agg = aggs_list[i]
        previous_day_close = previous_day_agg.close
        current_day_open = current_day_agg.open
        current_day_volume = current_day_agg.volume
        if previous_day_close is not None and current_day_open is not None:
            gap_up_percent = ((current_day_open - previous_day_close) / previous_day_close) * 100
            if gap_up_percent >= user_input_gap_up:
                current_day_high = current_day_agg.high
                date_str = datetime.fromtimestamp(current_day_agg.timestamp / 1000).strftime('%Y-%m-%d')
                current_day_high_time = get_daily_high_low_data(ticker, polygon_client, date_str)[1]
                current_day_close = current_day_agg.close
                current_date = datetime.strptime(date_str, '%Y-%m-%d').date()
                percent_gap_high = ((current_day_high - previous_day_close) / previous_day_close) * 100 if previous_day_close is not None else None
                closing_percent = ((current_day_close - previous_day_close) / previous_day_close) * 100 if previous_day_close is not None else None
                premarket_volume = get_premarket_volume(polygon_client, ticker, date_str)
                try:
                    daily_summary = polygon_client.get_daily_open_close_agg(
                        ticker=ticker,
                        date=date_str,
                        adjusted="true",
                    )
                    premarket_open = daily_summary.pre_market if daily_summary.pre_market else None
                    premarket_high, premarket_high_time, _, _ = get_premarket_high_low_data(ticker, polygon_client, date_str)
                    afterhours_close = daily_summary.after_hours if daily_summary.after_hours else None
                except Exception as e:
                    print(f"Error fetching daily summary for {ticker} on {date_str}: {e}")
                    premarket_open = None
                    premarket_high = None
                    premarket_high_time = None
                    afterhours_close = None
                runner_fader = "Runner" if current_day_close > current_day_open else (
                    "Fader" if current_day_close < current_day_open else "Neutral")
                vwap_crosses = count_vwap_crosses(polygon_client, ticker, date_str)
                gap_up_days.append({
                    'date': date_str,
                    'pd close': previous_day_close,
                    'premarket open': premarket_open,
                    'premarket high': premarket_high,
                    'premarket high time': premarket_high_time,
                    'premarket volume': premarket_volume,  # Keep as raw volume
                    'premarket $ vol(M)': (premarket_volume * premarket_high / 1000000) if premarket_high else 0,  # Pre-market dollar volume in millions
                    'open': current_day_open,
                    'gap up % at open': gap_up_percent,
                    'day high': current_day_high,
                    'day high time': current_day_high_time,
                    'day high %': percent_gap_high,
                    'close price': current_day_close,
                    'closing percent': closing_percent,
                    'afterhours close': afterhours_close,
                    'total volume(M)': current_day_volume / 1000000,  # Convert to millions
                    'total $ vol': (current_day_volume / 1000000) * current_day_high,  # Total dollar volume in millions
                    'VWAP Crosses': vwap_crosses,
                    'Runner/Fader': runner_fader,
                })
    return gap_up_days

def analyze(tickers, polygon_client):
    """
    Example function to analyze a list of tickers and return gap up stats for each.
    """
    results = {}
    for ticker in tickers:
        print(f"Analyzing gap ups for {ticker}...")
        gap_up_days_list = get_gap_up_day_stats(ticker, polygon_client)
        results[ticker] = gap_up_days_list
    return results 