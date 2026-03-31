import os
from google.adk import Agent
from google.adk.tools.function_tool import FunctionTool

# Tool definition for generating an image
def generate_image(prompt: str) -> str:
    """Generates an image based on the prompt and returns a URL."""
    print(f"Generating branded image for prompt: {prompt}")
    mock_url = f"https://storage.googleapis.com/your-bucket/mock-image.png"
    return mock_url

# Define the ADK Agent
root_agent = Agent(
    name="illustration_agent",
    instructions="""
    You are an illustration agent for Cymbal Stadiums. 
    Always use the generate_image tool. 
    Ensure prompts use a Corporate Memphis style with purples and greens on sunset gradients.
    """,
    tools=[FunctionTool(generate_image)]
)
