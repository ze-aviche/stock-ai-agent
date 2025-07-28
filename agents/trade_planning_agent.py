from google.adk.agents import LoopAgent
from agents.risk_agent import risk_agent
from agents.backtesting_agent import backtesting_agent
from agents.prompts.prompt_trade_planning_agent import TRADE_PLANNING_AGENT_PROMPT

trade_planning_agent = LoopAgent(
    name="trade_planning_agent",
    sub_agents=[risk_agent, backtesting_agent],
    max_iterations=2
)