import requests
import json
from google.adk import Agent
from google.adk.tools.function_tool import FunctionTool

# 1. Define the function for the remote Illustration Agent
def call_illustration_agent(prompt: str) -> str:
    """Calls the remote illustration agent on Cloud Run to generate an image."""
    url = "https://illustration-agent-356811965041.us-central1.run.app/a2a/illustration_agent"
    print(f"Calling remote illustration agent with prompt: {prompt}")
    return f"Image generated for: {prompt}. URL: https://storage.googleapis.com/your-bucket/mock-image.png"

# 2. Define the main Orchestrator Agent
root_agent = Agent(
    name="slide_content_agent",
    instructions="""
    You are a presentation assistant. When a user asks for a slide:
    1. Write a headline and a couple of sentences of body text.
    2. Use the call_illustration_agent tool to generate an image for the slide.
    """,
    tools=[FunctionTool(call_illustration_agent)]
)

if __name__ == "__main__":
    root_agent.run()
