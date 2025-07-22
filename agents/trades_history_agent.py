from google.adk.agents import LLMAgent

trade_history_agent = LLMAgent(
    name="Trade History Agent",
    description="Checks if a ticker has been previously traded and fetches historical data from DB.",
    instructions="Query trades DB to check and retrieve previous trades for given ticker."
)