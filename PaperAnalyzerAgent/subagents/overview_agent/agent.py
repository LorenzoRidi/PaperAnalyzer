from google.adk.agents.llm_agent import Agent
from .prompt import INSTRUCTION

# Define sub-agents
overview_agent = Agent(
    model='gemini-2.5-flash',
    name='overview_agent',
    description='Provides a technical, scientific, and market assessment of the document.',
    instruction=INSTRUCTION,
    output_key="overview_result"
)