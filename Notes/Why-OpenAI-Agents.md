
# What is the OpenAI Agent SDK?

The OpenAI Agent SDK is a free, open-source Python tool that lets you build smart AI agents. These agents are like helpers powered by a Large Language Model (LLM), which is a program trained on tons of text to understand and create human-like answers. The SDK is popular because it’s quick to learn, uses simple building blocks (called primitives), and lets you customize or edit its source code to fit your needs. It saves you time by handling the hard work, like managing tasks and connecting to tools.

You can start using it by installing it with:
```
pip install openai-agents
````

---

## Key Concepts

### Why Use the OpenAI Agent SDK?

![Why use OpenAi Agents SDK!](/public/why_OpenAiAgentSDK.PNG "Why use OpenAi Agents SDK")

The OpenAI Agent SDK stands out for a few reasons:

- **Few Primitives, But Enough**: It uses a small set of simple ideas that are powerful and easy to learn.  
- **Customizable**: You can change its source code to add your own features.  
- **Python First**: Python is a popular and easy programming language loved worldwide, making the SDK a favorite among developers.

---

### Tool/Function Calling

Tool calling (or function calling) is a key feature released by OpenAI in June 2023. It turns regular AI that generates text (generative AI) into action-taking AI (agentic AI).

- **Why It’s Powerful**: Before tool calling, LLMs could only create content. Now, with tools, agents can take actions like turning on a light or fetching data.  
- **How It Works**: The LLM calls a tool, gets the result, and uses it to respond.

---
## What is the Role of LLM in Agents?

A Large Language Model (LLM) is the brain of an AI agent in the OpenAI Agent SDK. It’s a smart program trained on tons of text to understand natural language prompts (sentences with meaning) and give helpful answers. Agents need LLMs because they can process what you say and decide how to respond, making them act like assistants. The LLM helps turn your words into actions, especially with tools, and is key to building agents that feel natural to use.

---

## Key Concepts

### Why LLMs Are Needed

- LLMs understand the meaning behind your words and give smart replies.  
- They make agents work by processing requests and creating responses.

---

### Simple Workflow

- **Basic Flow**: You send a request → The LLM processes it → You get a response.  
- **Before Tool Calling**: LLMs only made text, like writing a story or answering a question.  
- **With Tool Calling**: It’s a two-step process:

  - User request → LLM calls a tool → Tool sends a message back to LLM → LLM responds to user. (takes 2 turns)

---

### LLM Behavior

- **Stateless Nature**: LLMs don’t remember past chats on their own. Each time you talk, it’s like starting fresh. In the OpenAI Agent SDK, we send the full session history (like past questions and tools) with every request to help it remember.

#### Short vs. Long-Term Memory:

- **Short-Term Memory**: The SDK can handle this during one chat, like remembering your name.  
- **Long-Term Memory**: The SDK doesn’t have this built-in. You need external tools:

  - **Langmem**: Remembers user data or past chats.  
  - **RAG (Retrieval-Augmented Generation)**: Pulls data from documents or databases.

#### Long-Running Tasks:

For tasks that take time, use:

- **AWS Step Functions**: Manages multi-step processes.  
- **AWS Long-Running Containers**: Runs tasks over time.  
- **LangGraph**: Handles complex workflows.  
- **Temporal**: Keeps tasks running smoothly.

---

### Human in the Loop (HITL)

The SDK lacks a feature where a human can step in to approve or guide the AI. You can add this manually with:

- **Dapr**: A tool for connecting services.  
- **LangGraph**: For workflow control.  
- **tool_use_behavior**: A built-in SDK feature to customize how tools are used.

---

### Messages and Inputs

#### Four Types of Messages:

- **System Prompt**: Tells the LLM how to act (e.g., “Be a friendly helper”).  
- **User Message**: What you ask or say to the agent.  
- **Tool Message**: The result from a tool the LLM used.  
- **AI Message**: The LLM’s reply back to you.

#### Inputs to LLM:

The LLM uses four things:

- **System Prompt (Instructions)**: Sets the LLM’s role and tone.  
- **User Prompt**: Your question or command.  
- **Tool Schema**: A description of the tools it can use.  
- **Tool Return Message**: The output from a tool.


#### LLM Outputs

#### Output Types:

- **Plain Text**: A simple chat reply, like “Hello!”  
- **Structured Output**: Organized data using tools like dataclass or Pydantic models.
- Tool Calls:

>- The tool’s name.  
>- The inputs (parameters) to use with the tool.

### Response Model vs. ChatCompletionsAIModel:

- **Response Model (Default)**: Used automatically, simple and good for most agents.  
- **ChatCompletionsAIModel**: Lets you use external LLMs (e.g., Gemini) via APIs, giving you more options to plug into the SDK.

---

### Extra Notes on LLM

- **Learning**: LLMs can improve by learning from what you do, like noting your name or role.  
- **Docstring Benefit**: Adding a docstring (a note in your code) to a function helps both developers and the LLM understand what the tool does.

---

## Types of Tools

The OpenAI Agent SDK offers three types of tools:

- **A) Function Tool**: Turn any Python function into a tool using the `@function_tool` decorator.  
- **B) Hosted Tools**: Pre-built tools like web search, file search, or computer tools.  
- **C) Agents as Tool**: Use an agent as a tool with the `.as_tool` method.

---

### Orchestrator Agent (In Agent as Tool)

The orchestrator agent is like a team leader. It supervises sub-agents, collects their responses after they finish their work, and then sends the final answer to the user.

---

### Adding Features to Tools

You can enhance tools with many things, like:

- **MCP**: A standard way to add external tools.  
- **Custom Functions**: Your own Python code.  
- **FastAPI**: A tool for building web apps.  
- **Database**: To store and retrieve data.  
- **Custom API**: Your own web services.

---

## Built-in Agent Loop

The built-in agent loop saves developers time by automatically managing tasks when you ask an agent to do something.

**Steps**:

1. Call the LLM for the current agent with the user’s input.  
2. The LLM produces an output:  
   a. **Final Output**: If the LLM gives a complete answer, the loop ends, and the result is returned.  
   b. **Handoff**: If the LLM passes the task to another agent, it updates the agent and input, then restarts the loop.  
   c. **Tool Calls**: If the LLM calls a tool, it runs the tool, adds the results, and restarts the loop.

- **Limit**: If the loop runs more than `max_turns` (default 10 times), it stops with a `MaxTurnsExceeded` error.

---

## Details with Example

### How Tool Calling Works

Before tool calling (June 2023), LLMs only made text. Now, they can act. Here’s the workflow:

>1. User says, “What’s the weather?”  
>2. LLM decides to call a `get_weather` tool.  
>3. The tool returns “Sunny, 20°C” to the LLM.  
>4. LLM responds, “The weather is sunny, 20°C.”

#### Example Code:

```python
from agents import Agent, Runner, function_tool

@function_tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny, 20°C."

agent = Agent(
    name="WeatherBot",
    instructions="Answer weather questions using tools.",
    tools=[get_weather]
)

response = Runner.run_sync(agent, "What’s the weather in Karachi?")
print(response.final_output)  # Output: The weather in [city] is sunny, 20°C.
````

**Note**: The LLM takes 2 turns—first to call the tool, then to respond with the result.

---

### Using an Orchestrator Agent

Imagine you ask, “Plan my day.” The orchestrator agent assigns tasks to sub-agents (e.g., a “Schedule Agent” and a “Reminder Agent”), collects their answers, and gives you a full plan.

---

### Adding MCP to Tools

**MCP (Model Context Protocol)** is a standard way to connect external tools. For example, you can add a web search tool via MCP to let the agent look up news.

---

## Quick Takeaways

* The OpenAI Agent SDK is a simple Python tool to build AI agents, loved for its ease, customization, and Python focus.
* Tool calling (since June 2023) turns LLMs into action-taking agents, using a 2-turn workflow.
* LLMs need natural language skills and can learn from notes or user actions, with inputs like system prompts and tool schemas.
* Tools come in three types: function tools (with `@function_tool`), hosted tools, and agents as tools, managed by an orchestrator agent.
* You can enhance tools with MCP, APIs, or databases.
* The built-in agent loop saves time by handling tasks automatically, with a limit of 10 turns to avoid endless loops.
