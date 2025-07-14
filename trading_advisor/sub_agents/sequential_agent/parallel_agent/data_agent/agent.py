from google.adk.agents import LlmAgent


def get_historical_data() -> dict[str, list[str]]:
    """Fetch all small cap stocks"""
    return {
            "message": ["AAPL", "GOOG", "MSFT", "AMZN", "TSLA"]
            }


data_agent = LlmAgent(
    name="data_agent",
    description="An agent that fetches and processes data",
    tools=[get_historical_data],
    model="gemini-2.0-flash",
    output_key="historical_data_of_gap_up_stocks",
)