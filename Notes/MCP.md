
# Model Context Protocol (MCP) Notes

## What is the Model Context Protocol (MCP)?

The Model Context Protocol (MCP) is a standardized way to provide tools and context to a Large Language Model (LLM) within the OpenAI Agents SDK. Think of it as a bridge that connects your AI agent to external tools (like functions or APIs) and gives the LLM the information it needs to use them effectively. MCP ensures that tool calls are safe, structured, and reliable, making it easier for agents to perform real-world tasks like fetching data, querying databases, or interacting with APIs.  
In simpler terms, MCP is like a set of rules that helps the LLM understand what tools are available, how to use them, and what context (like user input or conversation history) to consider when making decisions.

## How Does MCP Work?

MCP acts as a middleman between the LLM and the tools you define for your agent. It does two main things:

- **Provides Context**: MCP sends the LLM details about the tools it can use, the current conversation history, and any relevant data (like user input). This helps the LLM decide whether to respond with text or call a tool.
- **Sanitizes Tool Calls**: MCP ensures that when the LLM wants to use a tool, it sends a properly formatted request (e.g., specifying the tool name and correct arguments). This prevents errors, like the LLM passing invalid data to a tool.

The OpenAI Agents SDK has built-in support for MCP, allowing you to connect your agents to MCP servers—special services that manage tool definitions and execution. These servers act like a central hub, providing a wide range of tools that multiple agents can access without you needing to redefine them for each agent.  
**Example**: Imagine you have an agent that answers questions about weather. MCP tells the LLM about a `get_weather` tool, including what inputs it needs (like a city name). When you ask, “What’s the weather in Paris?”, the LLM uses MCP to safely call the tool with the correct city name and get the result.

## Why Use MCP?

MCP makes building AI agents easier and safer by:

- **Simplifying Tool Integration**: You don’t need to hardcode every tool into your agent’s code. MCP servers provide a centralized way to manage and share tools.
- **Ensuring Safety**: MCP validates tool calls to prevent errors or misuse (e.g., calling a tool with wrong or harmful inputs).
- **Enabling Flexibility**: With MCP, you can connect your agent to different MCP servers, giving access to a wide variety of tools and LLMs without changing your code.
- **Supporting Scalability**: MCP allows multiple agents to share the same tools and context, making it easier to build complex multi-agent systems.

## Key Features of MCP in the OpenAI Agents SDK

- **Tool Management**: MCP lets you define tools (like Python functions) and share them with the LLM via an MCP server. The LLM can then decide when and how to use them.
- **Context Sharing**: MCP ensures the LLM has the right context (e.g., user input, conversation history) to make informed decisions.
- **Sanitization**: MCP checks that tool calls are valid and safe, using schemas (like Pydantic) to enforce correct data formats.
- **M MCP Server Support**: The Agents SDK can connect to external MCP servers, which provide a library of tools and handle their execution.
- **Interoperability**: MCP works with different LLMs and toolsets, making your agents more flexible.

## How MCP Fits into the OpenAI Agents SDK

In the OpenAI Agents SDK, MCP is integrated into the agent loop—the process where the agent interacts with the LLM, processes tool calls, and produces a final response. Here’s how it works:

1. **Agent Setup**: You define an agent with instructions and connect it to an MCP server that provides tools and context.
2. **User Input**: When you give the agent an input (e.g., “What’s the weather in Paris?”), the SDK sends it to the LLM via MCP.
3. **Context and Tools**: MCP supplies the LLM with the conversation history and a list of available tools (e.g., `get_weather`).
4. **Tool Call Decision**: The LLM decides whether to respond with text or call a tool. If it chooses a tool, MCP ensures the call is formatted correctly.
5. **Execution**: The SDK executes the tool (via the MCP server or locally) and returns the result to the LLM.
6. **Response**: The LLM uses the tool’s result to generate a final answer, and the loop ends.

### Example:

```python
from openai_agents import Agent, Runner
from openai_agents.models import LitellmModel

# Define a tool (this could be hosted on an MCP server)
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny, 20°C."

# Create an agent connected to an MCP server
weather_agent = Agent(
    name="WeatherBot",
    instructions="Answer weather-related questions using tools from the MCP server.",
    model=LitellmModel(model="openai/gpt-4o", api_key="YOUR_API_KEY"),
    tools=[get_weather]  # Tools could come from an MCP server
)

# Run the agent
runner = Runner()
response = runner.run(weather_agent, "What's the weather in Paris?")
print(response)  # Output: The weather in Paris is sunny, 20°C.
````

In this example, MCP ensures the `get_weather` tool is properly described to the LLM and that the tool call (with “Paris” as input) is valid before execution.

## MCP Servers

An MCP server is a service that hosts tools and context for agents to use. Instead of defining tools directly in your code, you can connect your agent to an MCP server, which provides a library of pre-built tools (e.g., for weather, math, or API calls). This is especially useful for:

* **Reusability**: Multiple agents can use the same tools without duplicating code.
* **Scalability**: Large projects can rely on MCP servers to manage complex toolsets.
* **Community Tools**: Some MCP servers are community-driven, offering a wide range of tools for different tasks.

The OpenAI Agents SDK supports connecting to MCP servers, allowing your agents to access a diverse set of tools without needing to implement each one locally.
**Example**: You might connect to an MCP server that provides a `search_web` tool. Your agent could use it to answer questions like “What’s trending today?” without you writing the search logic yourself.

## Tips for Using MCP

* **Start Simple**: Begin with a single tool and a local setup to understand how MCP formats tool calls.
* **Use Schemas**: Define tool inputs with Pydantic schemas to ensure the LLM sends valid data.
* **Explore MCP Servers**: Experiment with public or community MCP servers to access pre-built tools.
* **Check Tracing**: Use the SDK’s tracing feature to debug how MCP handles tool calls and context.
* **Secure API Keys**: If connecting to an MCP server, store API keys securely (e.g., in environment variables).

## Why MCP Matters

MCP makes the OpenAI Agents SDK more powerful by standardizing how agents interact with tools and context. It simplifies development, improves safety, and enables you to tap into a growing ecosystem of tools via MCP servers. Whether you’re building a simple weather bot or a complex multi-agent system, MCP helps your agents work smarter and more reliably.

