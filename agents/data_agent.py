from google.adk.agents import LlmAgent
from agents.prompts.prompt_data_agent import DATA_AGENT_PROMPT
from api_helper.polygon_api_get_historical_data import analyze, get_gap_up_day_stats, get_daily_high_low_data, get_premarket_high_low_data, get_premarket_volume, count_vwap_crosses

data_agent = LlmAgent(
    name="data_agent",
    description="Fetches current and historical market data for a given ticker.",
    instruction=DATA_AGENT_PROMPT,
    model="gemini-2.0-flash", 
    tools=[analyze, get_gap_up_day_stats, get_daily_high_low_data, get_premarket_high_low_data, get_premarket_volume, count_vwap_crosses]
)