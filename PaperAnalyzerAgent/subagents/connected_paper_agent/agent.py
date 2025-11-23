from google.adk.agents.llm_agent import Agent
from google.adk.tools.google_search_tool import GoogleSearchTool
from .prompt import INSTRUCTION

connected_paper_agent = Agent(
    model='gemini-2.5-flash',
    name='connected_paper_agent',
    description='Performs a Connected Paper analysis based on co-citation and bibliographic matching.',
    instruction=INSTRUCTION,
    tools=[GoogleSearchTool(bypass_multi_tools_limit=True)],
    output_key="connected_paper_result"
)
