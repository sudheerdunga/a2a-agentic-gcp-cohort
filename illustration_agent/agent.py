import os
from google_adk import Agent, tool

# Tool definition for generating an image
@tool
def generate_image(prompt: str) -> str:
    """Generates an image based on the prompt and returns a URL."""
    # In a full implementation, you would use google-genai to generate the image bytes
    # and upload them to a Google Cloud Storage bucket.
    # For this scaffolding, we return a mock URL.
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
    tools=[generate_image]
)
