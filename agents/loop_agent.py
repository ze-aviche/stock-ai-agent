from google.adk.agents import LoopAgent
from agents.trade_planning_agent import trade_planning_agent

loop_agent = LoopAgent(
    name="Trade Loop Agent",
    description="Refines trade plan iteratively through risk and backtesting validation.",
    agent=trade_planning_agent,
    max_iterations=3
)