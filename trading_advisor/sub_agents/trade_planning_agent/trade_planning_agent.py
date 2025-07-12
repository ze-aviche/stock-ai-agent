from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from . import prompt
from google.adk import Agent


MODEL = "gemini-2.5-pro"

trading_agent = Agent(
    model=MODEL,
    instructions= prompt.TRADING_AGENT_PROMPT,
    name="trading_agent",
    output_key="proposed_trading_strategies",
)
