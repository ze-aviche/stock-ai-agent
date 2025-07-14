from google.adk.agents import LlmAgent
from . import prompt

GAP_UP_LISTING_AGENT_PROMPT = prompt.GAP_UP_LISTING_AGENT_PROMPT
MODEL = "gemini-2.5-pro"

def fetch_gap_up_stocks() -> dict[str, list[str]]:
    """Fetch gap up stocks for today's trading session"""
    return {
        "message": ["EVOK", "SNDL", "MSTR", "KODK"]
    }

gap_up_listing_agent = LlmAgent(
    name="gap_up_listing_agent",
    description="An agent that lists gap up stocks for today's trading session",
    instruction=GAP_UP_LISTING_AGENT_PROMPT,
    model=MODEL,
    tools=[fetch_gap_up_stocks],
    output_key="list_of_todays_gap_up_stocks",
)