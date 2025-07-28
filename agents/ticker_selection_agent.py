from google.adk.agents import BaseAgent
from google.adk.events import Event
from google.adk.agents.invocation_context import InvocationContext
from typing import AsyncGenerator


class TickerSelectionAgent(BaseAgent):
    def __init__(self, name="ticker_selection_agent"):
        super().__init__(name=name)

    def run(self, state: dict) -> dict:
        ticker_string = state.get("tickers", "")
        if not ticker_string:
            print("No tickers found in input.")
            return state

        tickers = [t.strip().upper() for t in ticker_string.split(",") if t.strip()]
        
        print("\nTickers identified by LLM:")
        for i, ticker in enumerate(tickers, 1):
            print(f"{i}. {ticker}")

        selected_input = input("\nEnter one or more ticker numbers or symbols (comma-separated): ").strip()
        selected_set = set()

        for s in selected_input.split(","):
            s = s.strip().upper()
            if s.isdigit():
                idx = int(s) - 1
                if 0 <= idx < len(tickers):
                    selected_set.add(tickers[idx])
            elif s in tickers:
                selected_set.add(s)

        selected_ticker_string = ", ".join(sorted(selected_set))

        print(f"\nSelected tickers: {selected_ticker_string}")
        state["selected_tickers"] = selected_ticker_string
        return state

    async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
        state = ctx.state.copy()
        updated_state = self.run(state)
        ctx.state.update(updated_state)
        yield Event.final(ctx.state)
