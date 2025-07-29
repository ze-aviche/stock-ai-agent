from google.adk.agents import Agent
from agents.risk_agent import risk_agent
from agents.backtesting_agent import backtesting_agent
from agents.prompts.prompt_trade_planning_agent import TRADE_PLANNING_AGENT_PROMPT
from google.genai import types
from google.adk.planners import BuiltInPlanner

trade_planning_agent = Agent(
    name="trade_planning_agent",
    description="Trade planning agent that plans the trades for the tickers",
    instruction=TRADE_PLANNING_AGENT_PROMPT,
    model="gemini-2.0-flash",
    planner=BuiltInPlanner(
        thinking_config=types.ThinkingConfig(
            include_thoughts=True
        )
    ),
    #tools=[],
    output_key="trade_planning"
)