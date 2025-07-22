from google.adk.agents import LLMAgent

backtesting_agent = LLMAgent(
    name="Backtesting Agent",
    description="Backtests the trade plan against historical data.",
    instructions="Simulate past performance of trade logic for validation."
)