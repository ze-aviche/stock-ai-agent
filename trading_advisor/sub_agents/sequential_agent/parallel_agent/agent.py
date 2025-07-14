from google.adk.agents import ParallelAgent
from .data_agent.agent import data_agent
from .trades_history_agent.agent import trades_history_agent  


parallel_agent = ParallelAgent(
    name="parallel_agent",
    description="An agent that runs in parallel",
    sub_agents = [data_agent, trades_history_agent],
)