import vertexai
#from absl import app, flags
from dotenv import load_dotenv
from agents.agent import root_agent
from vertexai import agent_engines
from vertexai.preview.reasoning_engines import AdkApp
from api_helper.config.vertex_env import PROJECT_ID, LOCATION, STAGING_BUCKET

vertexai.init(
    project=PROJECT_ID, location=LOCATION, staging_bucket=STAGING_BUCKET
    )

app = AdkApp(
    name=root_agent,
    description="A trading advisor that uses AI to analyze market data and make trading decisions.",
    
    enable_tracing=True,
)

remote_app = agent_engines.create(
    agent_engine=app,
    requirements=[
        "google-cloud-aiplatform[adk, agent-engines]"
    ], 
    extra_packages=["./"],    
)







