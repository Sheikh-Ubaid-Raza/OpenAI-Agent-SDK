# What is the OpenAI Agents SDK?
The OpenAI Agents SDK is an open-source Python library that helps you build smart AI agents—programs powered by Large Language Models (LLMs) that understand instructions, make decisions, and perform tasks. It’s designed to be simple, lightweight, and ready for real-world use, letting you create multi-agent workflows with minimal code. The SDK handles the tricky “agent loop” (thinking, acting, and observing) automatically, so you can focus on what your agent should do. It’s Python-first, meaning it’s built for Python lovers, and includes tools for tracing and debugging to make development easier.

You can install it with:  
`pip install openai-agents`

Or, if using UV (a fast Python tool by Astral):  
`uv add openai-agents`

With just a few lines of Python, you can create an agent to answer questions or use tools (like fetching weather data), and the SDK manages conversation history and tool connections for you.

## Key Concepts

### What is an LLM?
A Large Language Model (LLM) is the “brain” of an AI agent. It’s an advanced AI trained on massive amounts of text (like thousands of books and websites) to understand and generate human-like language. Examples include OpenAI’s GPT-4o, Google’s Gemini, Anthropic’s Claude, Bard (Google), Llama (Meta), and Bing Chat. LLMs use deep neural networks (called transformers) to predict and create text based on patterns they’ve learned. For agents, the LLM processes your input, decides what to say, or picks tools to use.

**Example:** If you ask, “What’s the weather in Paris?”, the LLM might reply with text or call a weather tool.

### Limitations of LLMs
LLMs are powerful but have limits:

- **No Actions:** They only generate text and can’t interact with the world (e.g., call APIs or update data). The SDK turns their output into actions.
- **No Memory:** They are stateless, forgetting past chats unless you provide conversation history.
- **Hallucinations:** They can give confident but wrong answers (e.g., making up facts).
- **Prompt Sensitivity:** Small changes in wording can lead to different results, affecting reliability.
- **No True Reasoning:** They mimic understanding but don’t think like humans.

The SDK addresses these with tools, memory management, and validation to make agents reliable.

## Why Use the OpenAI Agents SDK?
The SDK is perfect for beginners and developers wanting a simple, official OpenAI-supported framework. Compared to alternatives:

- **OpenAI Agents SDK:** Lightweight, easy to learn with three core ideas (Agents, Handoffs, Guardrails), great for quick starts, reliable production apps, and debugging with tracing.
- **LangChain/LangGraph:** General tools for LLM apps; LangGraph is strong for complex workflows but harder to learn.
- **CrewAI:** Intuitive for role-based agent teams but less flexible.
- **AutoGen:** Flexible for multi-agent chats but has a steeper learning curve.

![Why use OpenAi Agents SDK!](/public/why_OpenAiAgentSDK.PNG "Why use OpenAi Agents SDK")

It’s ideal for building and debugging agent systems fast due to its simplicity and Python-first design.

## OpenAI Agent SDK Core Principles
The SDK’s design focuses on:

- **Agents:** LLM-driven assistants with a name, instructions, and optional tools that process input into text or tool calls.
- **Handoffs:** One agent passes tasks to another with specialized skills, chaining agents in workflows.
- **Guardrails:** Checks (using Pydantic schemas) ensure inputs and outputs are valid and safe.
- **Agent Loop:** An automatic cycle driving the agent’s operation.
- **Function Tools:** Python functions agents can call to perform tasks.
- **Tracing:** Logs every step (LLM calls, tool usage, handoffs) for debugging and visualization.

These let you build complex systems without redoing orchestration logic.

## Swarm and Evolution
Swarm was OpenAI’s earlier open-source framework for multi-agent coordination, aimed at teaching lightweight agent handoffs and messaging. The Agents SDK is its production-ready successor, building on Swarm’s ideas for real-world use.

## Details with Examples

### The Agent Loop Explained
The agent loop is the SDK’s core cycle. When you run `Runner.run(agent, input)`, it:

- **Sends Input to LLM:** Sends the agent’s instructions and chat history to the LLM.
- **Receives Response:** The LLM returns text, a tool call, or a handoff.
- **Processes Actions:**
  - If a tool call, the SDK runs the function and adds the result.
  - If a handoff, it switches to the new agent.
- **Checks for Completion:** Ends if the response is a final answer (no more tools/handoffs).
- **Repeats:** Loops back if more actions are needed.

**Example:**

Input: “What’s the weather in Paris?”  
Loop: LLM says “Call get_weather('Paris')” → SDK runs it, gets “sunny, 20°C” → LLM says “The weather in Paris is sunny, 20°C” → Loop ends.

### Getting Started Example

Here’s a simple script:

```python
from agents import Agent, Runner

# Define a tool
def get_weather(city: str) -> str:
    # Placeholder: Real apps call an API
    return f"The weather in {city} is sunny, 20°C."

# Create an agent
weather_agent = Agent(
    name="WeatherBot",
    instructions="Answer weather-related questions for users.",
    tools=[get_weather]
)

# Run the agent
response = Runner.run(weather_agent, "What's the weather in Paris?")
print(response.final_output)  # Output: The weather in Paris is sunny, 20°C.
````

### Tools and Function Calling

A tool is a Python function an agent calls to interact with the world (e.g., fetching data). Function calling lets the LLM request a tool with a structured output like:

```json
{ "name": "get_weather", "arguments": { "city": "London" } }
```

The `@function_tool` decorator simplifies this:

* Shows the tool to the LLM.
* Parses the request.
* Runs the function.
* Returns the result.

**Example:**

```python
from agents import function_tool

@function_tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny, 20°C."
```

This turns agents into action-takers.

## UV for Project Setup

UV is a fast, Rust-based tool for Python projects, ideal for the SDK. It speeds up package installs and virtual environments.

### Why Use UV?

* **Speed:** Faster than pip and venv.
* **Simplicity:** Eases dependency management.
* **Best Practice:** Ensures isolated, clean setups.

### Setup Instructions

**Simple Project (Without Package Structure):**

```bash
uv init my_project
cd my_project
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv add openai openai-agents chainlit
code .
uv run chainlit run app.py  # replace app.py with your file
```

**Structured Project (With Package Structure):**

```bash
uv init --package my_project
cd my_project
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv add openai openai-agents chainlit
code .
uv run chainlit run my_project/app.py
```

Note: Adjust the path to `app.py` if it’s elsewhere.

## Virtual Environments & Their Benefits

A virtual environment is an isolated Python setup for each project, with its own interpreter and libraries.

### Benefits:

* **Avoids Conflicts:** Different projects can use different package versions (e.g., openai==0.28.0 vs. openai==1.3.0).
* **Reproducibility:** Share a `requirements.txt` for others to recreate your setup.
* **Clean System:** Keeps global Python uncluttered.
* **No Permission Issues:** No need for sudo installs.

**Example:** Without a virtual environment, a global openai-agents install might break another project; with `uv venv`, each stays separate.

## OpenRouter

[OpenRouter](https://openrouter.ai/) is a third-party service with a single API to access over 100 LLMs (e.g., OpenAI’s GPT, Google’s Gemini, Anthropic’s Claude) using one API key.

### Why Use It?

* **Unified Access:** Swap models (e.g., model="openai/gpt-4" or model="google/gemini-1.5") without code changes.
* **Cost Savings:** Often cheaper than direct providers.
* **Reliability:** Fallbacks keep your app running.

**Example:** Configure the SDK to use OpenRouter’s endpoint for transparent LLM switches.

## LiteLLM

LiteLLM is an open-source library to call over 100 LLMs with one syntax, requiring your own API keys.

### Why Use It?

* **Flexibility:** Supports many models, including open-source ones.
* **Free:** No service fees (you pay providers).
* **Integration:** Install with `pip install openai-agents[litellm]`.

**Example:**

```python
from agents import Agent, Runner
from agents.extensions.models.litellm_model import LitellmModel

gemini_agent = Agent(
    name="GeminiBot",
    instructions="Answer questions using Gemini.",
    model=LitellmModel(
        model="google/gemini-2.0-flash",
        api_key="YOUR_GOOGLE_API_KEY"
    )
)

response = Runner.run_sync(gemini_agent, "Who is the founder of Pakistan?")
```

This lets your agent use Google’s Gemini.

## OpenRouter vs. LiteLLM

| Feature   | OpenRouter                      | LiteLLM                    |
| --------- | ------------------------------- | -------------------------- |
| Type      | Paid, hosted service            | Free, open-source library  |
| Setup     | One API key for all             | Separate keys per provider |
| Ideal For | Simplified billing, reliability | Flexibility, cost savings  |

Choose **OpenRouter** for convenience; **LiteLLM** for flexibility.

## Using Google Gemini with the Agents SDK

The SDK is model-agnostic, supporting Google’s Gemini via LiteLLM or OpenAI-compatible endpoints. Example: Use `LitellmModel(model="google/gemini-2.0-flash", api_key=...)`. Google also offers an OpenAI-compatible API for Gemini, allowing `OpenAIChatCompletionsModel` with proper setup.

## Chainlit

Chainlit is an open-source Python framework for building interactive web interfaces for LLM or agent apps.

### Why Use It?

* **Chat Interfaces:** Turns agents into user-friendly chatbots.
* **Debugging:** Visualizes reasoning, tool calls, and handoffs.
* **Rapid Prototyping:** Builds demos fast.
* **Features:** Includes authentication and conversation history.

**Example:**

```bash
uv add chainlit
uv run chainlit run app.py
```

This launches a web app to interact with your agent and see its steps.

## Quick Takeaways

* The OpenAI Agents SDK is a simple, Python-first tool to build LLM-powered agents, handling the agent loop and multi-agent workflows.
* An LLM is the agent’s brain, trained on vast text, but limited by no actions, memory, or reasoning—addressed by the SDK.
* Core Principles include Agents, Handoffs, Guardrails, and Tracing, with Function Tools for actions.
* **Why Choose It?** It’s easier than LangChain, CrewAI, or AutoGen, with built-in debugging and production readiness.
* Use UV and virtual environments for fast, isolated setups; enhance with OpenRouter (unified API) or LiteLLM (flexible models) for multiple LLMs.
* Chainlit adds interactive interfaces, and the SDK supports Gemini via compatibility.
* Start small, use tracing to debug, and grow with external tools for memory or workflows.

