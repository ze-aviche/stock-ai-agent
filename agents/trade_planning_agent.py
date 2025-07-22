from google.adk.agents import SequentialAgent
from agents.risk_agent import risk_agent
from agents.backtesting_agent import backtesting_agent
from agents.prompts.prompt_trade_planning_agent import TRADE_PLANNING_AGENT_PROMPT

trade_planning_agent = SequentialAgent(
    name="trade_planning_agent",
    description="Creates a trade plan by analyzing data, risk, and simulation results.",
    steps=[risk_agent, backtesting_agent],
    model="gemini-2.0-flash"
)