from google.adk.agents.llm_agent import Agent
from google.adk.tools.google_search_tool import GoogleSearchTool
from .prompt import INSTRUCTION

bibliographic_agent = Agent(
    model='gemini-2.5-flash',
    name='bibliographic_agent',
    description='Performs a bibliographic analysis mapping the academic context.',
    instruction=INSTRUCTION,
    tools=[GoogleSearchTool(bypass_multi_tools_limit=True)],
    output_key="bibliographic_result"
)