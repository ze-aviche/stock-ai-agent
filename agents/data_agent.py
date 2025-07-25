from google.adk.agents import LlmAgent
from agents.prompts.prompt_data_agent import DATA_AGENT_PROMPT
from api_helper.wrapper_functions import analyze_tool, get_gap_up_day_stats_tool, get_daily_high_low_data_tool, get_premarket_high_low_data_tool, get_premarket_volume_tool, count_vwap_crosses_tool

data_agent = LlmAgent(
    name="data_agent",
    description="Fetches current and historical market data for a given ticker.",
    instruction=DATA_AGENT_PROMPT,
    model="gemini-2.0-flash", 
    tools=[analyze_tool, get_gap_up_day_stats_tool, get_daily_high_low_data_tool, get_premarket_high_low_data_tool, get_premarket_volume_tool, count_vwap_crosses_tool]
)