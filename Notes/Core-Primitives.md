
# What is the OpenAI Agent SDK?

The OpenAI Agent SDK is a free, open-source Python library that helps you create smart AI agents. These agents are like helpful assistants powered by a Large Language Model (LLM), which is a program trained on huge amounts of text to understand and generate human-like responses. The SDK makes it easy to build agents that can work together, share tasks, and follow safety rules. It handles the complicated parts—like calling the LLM and managing tasks—automatically, so you can focus on telling the agent what to do. It’s designed to be lightweight (not heavy on your computer) and uses Python, with built-in tools to track and fix problems.

You can install it with a simple command:
```
pip install openai-agents
```

Or, if you use UV (a faster tool for managing Python projects), you can install it with:
```
uv add openai-agents
````

---

## Key Concepts

### The Big Picture: From APIs to Agents

Two years ago, we mostly used APIs—specific commands to get data from services. Now, the vision has changed: everything can be an AI agent. With an agent, you can talk naturally, like saying, “Turn off all lights at home.” The agent will call the right API routes and send “turn off” commands to control physical devices through the Internet of Things (IoT), which connects everyday devices to the internet.

- **APIs**: You learn endpoints (addresses) and mechanisms to get data, needing coding skills.  
- **AI Agents**: You use natural language, and the agent understands and acts without you writing code.

---

### History of OpenAI Agent SDK

The OpenAI Agent SDK didn’t appear overnight—it evolved step by step:

- It started with the Assistant API, a basic tool to create helpers.
- Then came Swarm, an early version to coordinate multiple agents.
- Now, we have the OpenAI Agent SDK (also called Responsive API), which is more advanced.
- **Prediction**: In the future, it might combine the Assistant API and Responsive API for even better performance.

---

### What is an Agent?

An agent is like a human with a brain (LLM), a role (instructions or personality), and tools (like hands or eyes to do tasks). It’s simply a call to an LLM that can work with other agents to get the best result. The OpenAI Agent SDK is very simple and easy to learn, using only a few basic ideas (called abstractions) and three main building blocks (primitives), which are enough to do a lot.

---

## Details with Examples

### How Agents Work with Different Systems

Agents can connect to physical devices via IoT. For example, if you say, “Turn off all lights,” the agent calls API routes for each light and passes “turn off” parameters, turning them all off automatically.

---

### Handoffs (The Delegator)

Handoffs let agents pass tasks to other agents in a multi-agent system, like a team working together.

- **What It Does**: Helps with multi-agent workflows by letting one agent give work to another based on their skills or abilities.
- **Triage Agent**: A triage agent is a special kind of agent that is connected to expert agents from different fields. Its job is to analyze the user’s question and decide which expert agent should handle the task.

When a task is handed off, the entire conversation history is sent along so the receiving expert agent understands the context.

After the handoff, the expert agent (not the triage agent) is the one that responds to the user.
- **Example**: If you ask, “Fix my car,” the triage agent sends it to a “Mechanic Agent.” You give the past chat history, and the Mechanic Agent takes over to answer.
- **Inside Handoff**: It can also involve tool calling (you can see this in tracing logs, which track what happens).

---

### Guardrails (The Safety Guard)

Guardrails are like security guards that check what goes into and comes out of the agent to keep things safe and under control.

- **General Idea**: They enable input and output data validation, restricting what the agent accepts or says. This saves money on input tokens (pieces of text the LLM processes) and ensures safe conversations.

#### Input Guardrails

- **Checks the user’s input first.**  
- If someone uses bad language (e.g., abuse), it triggers a “tripwire” (sets `tripwire_triggered = True`) to stop the process for that question. Other questions work normally.
- **How It Works**: When a user inputs something, it goes to both the agent and the input guardrail function at the same time. The input guardrail function runs first and decides if it’s okay. It’s applied to the first agent with `@input_guardrails`.

#### Output Guardrails

- **Checks the final answer.**  
- For example, it can stop the agent from talking about politics.
- **How It Works**: It’s like the input guardrail but applied to the last agent where the response comes from, using `@output_guardrails`.

#### Multiple Agents

- If you have many agents, the input guardrail checks the first agent once.  
- Then, after any handoffs, the output guardrail checks the last agent that gives the final answer.
- **Example**: If a user says, “Insult me,” the input guardrail stops it. If the agent tries to discuss politics, the output guardrail blocks that too.

---

### Tracing or Observability (The Built-in Tracker)

Tracing is a feature that automatically logs what the agent does on the OpenAI platform, helping you watch, save, and fix problems.

- **What It Does**: By default, it logs tracing on the OpenAI platform. You can track tool calls, handoffs, and workflows. It helps identify errors (debugging), visualize how the agent works, and fine-tune the model.
- **How to Use**: Run `enable_verbose_stdout_logging()` in the command prompt to see tracing details. You can also use third-party tools like Agents Ops or Langtrace for extra help.


#### Example Code:
```python
from agents import Agent, Runner, function_tool, enable_verbose_stdout_logging

enable_verbose_stdout_logging()  # For tracing

@function_tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Define a simple agent
agent = Agent(
    name="GreetBot",
    instructions="Greet users politely.",
    tools=[greet]
)

response = Runner.run_sync(agent, "What’s my greeting?")
print(response.final_output)  # Output: Hello, [your name]! (with tracing logs showing each step)
````

Here, tracing logs show the tool call to greet and the response process.

---

## Quick Takeaways

* The OpenAI Agent SDK is a simple Python tool to build smart AI agents using LLMs, evolving from APIs to natural language control.
* Agents are like humans with a brain (LLM), role (instructions), and tools, working better together with handoffs (e.g., triage agent picking a Mechanic Agent).
* Guardrails keep things safe by checking inputs (e.g., blocking abuse) and outputs (e.g., no politics), saving costs and ensuring safety.
* Tracing helps you watch and fix what the agent does with built-in logs and third-party tools.
* You can start easily, connect to IoT devices, and grow with more agents and tools for future use!


- **Resource**: Check [Open AI Agents SDK Official Documentation](https://openai.github.io/openai-agents-python/) for more information.

