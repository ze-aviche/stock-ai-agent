from google.adk.agents import LlmAgent
from agents.prompts.prompt_trades_history_agent import TRADES_HISTORY_AGENT_PROMPT

trade_history_agent = LlmAgent(
    name="trade_history_agent",
    description="Checks if a ticker has been previously traded and fetches historical data from DB.",
    instructions=TRADES_HISTORY_AGENT_PROMPT,
    model="gemini-2.0-flash"
)