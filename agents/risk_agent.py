from google.adk.agents import LlmAgent
from agents.prompts.prompt_risk_agent import RISK_AGENT_PROMPT

risk_agent = LlmAgent(
    name="risk_agent",
    description="Evaluates risk parameters for a proposed trade.",
    instruction=RISK_AGENT_PROMPT,
    model="gemini-2.0-flash"
)