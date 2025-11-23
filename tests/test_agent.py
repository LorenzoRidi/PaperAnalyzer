import asyncio
import sys
import os

# Add the project root to the python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from PaperAnalyzerAgent.agent import root_agent, runner

async def test_agent_structure():
    print("Verifying agent structure...")
    assert root_agent.name == "root_agent"
    assert len(root_agent.sub_agents) == 4
    
    sub_agent_names = [agent.name for agent in root_agent.sub_agents]
    expected_names = ["overview_agent", "innovation_agent", "bibliographic_agent", "connected_paper_agent"]
    
    for name in expected_names:
        assert name in sub_agent_names, f"Missing sub-agent: {name}"
        print(f"Found sub-agent: {name}")
        
    print("Agent structure verified successfully.")

async def main():
    await test_agent_structure()
    print("All tests passed!")

if __name__ == "__main__":
    asyncio.run(main())
