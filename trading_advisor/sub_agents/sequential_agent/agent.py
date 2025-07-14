from google.adk.agents import SequentialAgent
from .gap_up_listing_agent.agent import gap_up_listing_agent
from .parallel_agent.agent import parallel_agent
from .execution_agent.agent import execution_agent
from .loop_agent.agent import loop_agent

sequential_agent = SequentialAgent(
    name="sequential_agent",
    description="An agent that runs in sequential",
    sub_agents = [gap_up_listing_agent, parallel_agent, loop_agent, execution_agent],
)