from google.adk.agents import Agent
from .sub_agents.data_agent.agent import data_agent
from .sub_agents.gap_up_listing_agent.agent import gap_up_listing_agent
from .sub_agents.risk_agent.agent import risk_agent
from .sub_agents.trade_planning_agent.agent import trade_planning_agent
from .sub_agents.backtesting_agent.agent import backtesting_agent
from .sub_agents.execution_agent.agent import execution_agent

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
    tools=[get_stock_price],
    sub_agents=[data_agent, gap_up_listing_agent, risk_agent, trade_planning_agent, backtesting_agent, execution_agent],
    model="gemini-2.0-flash",
    
)





