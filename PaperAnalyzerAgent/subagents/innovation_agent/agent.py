from google.adk.agents.llm_agent import Agent
from .prompt import INSTRUCTION

innovation_agent = Agent(
    model='gemini-2.5-flash',
    name='innovation_agent',
    description='Analyzes the importance of innovation compared to conventional treatments.',
    instruction=INSTRUCTION,
    output_key="innovation_result"
)
