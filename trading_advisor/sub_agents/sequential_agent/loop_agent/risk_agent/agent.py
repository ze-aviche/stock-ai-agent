from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool
from . import prompt

MODEL = "gemini-2.5-pro"
RISK_PROMPT = prompt.RISK_AGENT_PROMPT

def google_search(query: str) -> dict[str, str]:
    """Search the web for the query"""
    return {
        "message": "Search results for the query"
    }

risk_agent = LlmAgent(
    name="risk_agent",
    description="An agent that calculates risk",
    instruction=RISK_PROMPT,
    tools=[google_search], # TODO: Add tools
    model=MODEL,
    output_key="risk_assessment",
)