from google.adk.agents import LlmAgent, SequentialAgent
from agents.prompts.prompt_gap_up_listing_agent import GAP_UP_LISTING_AGENT_PROMPT
from api_helper.polygon_api_get_gap_ups import get_gap_up_list, get_ticker_details
from agents.data_agent import data_agent
from agents.trade_planning_agent import trade_planning_agent
from agents.ticker_selection_agent import TickerSelectionAgent

gap_up_llm_agent = LlmAgent(
    name="gap_up_llm_agent",
    description="Identifies gap-up tickers using market APIs like Polygon.",
    instruction=GAP_UP_LISTING_AGENT_PROMPT,
    model="gemini-2.0-flash",
    tools=[get_gap_up_list, get_ticker_details],
    output_key="list_of_todays_gap_up_stocks"
)

# user_input_agent = UserInputAgent(
#     name = "user_input_agent", 
#     prompt="Please enter the stock ticker you'd like to analyze further for trade planning:",
#     input_key="selected_ticker",
#     output_key="selected_ticker"
# )

# ticker_selection_agent = UserInputAgent(
#     name="ticker_selection_agent",
#     prompt="Here are the tickers identified:\n{tickers}\n\nPlease enter one or more tickers (comma-separated):",
#     input_key="tickers",              # ✅ string literal
#     output_key="selected_tickers"     # ✅ string literal
# )

gap_up_listing_agent = SequentialAgent(
    name="gap_up_listing_agent",
    #sub_agents=[gap_up_llm_agent, TickerSelectionAgent(), data_agent, trade_planning_agent],
    sub_agents=[gap_up_llm_agent, data_agent],
)