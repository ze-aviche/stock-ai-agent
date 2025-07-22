from google.adk.agents import LLMAgent

risk_agent = LLMAgent(
    name="Risk Agent",
    description="Evaluates risk parameters for a proposed trade.",
    instructions="Assess position sizing, stop loss, max loss %, and other risk settings."
)