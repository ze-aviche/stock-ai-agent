from google.adk.agents import LlmAgent


def execute_trades(trades: list[str]) -> dict[str, str]:
    """Execute trades"""
    return {
        "message": "Trades executed successfully"
    }


execution_agent = LlmAgent(
    name="execution_agent",
    description="An agent that executes trades",
    tools=[execute_trades],
    model="gemini-2.0-flash",
)