# What Are Lifecycle Events in OpenAI Agents SDK?

Lifecycle Events in OpenAI Agents SDK are like special checkpoints in an agent’s life where you can step in and do something useful. These are called “hooks” and help you control or watch what happens when an agent works. There are two types: Agent Hooks (for a single agent) and Runner Hooks (for the whole process). Think of them as moments where you can prepare, check, or change things, just like preparing for a big event in real life. The SDK lets you customize these hooks to make your agent smarter and safer.

## Key Concepts

### What Are Hooks?

- Hooks are specific times during an agent’s work where you can add your own actions, like preparing data or checking results.
- Agent Hooks focus on events for one agent (e.g., when it starts or uses a tool).
- Runner Hooks cover events for the entire agent process (e.g., when tasks are handed off).
- How It Starts: You prepare information ahead of time (prefetching) and use a main class (like AgentHooks) to set up these actions.

### How Hooks Work

- You create a custom class and connect it to AgentHook or RunnerHook (this is called inheriting).
- Inside this class, you can change or add your own steps by overriding methods (e.g., on_agent_start).
- Like Human Life: A person’s life has stages (birth, school, marriage, sleep, death) with actions like waking up or running. Similarly, agents have hooks like on_start or on_tool_end to mark their stages.

### Main Classes for Hooks

- **RunHooks**: A class that catches events during an agent’s run, using any context type (e.g., user data).
- **AgentHooks**: A class for events specific to one agent, set with `agent.hooks` to track its actions.

## Details with Examples

### How to Use Hooks

**Step 1:** Make a custom class and inherit from `AgentHook` or `RunnerHook`.  
**Step 2:** Override the methods you want to customize with your own actions.  
**Prefetching:** Gather information before an event happens to be ready.

### RunHooks Methods

- **on_agent_start:** Happens before the agent starts working, every time it changes.  
  **Takes:** context (your data wrapper), agent (the agent).  
  **Example Use:** Print a welcome message.

- **on_agent_end:** Happens when the agent finishes with a final answer.  
  **Takes:** context, agent, output (the result).  
  **Example Use:** Save the final output.

- **on_handoff:** Happens when one agent passes the task to another.  
  **Takes:** context, from_agent (the giver), to_agent (the receiver).  
  **Example Use:** Log the handoff.

- **on_tool_start:** Happens before a tool is used.  
  **Takes:** context, agent, tool (the tool being called).  
  **Example Use:** Prepare data for the tool.

- **on_tool_end:** Happens after a tool finishes.  
  **Takes:** context, agent, tool, result (the tool’s output).  
  **Example Use:** Check the tool’s result.

### AgentHooks Methods

- **on_start:** Happens before this agent starts, every time it’s chosen.  
  **Takes:** context, agent.  
  **Example Use:** Set up the agent’s settings.

- **on_end:** Happens when this agent finishes with a final answer.  
  **Takes:** context, agent, output.  
  **Example Use:** Clean up after the agent.

- **on_handoff:** Happens when this agent receives a task from another.  
  **Takes:** context, agent, source (the agent giving the task).  
  **Example Use:** Welcome the new task.

- **on_tool_start:** Happens before this agent uses a tool.  
  **Takes:** context, agent, tool.  
  **Example Use:** Notify that a tool is starting.

- **on_tool_end:** Happens after this agent’s tool finishes.  
  **Takes:** context, agent, tool, result.  
  **Example Use:** Record the tool’s success.

---

### Example: Custom Agent Hooks

```python
from dataclasses import dataclass
from agents import Agent, AgentHooks, RunContextWrapper, Runner, function_tool

@dataclass
class UserInfo:
    name: str

class MyAgentHooks(AgentHooks[UserInfo]):
    async def on_start(self, context: RunContextWrapper[UserInfo], agent: Agent[UserInfo]) -> None:
        print(f"Agent {agent.name} is starting for {context.context.name}!")

    async def on_end(self, context: RunContextWrapper[UserInfo], agent: Agent[UserInfo], output: Any) -> None:
        print(f"Agent {agent.name} finished with: {output}")

@function_tool
async def say_hello(wrapper: RunContextWrapper[UserInfo]) -> str:
    return f"Hello, {wrapper.context.name}!"

async def main():
    user_info = UserInfo(name="Ayesha")
    agent = Agent[UserInfo](name="HelloBot", tools=[say_hello], hooks=MyAgentHooks())
    result = await Runner.run(agent, "Say hello", context=user_info)
    print(result.final_output)  # Output: Hello, Ayesha!
    # Prints: Agent HelloBot is starting for Ayesha! ... Agent HelloBot finished with: Hello, Ayesha!
````

---

### Example: Custom Runner Hooks

```python
from dataclasses import dataclass
from agents import Agent, RunHooks, RunContextWrapper, Runner, function_tool

@dataclass
class UserInfo:
    name: str

class MyRunHooks(RunHooks[UserInfo]):
    async def on_handoff(self, context: RunContextWrapper[UserInfo], from_agent: Agent[UserInfo], to_agent: Agent[UserInfo]) -> None:
        print(f"Task handed from {from_agent.name} to {to_agent.name} for {context.context.name}")

@function_tool
async def say_hello(wrapper: RunContextWrapper[UserInfo]) -> str:
    return f"Hello, {wrapper.context.name}!"

async def main():
    user_info = UserInfo(name="Zain")
    agent1 = Agent[UserInfo](name="StartBot", tools=[say_hello])
    agent2 = Agent[UserInfo](name="EndBot", tools=[say_hello])
    runner = Runner(hooks=MyRunHooks())
    result = await runner.run(agent1, "Say hello", context=user_info, handoff_to=agent2)
    print(result.final_output)  # Output: Hello, Zain!
    # Prints: Task handed from StartBot to EndBot for Zain
```

---

## Quick Takeaways

* Lifecycle Events (Hooks) are checkpoints where you can control or watch an agent’s work, with Agent Hooks for one agent and Runner Hooks for the process.
* **How to Use:** Create a custom class, inherit from `AgentHook` or `RunnerHook`, and override methods like `on_start` or `on_handoff`.
* **Prefetching:** Prepare data before events to stay ready.
* `RunHooks` tracks events like agent start, end, handoffs, and tool use across the run.
* `AgentHooks` focuses on a single agent’s start, end, handoffs, and tool use.
* Start with simple hooks to monitor, then add custom actions to make your agent work better.
