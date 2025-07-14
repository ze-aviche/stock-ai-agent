from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from . import prompt
from google.adk import Agent


MODEL = "gemini-2.5-pro"

trade_planning_agent = Agent(
    model=MODEL,
    instruction= prompt.TRADING_AGENT_PROMPT,
    name="trading_planning_agent",
    output_key="proposed_trading_strategies",
)
