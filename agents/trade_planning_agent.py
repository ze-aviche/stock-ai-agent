from google.adk.agents import SequentialAgent
from agents.risk_agent import risk_agent
from agents.backtesting_agent import backtesting_agent

trade_planning_agent = SequentialAgent(
    name="Trade Planning Agent",
    description="Creates a trade plan by analyzing data, risk, and simulation results.",
    steps=[risk_agent, backtesting_agent]
)