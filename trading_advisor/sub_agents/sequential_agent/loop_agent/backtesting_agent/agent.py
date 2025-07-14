from google.adk.agents import LlmAgent
from . import prompt

BACKTESTING_PROMPT = prompt.BACKTESTING_AGENT_PROMPT

def backtest_strategy(tickers: list[str], strategies: list[str]) -> dict[str, str]:
    """Backtest a trading strategy"""
    return {
        "message": "Backtest results"
    }

backtesting_agent = LlmAgent(
    name="backtesting_agent",
    description="An agent that backtests trading strategies",
    instruction=BACKTESTING_PROMPT,
    model="gemini-2.5-pro",
    tools=[backtest_strategy], # TODO: Add tools
)