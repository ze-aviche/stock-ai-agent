from google.adk.agents import LlmAgent
from agents.prompts.prompt_execution_agent import EXECUTION_AGENT_PROMPT
from api_helper.execute_trades_alpaca import (
    get_current_price,
    place_market_order,
    place_stop_order,
    place_limit_order,
    check_order_status,
    monitor_and_execute
)

# Execution Agent Definition
execution_agent = LlmAgent(
    name="execution_agent",
    description="Executes trades based on planning agent recommendations using Alpaca paper trading",
    instruction=EXECUTION_AGENT_PROMPT,
    model="gemini-2.0-flash",
    tools=[
        get_current_price,
        place_market_order,
        place_stop_order,
        place_limit_order,
        check_order_status,
        monitor_and_execute
    ]
)