from google_adk import Agent
from a2a_sdk import RemoteA2aAgent

# 1. Initialize the remote agent using its Agent Card
illustration_agent = RemoteA2aAgent(
    name="illustration_agent",
    description="Agent that generates illustrations.",
    agent_card="illustration-agent-card.json",
)

# 2. Define the main Orchestrator Agent and add the remote agent as a sub-agent
root_agent = Agent(
    name="slide_content_agent",
    instructions="""
    You are a presentation assistant. When a user asks for a slide, 
    write a headline and a couple of sentences of body text. 
    Then, transfer the context to the illustration_agent to generate an image for the slide.
    """,
    sub_agents=[illustration_agent]
)
