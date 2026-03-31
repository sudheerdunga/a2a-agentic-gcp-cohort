FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the agent code to an agent-specific folder so adk CLI can discover it
COPY . /app/agents/illustration_agent/

# Cloud Run expects the service to listen on the port defined by $PORT
ENV PORT=8080

# Start the ADK agent as an A2A server using the adk CLI
CMD ["sh", "-c", "adk api_server --host 0.0.0.0 --port $PORT --a2a /app/agents"]
