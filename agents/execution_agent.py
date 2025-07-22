from google.adk.agents import LlmAgent
#from db.trades_db import insert_trade_from_alpaca
from agents.prompts.prompt_execution_agent import EXECUTION_AGENT_PROMPT
#import alpaca_trade_api as tradeapi

#from alpaca.trading.client import TradingClient
#from alpaca.trading.requests import MarketOrderRequest
#from alpaca.trading import enums

# Replace with your actual API keys
API_KEY = 'YOUR_API_KEY'
API_SECRET = 'YOUR_API_SECRET'

# Instantiate the TradingClient. Set paper=True for paper trading.
#trading_client = TradingClient(API_KEY, API_SECRET, paper=True) # Or paper=False for live trading


#api = tradeapi.REST("APCA_API_KEY_ID", "APCA_API_SECRET_KEY", base_url="https://paper-api.alpaca.markets")

# Example: Buy 1 share of AAPL at market price
# order_data = MarketOrderRequest(
#     symbol="AAPL",
#     qty=1,
#     side=enums.OrderSide.BUY,
#     time_in_force=enums.TimeInForce.DAY
# )
#order = trading_client.submit_order(order_data=order_data)

#print(f"Order submitted: {order}")


def execute_trade(ticker, qty, side="buy"):
    print(f"🚀 Executing trade: {side.upper()} {qty} shares of {ticker}")
    
    # order = api.submit_order(
    #     symbol=ticker,
    #     qty=qty,
    #     side=side,
    #     type="market",
    #     time_in_force="gtc"
    # )

    # Wait for fill or query after delay (in real world, handle async via webhook)
    # #order_result = api.get_order(order.id)
    # print(f"✅ Order response: {order_result}")

    # # Insert into DB
    # insert_trade_from_alpaca(order_result._raw)

    # return order_result


    execution_agent = LlmAgent(
    name="execution_agent",
    description="Executes approved trades using Alpaca API.",
    instructions=EXECUTION_AGENT_PROMPT,
    model="gemini-2.0-flash"
)