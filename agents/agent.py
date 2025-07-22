from google.adk.agents import LlmAgent
from agents.prompts.prompt_trading_advisor import TRADING_ADVISOR_SYSTEM_PROMPT
from agents.gap_up_listing_agent import gap_up_listing_agent
from agents.trade_planning_agent import trade_planning_agent
from agents.risk_agent import risk_agent
from agents.backtesting_agent import backtesting_agent
from agents.execution_agent import execution_agent

root_agent = LlmAgent(
    name="trading_advisor",
    description="Root agent that handles user prompts and initiates trading pipeline.",
    instructions=TRADING_ADVISOR_SYSTEM_PROMPT,
    sub_agents = [gap_up_listing_agent, trade_planning_agent, risk_agent, backtesting_agent, execution_agent],
    model="gemini-2.0-flash"
)