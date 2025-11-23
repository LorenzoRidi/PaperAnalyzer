from google.adk.agents import SequentialAgent
from google.adk.agents.callback_context import CallbackContext
from google.genai import types
from google.adk.runners import Runner
from google.adk.artifacts import InMemoryArtifactService
from google.adk.sessions import InMemorySessionService

from .subagents.overview_agent.agent import overview_agent
from .subagents.innovation_agent.agent import innovation_agent
from .subagents.bibliographic_agent.agent import bibliographic_agent
from .subagents.connected_paper_agent.agent import connected_paper_agent

async def load_paper(callback_context: CallbackContext):
    result = types.Content(role="model")
    print(callback_context.user_content.parts)

    for part in callback_context.user_content.parts:
        if part.inline_data:
            try:
                version = await callback_context.save_artifact(filename="paper.pdf", artifact=part)
                result = None
            except Exception as e:
                print(f"An unexpected error occurred when saving artifact: {e}")
                result.parts = [types.Part(text="Error while reading your PDF file")]
        else:
            result.parts = [types.Part(text="You need to attach a PDF file")]

    return result

root_agent = SequentialAgent(
    name='root_agent',
    description='A helpful assistant for analyzing research papers.',
    before_agent_callback=load_paper,
    sub_agents=[overview_agent, innovation_agent, bibliographic_agent, connected_paper_agent]
)

# Instantiate the desired artifact service
artifact_service = InMemoryArtifactService()

# Provide it to the Runner
runner = Runner(
    agent=root_agent,
    app_name="paper_analyzer",
    session_service=InMemorySessionService(),
    artifact_service=artifact_service # Service must be provided here
)