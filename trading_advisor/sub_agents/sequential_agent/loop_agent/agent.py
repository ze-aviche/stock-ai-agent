from google.adk.agents import LoopAgent
from .trade_planning_agent.agent import trade_planning_agent
from .risk_agent.agent import risk_agent
from .backtesting_agent.agent import backtesting_agent


trade_planning_loop_agent = LoopAgent(
    name="trade_planning_loop_agent",
    description="An agent that loops through the trading planning process",
    sub_agents = [trade_planning_agent, risk_agent, backtesting_agent],
    max_iterations=3,
)