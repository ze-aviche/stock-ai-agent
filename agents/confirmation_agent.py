import asyncio
from google.adk.agents import LlmAgent
from google.adk.sessions import InMemorySessionService, Session
from google.adk.runners import Runner
from google.genai.types import Content, Part
import os

# Set API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyAv4mRR2Hbb4x8ek4YAw20T7m9uWCw-jWw"

class ConfirmationAgent:
    def __init__(self, previous_agent_name="previous agent", next_agent_name="next agent"):
        self.previous_agent_name = previous_agent_name
        self.next_agent_name = next_agent_name
        
        self.confirmation_agent = LlmAgent(
            name="confirmation_agent",
            description="Confirms completion of previous agent and asks for permission to proceed",
            instruction=f"""
            You are a confirmation agent that:
            1. Confirms that the {self.previous_agent_name} has completed its work
            2. Summarizes what was accomplished
            3. Asks the user if they want to proceed to the {self.next_agent_name}
            4. Waits for user confirmation (yes/no/y/n)
            
            Always end your response with a clear question asking for permission to proceed.
            Be polite and professional in your communication.
            """,
            model="gemini-2.0-flash"
        )
        
        self.session_service = InMemorySessionService()
        self.runner = Runner(
            app_name="confirmation_workflow",
            agent=self.confirmation_agent,
            session_service=self.session_service
        )
    
    async def confirm_and_proceed(self, previous_results=None, user_message=None):
        """
        Confirms previous agent completion and asks for permission to proceed.
        
        Args:
            previous_results: Results from the previous agent (optional)
            user_message: Custom message from user (optional)
        
        Returns:
            bool: True if user confirms to proceed, False otherwise
        """
        # Create session
        session = await self.session_service.create_session(
            app_name="confirmation_workflow",
            user_id="user",
            session_id="confirmation_session"
        )
        
        # Prepare the confirmation message
        if user_message:
            confirmation_message = f"""
            The {self.previous_agent_name} has completed its work.
            
            {user_message}
            
            Previous results: {previous_results if previous_results else 'No specific results to show'}
            
            Are you ready to proceed to the {self.next_agent_name}? Please respond with yes/no.
            """
        else:
            confirmation_message = f"""
            The {self.previous_agent_name} has completed its work successfully.
            
            Previous results: {previous_results if previous_results else 'No specific results to show'}
            
            Are you ready to proceed to the {self.next_agent_name}? Please respond with yes/no.
            """
        
        # Run the confirmation agent
        content = Content(parts=[Part(text=confirmation_message)])
        
        print(f"\n{'='*60}")
        print(f"CONFIRMATION: {self.previous_agent_name.upper()} → {self.next_agent_name.upper()}")
        print(f"{'='*60}")
        
        for event in self.runner.run(user_id="user", session_id="confirmation_session", new_message=content):
            if event.content and event.content.parts:
                print(f"Agent: {event.content.parts[0].text}")
        
        # Get user response
        print(f"\n{'='*60}")
        user_response = input("Your response (yes/no/y/n): ").strip().lower()
        print(f"{'='*60}")
        
        # Check if user confirmed
        if user_response in ['yes', 'y', 'proceed', 'continue', 'ok', 'okay']:
            print(f"✅ Confirmed! Proceeding to {self.next_agent_name}...")
            return True
        else:
            print(f"❌ Cancelled. Stopping workflow before {self.next_agent_name}.")
            return False

# Example usage
async def example_usage():
    # Create confirmation agent
    confirm_agent = ConfirmationAgent(
        previous_agent_name="Gap Up Listing Agent",
        next_agent_name="Data Analysis Agent"
    )
    
    # Simulate previous agent results
    previous_results = {
        "gap_up_tickers": ["LIDR", "AAPL", "MSFT"],
        "total_tickers_processed": 150,
        "gap_up_count": 3
    }
    
    # Ask for confirmation
    should_proceed = await confirm_agent.confirm_and_proceed(
        previous_results=previous_results,
        user_message="Found 3 gap-up stocks. Ready to analyze historical data?"
    )
    
    if should_proceed:
        print("Proceeding with data analysis...")
        # Continue with next agent
    else:
        print("Workflow stopped by user.")

if __name__ == "__main__":
    asyncio.run(example_usage()) 