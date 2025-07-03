from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Agent, Runner
from agents.run import RunConfig
from dotenv import load_dotenv
import asyncio
import os

# Load environment variables from .env file
load_dotenv()

# Read Gemini API key from environment
API_KEY = os.environ.get("GEMINI_API_KEY")

# Create an AsyncOpenAI client with Gemini base URL
external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Define the model to use (Gemini in this case)
gemini_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Configure how the agent should run
my_config = RunConfig(
    model=gemini_model,
    model_provider=external_client,
    tracing_disabled=True
)

# Define the async function to run the agent inside loop
async def main():
    # Create the agent once (reuse for every interaction)
    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant",
    )

    # Start chat loop
    while True:
        user_input = input("Ask Anything: ")

        if user_input.lower() in ['quit', 'exit', 'bye']:
            print("Goodbye!")
            break

        # Run the agent with the user input
        response = await Runner.run(agent, user_input, run_config=my_config)
        print("Agent:", response.final_output)

# Run the main loop
if __name__ == "__main__":
    asyncio.run(main())
