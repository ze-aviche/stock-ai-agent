from google.adk.agents import LlmAgent
from agents.prompts.prompt_backtesting_agent import BACKTESTING_AGENT_PROMPT

backtesting_agent = LlmAgent(
    name="backtesting_agent",
    description="Backtests the trade plan against historical data.",
    instruction=BACKTESTING_AGENT_PROMPT,
    model="gemini-2.0-flash"
)