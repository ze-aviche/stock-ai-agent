from google.adk.agents import LLMAgent

gap_up_listing_agent = LLMAgent(
    name="Gap Up Listing Agent",
    description="Identifies gap-up tickers using market APIs like Polygon.",
    instructions="Fetch today's gap-up stocks from Polygon API."
)