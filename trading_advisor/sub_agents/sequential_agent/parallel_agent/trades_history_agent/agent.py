from google.adk.agents import Agent
from . import prompt

TRADES_HISTORY_PROMPT = prompt.TRADES_HISTORY_AGENT_PROMPT

def get_trades_history(tickers: list[str]) -> dict[str, str]:
    """Get trades history"""
    return {
        "message": "Trades history"
        #[TODO] make a query to the database to get the trades history
    }

trades_history_agent = Agent(
    name="trades_history_agent",
    description="An agent that gets trades history",
    instruction=TRADES_HISTORY_PROMPT,
    model="gemini-2.5-pro",
    tools=[get_trades_history], # TODO: Add tools
)