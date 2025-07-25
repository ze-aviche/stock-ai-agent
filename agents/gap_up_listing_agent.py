from google.adk.agents import LlmAgent, SequentialAgent
from agents.prompts.prompt_gap_up_listing_agent import GAP_UP_LISTING_AGENT_PROMPT
from api_helper.polygon_api_get_gap_ups import get_gap_up_list, get_ticker_details
from agents.data_agent import data_agent

gap_up_llm_agent = LlmAgent(
    name="gap_up_llm_agent",
    description="Identifies gap-up tickers using market APIs like Polygon.",
    instruction=GAP_UP_LISTING_AGENT_PROMPT,
    model="gemini-2.0-flash",
    tools=[get_gap_up_list, get_ticker_details],
)

gap_up_listing_agent = SequentialAgent(
    name="gap_up_listing_agent",
    sub_agents=[gap_up_llm_agent, data_agent],
)