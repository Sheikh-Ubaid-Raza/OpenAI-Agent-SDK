# 🤖 AI Agents and OpenAI Agents SDK Notes

## 🔍 What are AI Agents?

AI agents are autonomous software programs that observe environments, make decisions, and execute tasks to achieve goals.  
**Example:** A travel agent autonomously searches flights, books hotels, and sets reminders for a trip based on “plan a vacation.”

---

## 🧠 AI Agents vs. Agentic AI

- **AI Agent**: A single autonomous program with a specific role (e.g., chatbot, email scheduler).  
- **Agentic AI**: A multi-agent system where agents collaborate on complex goals.  
**Example:** An agentic AI for employee onboarding uses one agent to route emails and another to schedule training.

---

## 🧬 Agentic AI vs. Generative AI

- **Generative AI**: Reactive, creates content (e.g., ChatGPT writing an essay).  
- **Agentic AI**: Proactive, plans and executes tasks.  
**Example:** Generative AI writes a report; Agentic AI analyzes customer data and initiates actions to improve satisfaction.

---

## 💬 AI Agents vs. AI Chatbots/Models

- **Chatbot/Model**: Conversational, responds to queries without autonomous actions.  
- **AI Agent**: Plans and executes tasks using tools.  
**Example:** A chatbot answers questions; an agent books meetings by checking calendars and sending invites.

---

## 🧩 General Agent vs. Specialized Agent

- **General Agent**: Handles a broad range of tasks with flexible capabilities (e.g., a virtual assistant managing emails, schedules, and research).  
- **Specialized Agent**: Designed for specific tasks with deep expertise (e.g., a weather agent that only fetches and processes weather data).  
**Example:** A general agent plans a trip (flights, hotels, itinerary); a specialized agent only books flights.

---

## 🔮 Future of Agentic AI

Agentic AI is expected to grow significantly, with 2025 seen as the “year of the agent” (99% of developers exploring agents).  
It will automate workflows (e.g., IT provisioning) and enable domain-specific agent teams, freeing humans for creative tasks.

---

## 🐝 Swarm

**Swarm** was OpenAI’s open-source framework for multi-agent coordination, now replaced by the production-ready **OpenAI Agents SDK**.

---

## 🧰 OpenAI Agents SDK

The **OpenAI Agents SDK** is an open-source Python library for building agentic AI applications, simplifying agent creation and orchestration.

**Installation:**
```bash
pip install openai-agents
````

**Features:** Lightweight, Pythonic, with built-in tracing and debugging.
**Example:** Create an agent to handle weather queries, with the SDK managing history and tool calls.

---

## ❓ Why OpenAI Agents SDK?

The SDK is simpler than LangChain, LangGraph, Crew AI, or AutoGen, with three core primitives and robust tracing.

* **LangChain / LangGraph**: General-purpose, strong state management
* **Crew AI**: Role-based, less scalable
* **AutoGen**: Flexible, steeper learning curve

**Advantage**: Official OpenAI support, beginner-friendly, reliable.

---

## 🧱 SDK Core Principles

* **Agents**: LLM-driven assistants with instructions and tools
* **Handoffs**: Task delegation between agents
* **Guardrails**: Input/output validations (e.g., Pydantic schemas)
* **Agent Loop**: Automated LLM calls, tool execution, and handoffs
* **Function Tools**: Python functions as tools
* **Tracing**: Logs reasoning and tool usage
* **Observability**: Monitors and visualizes workflows

---

## 🔁 Agent Loop

Drives agent operation:

1. Call LLM with instructions and history
2. Process response (text, tool calls, handoff)
3. If final output, stop; if handoff, switch agents; if tool call, execute and loop

**Example:**
For “What’s the weather in Paris?”, the agent calls `get_weather("Paris")`, gets “sunny,” and outputs the result.

---

## 🧠 What is an LLM?

**LLMs (Large Language Models)** are AI models trained on vast text to understand and generate language, powering agent reasoning.
**Examples:** ChatGPT, Gemini, Claude.

---

## ⚙️ UV for Project Setup

**UV** is a fast Python dependency manager.

**Setup:**

```bash
pip install uv            # Initialize UV
uv venv                   # Create virtual environment
source .venv/bin/activate # Activate it
pip install openai openai-agents  # Install dependencies
```

**Benefit:** Ensures isolated, clean project environments.

---

## 🧪 Virtual Environments

Virtual environments isolate Python dependencies per project, preventing conflicts and enabling reproducible setups.

**Benefits:** Avoids version clashes, simplifies collaboration, eliminates permission issues.

---

## 🔗 OpenRouter

**OpenRouter** provides a unified API for multiple LLMs (OpenAI, Gemini, Claude).

**Advantage:** Swap models without code changes, better pricing, redundancy.
**Use:** Configure SDK to use OpenRouter’s endpoint for flexible LLM access.

---

## 🌐 LiteLLM

**LiteLLM** is an open-source library supporting 100+ LLMs via a common interface.

**Use:**

```bash
pip install openai-agents[litellm]
```

**Configuration:**

```python
LitellmModel(model="google/gemini-2.5", api_key="...")
```

**Benefit:** Enables non-OpenAI models in the SDK.

---

## 🆚 OpenRouter vs. LiteLLM

* **OpenRouter**: Hosted API gateway, unified billing, paid
* **LiteLLM**: Client library, free, requires provider keys
  **Use Case:** OpenRouter for simplicity; LiteLLM for flexibility

---

## 💬 Chainlit

**Chainlit** is an open-source Python framework for building conversational AI interfaces.

**Use:** Create chat UIs or dashboards for agent systems, visualizing reasoning and handoffs.

---

## 🤝 Using Google Gemini with Agents SDK

Configure Gemini via LiteLLM:

```python
LitellmModel(model="google/gemini-2.0-flash", api_key="...")
```

**Note:** Gemini supports OpenAI-compatible endpoints.

---

## 🛠️ Tools in Agents SDK

Tools enable agents to act beyond text.

* **Hosted Tools**: OpenAI-provided (e.g., web search, code execution)
* **Function Tools**: Python functions as tools

**Example:**

```python
@function_tool
def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny."
```

**Agents as Tools:** One agent can call another.

---

## 🧾 Function Calling

Function calling lets agents invoke tools via JSON outputs.

* **Why:** Enables actionable tasks (e.g., calling a weather API)
* **Benefit:** Automates operations with machine-readable schemas

---

## 📚 Resources

* **Official Documentation:** [OpenAI Agents SDK Docs](https://openai.github.io/openai-agents-python/)
* **Panaversity Repo:** [Learn Agentic AI](https://github.com/panaversity/learn-agentic-ai/tree/main/01_ai_agents_first)

