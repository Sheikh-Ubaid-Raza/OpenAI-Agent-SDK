from agents import AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from dotenv import load_dotenv
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