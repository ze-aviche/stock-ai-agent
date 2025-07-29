from google.adk.agents import LlmAgent
from agents.gap_up_trade_workflow_agent import gap_up_trade_workflow_agent




# Main trading advisor agent
root_agent = LlmAgent(
    name="trading_advisor",
    description="Main trading advisor that orchestrates the complete trading workflow.",
    instruction="You are a comprehensive trading advisor that can identify gap-up stocks, analyze patterns, plan trades, and execute them. You coordinate with specialized agents to provide end-to-end trading solutions.",
    model="gemini-2.0-flash",
    sub_agents=[gap_up_trade_workflow_agent],
    
)