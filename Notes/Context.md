
# What is Context Management in OpenAI Agents SDK?

Context Management in OpenAI Agents SDK is a way to handle information an agent needs while working. This can include user details, memory, or tools, helping the agent understand and respond better. The SDK manages this context in two main ways: locally (kept on your server) and for the LLM (sent to the language model). Sensitive data stays safe on your local server, and you can add dynamic instructions or memories. It’s all controlled by you, making it flexible and secure.

## Key Concepts

### What is Context?

- Context means any information an agent needs at runtime, like user names or task details.
- It’s not given directly to the agent; it’s managed on your local server, allowing safe use of sensitive data (e.g., personal info).
- Context helps add dynamic instructions, memory (short-term, long-term, episodic, semantic, procedural), and structured outputs.

### Types of Context Management

- **Local Context:** Information stays with your server or agent loop and isn’t shared with the LLM, keeping sensitive data secure.
- **Agent/LLM Context:** Information sent to the LLM to help it respond, visible in the conversation history.

### Ways to Add Context

- **Data Class, Pydantic Object, or Class with Attributes:** Use any Python object (e.g., dataclass or Pydantic) to hold context.
- **Dynamic Instructions:** A function with context and agent as parameters sets instructions based on user data.
- **Memory Types:** Includes short-term (recent chats), long-term (past interactions), episodic (specific events), semantic (facts), and procedural (how-to knowledge).
- **Structured Output:** Using Pydantic or dataclass to get organized data, connecting different UIs to the agent.

## Run Context

### What It Is

Run context is the information and details about an agent’s work during a single run, wrapped in a special tool called `RunContextWrapper`.

### Purpose

It helps you track what’s happening (like usage) and share data with your code (e.g., tools or callbacks) without sending it to the LLM.

### Key Point

This context stays local and isn’t seen by the LLM, keeping your data safe.

## RunContextWrapper Dataclass

### What It Is

A special Python tool (dataclass) that wraps the context you give to `Runner.run()`. It’s like a box that holds your context and some extra info about the agent’s run.

### Based On

Uses `Generic[TContext]`, meaning it can work with any context type you choose (e.g., dataclass or Pydantic).

### Source

Found in `src/agents/run_context.py`.

### Note

This tool doesn’t send data to the LLM; it’s for your code (like tool functions, callbacks, or hooks).

## Context Window and Token Limit

- **Context Window:** Made up of system prompt, user prompt, and input text/list; limits how much the LLM can process (e.g., ChatGPT 4.1 has a 1 million token limit).
- **Token:** A piece of a sentence; text is split into tokens for AI processing. You can check token count with an OpenAI tokenizer.
- **Note:** Input context is usually larger than output context.

## Details with Examples

### How Context is Managed

#### Local Context

- Represented by `RunContextWrapper` class with a `context` property.
- You create a Python object (e.g., dataclass or Pydantic) and pass it to `Runner.run(..., context=your_object)`.
- Available to tool calls, lifecycle hooks, etc., but not sent to the LLM.

**Example: Store user info locally:**

```python
from dataclasses import dataclass
from agents import Agent, RunContextWrapper, Runner, function_tool

@dataclass
class UserInfo:
    name: str
    uid: int

@function_tool
async def fetch_user_age(wrapper: RunContextWrapper[UserInfo]) -> str:
    return f"The user {wrapper.context.name} is 47 years old"

async def main():
    user_info = UserInfo(name="John", uid=123)
    agent = Agent[UserInfo](name="Assistant", tools=[fetch_user_age])
    result = await Runner.run(agent, "What is the age of the user?", context=user_info)
    print(result.final_output)  # Output: The user John is 47 years old
````

* **Uses:** Contextual data (e.g., username/UID), dependencies (e.g., loggers), helper functions.
* **Important:** All agents, tools, and hooks in a run must use the same context type.

#### Agent/LLM Context

* Sent to the LLM via conversation history.

**Ways to Send:**

* **System Prompt (Dynamic):** Add instructions (static or via a function using context).
  Example: `f"The user name is {context.context.name}, help them with their question"`.
* **User Prompt:** Include in the input when calling `Runner.run`.
* **Tool Message:** Extract data from external APIs when the LLM calls a tool.
* **Retrieval/Web Search:** Fetch data from files, databases, or the web to ground responses.

**Example: Dynamic instruction for user “Ubaid”:**
Instruction: `f"The user name is Ubaid, help them with their question"`.

## RunContextWrapper Details

### Attributes

* **context: TContext:** The object you passed to `Runner.run()` (or `None` if not provided). It holds your custom data, like a user’s name.
* **usage: Usage:** Tracks how much the agent has used so far (e.g., tokens or time). For streamed responses (data sent in parts), this info updates only after the last part is done.

### How It Works

When you run an agent, `RunContextWrapper` wraps your context object and adds usage details, available to your tools or hooks.

**Example: Using context and usage:**

```python
from dataclasses import dataclass
from agents import Agent, RunContextWrapper, Runner, function_tool

@dataclass
class UserInfo:
    name: str

@function_tool
async def greet_user(wrapper: RunContextWrapper[UserInfo]) -> str:
    return f"Hello, {wrapper.context.name}! Usage so far: {wrapper.usage}"

async def main():
    user_info = UserInfo(name="Ali")
    agent = Agent[UserInfo](name="GreetBot", tools=[greet_user])
    result = await Runner.run(agent, "Say hello", context=user_info)
    print(result.final_output)  # Output: Hello, Ali! Usage so far: [usage details]
```

**Note:** Usage might be incomplete during streaming until the end.

## Benefits of Context

* **Dynamic Instructions:** A function sets unique instructions per user (e.g., “Help Ubaid with his question”).
* **Memory Management:** Adds short-term (current chat), long-term (past chats), episodic (events), semantic (facts), and procedural (steps) memory.
* **Structured Output:** Pydantic or dataclass ensures organized data, enabling UI connections (e.g., apps displaying agent responses).

## Context Window Details

* **Token Limit:** ChatGPT 4.1’s 1 million token limit means it can handle large inputs, but output is typically smaller.
* **Tokenizer:** Converts text into tokens; use an OpenAI tokenizer to count them.

## Quick Takeaways

* Context Management lets agents use runtime information safely, managed locally on your server.
* Local Context keeps sensitive data secure with `RunContextWrapper`, while LLM Context sends data to the LLM via prompts or tools.
* Add Context with dataclass, Pydantic, or any Python object, enabling dynamic instructions and memory types.
* Run Context with `RunContextWrapper` tracks usage and provides data to your code (not the LLM), using context and usage.
* Structured Output via Pydantic connects UIs to agents.
* Context Window limits input (e.g., 1 million tokens in ChatGPT 4.1), with tokens as text pieces.
* Start with local context for safety, use dynamic prompts for flexibility, and check token limits for efficiency.
