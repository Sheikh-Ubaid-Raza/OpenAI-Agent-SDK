from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from agents.run import RunConfig
from dotenv import load_dotenv
import asyncio
import os
# enable_verbose_stdout_logging()

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

my_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=my_model,
    model_provider=external_client,
    tracing_disabled=True
)

@function_tool
def get_weather(city: str) -> str:
    """
    This is tool for getting weather from city

    Args:
    This tool get city as argument
    
    Returns:
    This tool return the weather of given city
    """
    return f"Weather in {city} is sunny and 30°C."

async def main():

    agent = Agent(
        name="AI Assistant",
        instructions="You are a helpful Ai Assistant, use get_weather tool if someone asking about weather",
        tools=[get_weather]
    )

    result = await Runner.run(
        agent,
        "What is the weather in Islamabad?",
        run_config=config
    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())