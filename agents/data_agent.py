from google.adk.agents import LlmAgent
from agents.prompts.prompt_data_agent import DATA_AGENT_PROMPT

data_agent = LlmAgent(
    name="data_agent",
    description="Fetches current and historical market data for a given ticker.",
    instructions=DATA_AGENT_PROMPT,
    model="gemini-2.0-flash"
)