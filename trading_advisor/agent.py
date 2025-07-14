from google.adk.agents import Agent
from sub_agents.sequential_agent.agent import sequential_agent
from prompt import TRADING_ADVISOR_SYSTEM_PROMPT


def get_stock_price(stock_symbol: float) -> dict[str, str]:
    """Get the current price of a stock"""
    if stock_symbol == "AAPL":
        return {"status": "success",
                "message": "Stock price for AAPL is 100"
                }

    else:
        return {
            "error": "Stock symbol not found",
            "error_message": f"Stock symbol {stock_symbol} not found"
        }


root_agent = Agent(
    name="trading_advisor_agent",
    description="An AI agent that analyzes stock data and provides trading recommendations",
    instruction=TRADING_ADVISOR_SYSTEM_PROMPT,
    tools=[get_stock_price],
    sub_agents=[sequential_agent],
    model="gemini-2.0-flash",
    
)





