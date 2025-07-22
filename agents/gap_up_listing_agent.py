from google.adk.agents import LlmAgent
from agents.prompts.prompt_gap_up_listing_agent import GAP_UP_LISTING_AGENT_PROMPT
from api_helper.polygon_api_helper import get_gap_up_list

gap_up_listing_agent = LlmAgent(
    name="gap_up_listing_agent",
    description="Identifies gap-up tickers using market APIs like Polygon.",
    instruction=GAP_UP_LISTING_AGENT_PROMPT,
    model="gemini-2.0-flash",
    tools=[get_gap_up_list]
)