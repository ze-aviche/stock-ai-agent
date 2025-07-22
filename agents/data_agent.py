from google.adk.agents import LLMAgent

data_agent = LLMAgent(
    name="Data Agent",
    description="Fetches current and historical market data for a given ticker.",
    instructions="Use Polygon and Alpaca APIs to get relevant data for analysis."
)