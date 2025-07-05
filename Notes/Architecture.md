
# What is the OpenAI Agents SDK?

The OpenAI Agents SDK is a helpful toolset that lets you build smart AI agents. These agents are programs powered by Large Language Models (LLMs)—special computer programs trained on lots of text to understand and respond like humans. The SDK provides an easy way to create agents that can use tools, pass tasks to others, and follow safety rules, all controlled by a central process called the Agent Loop. OpenAI released it after the success of ChatGPT, which first appeared on November 30, 2022, and added a big feature called tool calling on June 13, 2023. In simple terms, it turns an LLM into a doer by connecting it to outside systems, APIs, and functions, making it great for tasks like answering questions or managing jobs.


## Key Concepts

### How the SDK Works

The SDK organizes everything into layers that team up to handle your requests and give responses. Here’s the basic flow:

- **User Input**: You ask the agent a question or give it a task.  
- **Agent Loop**: The main engine decides what to do—use a tool, pass the task, or reply.  
- **Memory Layer**: Keeps track of past chats to help the agent remember.  
- **LLM**: The brain that thinks, but it forgets unless reminded.  
- **Output**: The agent gives you an answer, like text or an action.

---

## Main Parts

- **Memory Layer**: Stores and recalls the agent’s memory.  
- **Agent Loop**: Manages all actions.  
- **Chat Completions / Response API**: Shapes chat responses.  
- **REST API Layer**: Links to outside services.  
- **LLM**: The thinking part, stateless by nature.

![architecture!](/public/architecture.jpeg "Open Ai Agents SDK Architecture")
---

## What’s Special

- Builds on ChatGPT’s launch and tool calling feature.  
- Turns LLMs into actionable helpers.  
- Uses layers to connect and manage tasks.

---

## Details with Examples

### The Memory Layer

**What It Does**:

- Holds conversation history, user details, or learned info.  
- Sends this memory to the Agent Loop to keep the agent on track.  
- Can connect to storage systems (like databases) for long-term memory.

**Why It Matters**:

Without memory, the LLM would forget everything after one question. This layer helps it remember short-term things or plan for deeper learning (called RSI: Reasoning, Storage, Interaction).

**Example**: If you ask, “What did I say earlier?”, the Memory Layer provides the past chat so the agent can answer.

---

### The Agent Loop (OpenAI Agents SDK)

**What It Does**:

- Runs a cycle of thinking, acting, and checking until the task is done.  
- Manages tool calling (using functions like get_weather), handoffs (passing tasks), and guardrails (safety checks).

**Key Features**:

- **Tool Calling**: Lets the agent use outside tools.  
- **Handoffs**: Allows one agent to pass work to another, like a team leader to a specialist.  
- **Guardrails**: Keeps inputs and outputs safe.

**Example Code**:

```python
from openai_agents import Agent, Runner

def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny, 20°C."

weather_agent = Agent(
    name="WeatherBot",
    instructions="Answer weather questions.",
    tools=[get_weather]
)
runner = Runner()
response = runner.run(weather_agent, "What's the weather in Paris?")
print(response)  # Output: The weather in Paris is sunny, 20°C.
````

Here, the Agent Loop runs the get_weather tool and returns the result.

---

### Chat Completions / Response API

**What It Does**:

* Takes your question and instructions to make a prompt for the LLM.
* Turns the LLM’s output into a clear response (text, audio, etc.).
* Supports tool calling, a key feature since June 13, 2023, for agents like GPT-4.

**Why It Matters**:

Before tool calling, LLMs only made text. Now, they can act, thanks to this layer’s use in tools like LangChain.

**Example**: You say, “Tell me the weather.” It becomes a tool call, and the API turns the result into “The weather is sunny.”

---

### REST API Layer

**What It Does**:

* Acts as a bridge for the agent to talk to outside services or databases.
* Sends requests (like tool calls) and gets data back.

**Why It Matters**:

Makes the agent flexible, letting it use web services beyond the LLM.

**Example**: The agent uses REST API to get real-time weather data from a service.

---

### LLM (Stateless)

**What It Does**:

* Processes inputs (like prompts or tool results) with deep learning (transformers).
* Creates outputs (text or tool calls) based on what it’s given.

**Why It Matters**:

It forgets past chats unless the Memory Layer or prompts remind it. The SDK sends session data each time to help.

**Example**: Without a prompt, it forgets your last question unless the Memory Layer steps in.

---

## Types of Messages in the Chat API

**What They Are**:

* **System Prompt**: Sets the agent’s behavior (e.g., “Be polite”).
* **User Prompt**: Your question (e.g., “What’s the weather?”).
* **Tool Message**: Data from a tool (e.g., “sunny, 20°C”).
* **AI Assistant Message**: The agent’s final reply.

**Example**: A system prompt says, “Be a weather expert,” and a user prompt asks, “What’s the forecast?” The tool message helps build the reply.

---

## Memory Behavior in OpenAI Agents SDK

**What It Does**:

* Sets instructions once but resends them with the full session each time you use `Runner.run`.
* Simulates short-term memory since the LLM doesn’t remember on its own.

**How It Works**:

* Uses system prompts or tool schemas to take notes.
* Needs external memory for longer context.

**Example**: If you say, “Continue from before,” the SDK sends past chats to keep the flow.

---

## Long-Term Memory in Agents SDK

**What It Is**:

The SDK doesn’t have built-in long-term memory.

**Solutions**:

* **LangGraph**: For complex memory patterns.
* **RAG (Retrieval-Augmented Generation)**: Fetches past data.
* **Langmen** (likely a typo for LangChain): Manages memory.

**Example**: Use RAG to recall a chat from weeks ago.

---

## Long-Running Workflows in Agents SDK

**What It Is**:

The SDK doesn’t support long tasks by itself.

**Solutions**:

* **AWS Step Functions**: Manages multi-step processes.
* **LangGraph Flows**: Handles complex tasks.
* **AWS Long-Running Containers**: Runs extended jobs.
* **Docker Containers**: Uses isolated setups.
* **Temporal.ai**: Keeps tasks running.

**Example**: Use AWS Step Functions for a multi-day project task.

---

## What’s Missing?

* Long Running Workflows: Tasks lasting hours or days.
* Memory: Beyond short-term needs.
* State Serving: Tracking agent state across sessions.
* Agent Serving: Scaling for many users.
* These need external tools to fix.

---

# APIs Explained

* **REST API**: A messenger letting the agent talk to outside services (e.g., weather apps) with requests and responses.
* **ChatCompletion API**: A chat helper that turns your question into a smart reply using the LLM.
* **Responses API**: A formatter that turns raw data into clear answers.
* **Assistant API**: A customizable helper you control with instructions and tools.

**Examples**:

* REST API fetches weather: “Sunny, 20°C.”
* ChatCompletion API replies: “2 + 2 is 4.”
* Responses API formats: “Weather in Paris is 20°C.”
* Assistant API solves: “3 + 5 = 8” with a math tool.

---

## Quick Takeaways

* The OpenAI Agents SDK builds smart agents from LLMs, using ChatGPT’s foundation and tool calling.
* Layers like Memory, Agent Loop, and APIs (REST, ChatCompletion, Responses, Assistant) work together to process and respond.
* The Memory Layer and Agent Loop manage memory and tasks, while the LLM needs help to remember.
* Use external tools (LangGraph, AWS) for long-term memory or workflows.
* Start small, add safety with guardrails, and debug with tracing to master the SDK.
* It’s a flexible base for creating interactive AI, enhanced by APIs and external integrations.
