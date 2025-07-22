# *Table of Content*

- [History of AI](#history-of-ai)
- [Types of AI](#types-of-ai)
- [What is Anthropic?](#what-is-anthropic)
- [What is the OpenAI Agents SDK?](#what-is-the-openai-agents-sdk)
- [Built in Agent Loop](#built-in-agent-loop)
- [What is an LLM?](#what-is-an-llm)
- [History of AI](#history-of-ai)
- [History of AI](#history-of-ai)
- [History of AI](#history-of-ai)
- [History of AI](#history-of-ai)
- [History of AI](#history-of-ai)
- [History of AI](#history-of-ai)

# History of AI

## 🧠 **Waves of AI Evolution**

*From Rules ➝ Learning ➝ Creating ➝ Acting in the Real World*

---

### **1. Symbolic AI (1950s–1980s)** – 🧱 *The Rule-Based Thinkers*

This was the **first generation** of AI. It followed **fixed rules** written by humans—like “if X happens, then do Y.” It didn’t learn from experience or data.

> 🧾 **Example**: Early chess programs that followed hard-coded rules to make moves.

📌 *Good at solving logic puzzles but failed in real-life messy situations like language or vision.*

---

### **2. Machine Learning (1980s–2010s)** – 📊 *The Pattern Learners*

Instead of rules, this AI learns by **looking at data**. It finds patterns using math and statistics. The more data it sees, the smarter it gets.

> 📩 **Example**: A spam filter that learns to detect junk emails by analyzing thousands of real messages.

📌 *It learns from data but still struggles with tasks that need deep understanding.*

---

### **3. Deep Learning (2010s–Present)** – 🧠 *The Data Cravers*

A powerful type of Machine Learning that uses **deep (multi-layered) neural networks**. It can understand **images, audio, and text** by training on huge amounts of data.

> 📷 **Example**: Face recognition on phones, voice assistants like Alexa or Google Assistant.

📌 *Deep Learning made modern AI like computer vision and speech recognition possible.*

---

### **4. Generative AI (2022–Present)** – ✨ *The Content Creators*

This AI doesn’t just analyze data—it **creates new content** like text, code, music, and images based on user prompts. It doesn't think or plan; it just responds creatively.

> ✍️ **Example**: ChatGPT (writes text), DALL·E (makes images), GitHub Copilot (writes code).

📌 *It’s great at helping with writing, creativity, and idea generation.*

---

### **5. Agentic AI (Emerging)** – 🎯 *The Goal Achievers*

Agentic AI goes beyond just giving responses. It can **make decisions, plan tasks, use tools**, and even **act independently** to reach a goal without needing constant input.

> 🧠 **Example**: An AI that can plan a trip—search flights, compare prices, and book tickets on its own.

📌 *This is where AI starts behaving like a real assistant—not just a chatbot.*

---

### **6. Robotic / Physical AI (Future)** – 🤖 *The Real-World Actors*

This is where **AI meets the physical world**. It combines thinking (Agentic AI) with doing (robots). These AIs can **move, see, pick up objects, and take real-world actions.**

> 🤖 **Example**: Self-driving cars, warehouse robots, or humanoid robots that assist in hospitals or homes.

📌 *Still developing, but already being tested in cars, drones, and factories.*

---

## 🪜 **Quick Recap Table**

| Stage                | What It Does                          | Real Example                     |
| -------------------- | ------------------------------------- | -------------------------------- |
| **Symbolic AI**      | Follows rules (no learning)           | Rule-based chess programs        |
| **Machine Learning** | Learns from data                      | Email spam filters               |
| **Deep Learning**    | Understands text, speech, images      | Face unlock, Siri, Alexa         |
| **Generative AI**    | Creates content from prompts          | ChatGPT, DALL·E, Copilot         |
| **Agentic AI**       | Plans and acts on goals independently | AI that books your flight        |
| **Robotic AI**       | Acts in real world using a body       | Self-driving cars, delivery bots |

---

# Types of AI
 
1. ANI
2. AGI
3. ASI

**Artificial Narrow Intelligence (ANI)** is AI that can do one specific task really well, like voice recognition or translating languages.
It’s smart **only in that one thing**—can’t think or work outside its skill.

> 🎯 Example: Siri or Alexa can set reminders, but can’t write a novel or design a robot.

---

**Artificial General Intelligence (AGI)** is a **theoretical AI** that can think and learn like a human.
It would understand anything, solve many kinds of problems, and even be creative—**but it doesn’t exist yet.**

> 🧠 Example: An AGI could write stories, solve science problems, and hold deep conversations—all in one system.

---

**Artificial Superintelligence (ASI)** would be **smarter than humans** in every way—logic, creativity, emotions, etc.
It’s a **future idea** and comes with big ethical questions (e.g., how to control it, risks to humans).

> 🌍 Example: An ASI could cure diseases or design clean energy—but also might be hard to manage or stop.

---

> ✅ **Key Add-On**: Right now, we only have **ANI** (narrow AI). AGI and ASI are still in the research/future phase.

---

## 🧩 **AGI Levels** (From Chatbots to AI Organizations)

**Level 1 – Chatbots**
These are basic AI systems that can chat or answer questions, but **can’t plan or take actions.**
They reply using pre-learned info—no real "thinking" involved.

> 💬 Example: A website chatbot that helps with FAQs.

---

**Level 2 – Reasoners**
These can **think and solve problems** like puzzles or logical tasks, but still don’t act on their own.

> 🧮 Example: An AI that solves math problems or creates a step-by-step project plan.

---

**Level 3 – Agents**
These are more advanced—they **plan, make decisions, and take actions** using tools like APIs or web browsers.

> ✈️ Example: An AI that books a flight on your behalf—searches sites, compares prices, and pays.

---

**Level 4 – Innovators**
These AIs go beyond tasks. They show **creativity and original thinking**—they might invent, design, or discover.

> 💡 Example: An AI that creates a new drug formula or writes a unique music style.

---

**Level 5 – Organizations**
This is the highest level: **Multiple AIs working together** like a team or company to run big, complex systems.

> 🏭 Example: An AI team that handles everything in a factory—from product design to delivery—without humans.


### What are AI Agents?

**AI agents** are smart software programs that act on their own to get things done for you. You give them a goal, and they figure out the steps to achieve it.

* **Example**: If you tell an AI agent to "plan my trip," it will automatically find flights, book hotels, and set up calendar reminders without you needing to guide each step. They often use large language models (LLMs) to understand your request and can use various tools (like booking websites) to complete their tasks.

---

### Key AI Concepts: How They Differ

Here’s a simple breakdown of how AI agents compare to other common AI terms.

#### **AI Agent vs. Agentic AI**
* An **AI Agent** is a single program focused on one type of job (e.g., a chatbot that only answers questions).
* **Agentic AI** is a bigger system where *multiple agents work together* on a complex goal. Think of it as a team of specialized agents managed by a larger system. For instance, one agent handles emails while another manages the calendar, and the agentic system coordinates them to onboard a new employee.

#### **Generative AI vs. Agentic AI**
* **Generative AI** (like ChatGPT) *creates content* based on your prompts. It reacts to what you ask. For example, you ask it to write an email, and it writes one.
* **Agentic AI** is proactive and *takes action*. It doesn't just create; it *does*. Instead of just writing an email, an agentic system could be given a goal like "improve customer satisfaction" and would then analyze data, plan steps, and execute tasks on its own to achieve it.

#### **AI Chatbot vs. AI Agent**
* An **AI Chatbot** is designed for conversation. It answers your questions or follows simple commands within a chat.
* An **AI Agent** is an action-taker. It can go beyond conversation to perform tasks in the real world, like accessing your calendar, sending emails, and booking appointments automatically. A chatbot talks; an agent acts.

#### **General vs. Specialized Agents**
* A **General Agent** is a jack-of-all-trades. It can handle a wide variety of tasks, like helping with research, scheduling, and general questions.
* A **Specialized Agent** is an expert in one specific area. For example, a specialized agent might be an expert at finding the cheapest flights using reward points, while a general agent would handle the entire vacation plan (flights, hotel, and activities).

---

### The Future of Agentic AI 🚀

Agentic AI is set to become a major technology. Experts believe **2025 will be the "year of the agent,"** as most developers are already building them.

Soon, businesses will use agentic systems to automate routine work like IT support and employee onboarding, freeing up people to focus on more creative and strategic tasks. We can expect to see teams of specialized agents working together seamlessly to solve complex problems.

---
## What is Anthropic?

**Anthropic** is an AI research company, founded by former OpenAI researchers, that is best known for creating the **Claude** series of language models. The company's primary focus is on developing AI that is **safe, interpretable, and aligned with human values**.

***

### Agents vs. Workflows: Building Smart Systems

Anthropic provides a framework for building AI systems that can perform tasks, distinguishing between two main approaches: **agents** and **workflows**. Both fall under the umbrella of "agentic systems," but they operate differently.

* **Agents**: An **agent** is an autonomous system that can think for itself. It decides which tools to use and what steps to take to complete a goal. This makes agents flexible and powerful for complex tasks, but also less predictable.
* **Workflows**: A **workflow** follows a pre-defined sequence of steps, much like a recipe. An LLM in a workflow is guided along a fixed path, making the process predictable and consistent.

The general advice is to start with the simplest solution. If a task requires consistency and has clear steps, a **workflow** is best. If it requires flexibility and autonomous decision-making for a complex goal, an **agent** is the better choice. Keep in mind that agentic systems might be slower and more expensive but often achieve better results on difficult tasks.

***

### Anthropic’s Five Design Patterns for Agentic Systems

Anthropic has outlined five key design patterns to build effective and sophisticated agentic systems. These patterns can be implemented using various development frameworks.

1.  **Prompt Chaining (Chain Workflow)** ⛓️
    This pattern breaks a large task into smaller, sequential steps. The output of one step becomes the input for the next, creating a logical chain of actions.

2.  **Routing** Routing involves directing a task to the most suitable tool or agent. A central router agent assesses the task and passes it to the specialized agent best equipped to handle it.

3.  **Parallelization** 
    To increase efficiency, this pattern executes multiple sub-tasks at the same time. This is ideal for tasks that can be broken down into independent parts.

4.  **Orchestrator-Workers** 
    In this model, a central **"orchestrator"** agent breaks down a complex goal into smaller sub-tasks and assigns them to specialized **"worker"** agents. The orchestrator manages the overall process and coordinates the workers.

5.  **Evaluator-Optimizer** 🔎
    This pattern creates a feedback loop for continuous improvement. An **"evaluator"** agent assesses the performance of other agents and provides feedback, while an **"optimizer"** agent uses that feedback to improve the process.

---

# What is the OpenAI Agents SDK?

The **OpenAI Agents SDK** is an open-source Python library designed to help you build smart **AI agents**. These are programs powered by Large Language Models (LLMs) that can understand instructions, make decisions, and perform tasks autonomously. The SDK is designed to be lightweight, simple, and ready for real-world use.

A key feature is that it automatically handles the complex **"agent loop"**—the cycle of thinking, acting, and observing—so you can focus on defining your agent's goals and capabilities. It simplifies connecting agents to external **tools** (like APIs or custom functions) and enables multiple agents to collaborate and hand off tasks to one another. First released in early 2025, it builds upon the success of features like **tool calling**, which OpenAI introduced on June 13, 2023, turning models like ChatGPT into active "doers" rather than just responders.

-----

### Core Features

  * **Python-First Design**: Built to be intuitive for Python developers, using familiar coding structures.
  * **Automated Agent Loop**: Manages the core logic of an agent's operation, including conversation history and tool use.
  * **Tool Integration**: Easily connect your agent to external systems and APIs by turning any Python function into a tool.
  * **Multi-Agent Workflows**: Allows specialized agents to work together and delegate tasks.
  * **Tracing & Debugging**: Includes built-in tools to help you visualize and fix your agent's behavior.

-----

### Installation

You can install the SDK using pip:

```bash
pip install openai-agents
```

Or, if you use the `uv` package manager:

```bash
uv add openai-agents
```
## History of OpenAI Agent SDK

The **OpenAI Agent SDK**, also known as the **Responsive API**, is the latest iteration in OpenAI's journey to create advanced AI helpers. Its development has been a gradual process:

* It began with the **Assistant API**, a fundamental tool for creating AI assistants.
* Next came **Swarm**, an early open-source framework designed for coordinating multiple agents, focusing on lightweight agent handoffs and messaging.
* The **OpenAI Agent SDK** (Responsive API) emerged as the production-ready successor to Swarm, building upon its concepts for real-world applications and offering more advanced capabilities.

**Future Outlook**: It's anticipated that the Agent SDK might eventually merge with the Assistant API, leading to even more powerful and integrated AI solutions.

## Why Use the OpenAI Agents SDK?
The SDK is perfect for beginners and developers wanting a simple, official OpenAI-supported framework. Compared to alternatives:

- **OpenAI Agents SDK:** Lightweight, easy to learn with three core ideas (Agents, Handoffs, Guardrails), great for quick starts, reliable production apps, and debugging with tracing.
- **LangChain/LangGraph:** General tools for LLM apps; LangGraph is strong for complex workflows but harder to learn.
- **CrewAI:** Intuitive for role-based agent teams but less flexible.
- **AutoGen:** Flexible for multi-agent chats but has a steeper learning curve.

![Why use OpenAi Agents SDK!](/public/why_OpenAiAgentSDK.PNG "Why use OpenAi Agents SDK")

It’s ideal for building and debugging agent systems fast due to its simplicity and Python-first design.
The OpenAI Agent SDK is favored for its **simplicity** ("few primitives, but enough"), **customizability** (allowing source code modification), and **Python-first design**, making it accessible to a wide developer base.

# Built in Agent Loop

The **Agent Loop** is the core mechanism of the OpenAI Agent SDK, automating how an AI agent processes tasks. It saves developers time by handling the continuous interaction needed for an agent to reach a solution.

Here's how it works:
1.  **Input to LLM**: The agent's instructions and conversation history are sent to its Large Language Model (LLM).
2.  **LLM's Response**: The LLM analyzes the input and decides its next step:
    * **Final Output**: If the LLM produces a complete answer, the loop ends, and the result is returned.
    * **Handoff**: If the LLM determines another agent is better suited for the task, it "hands off" the task, switching to the new agent and restarting the loop.
    * **Tool Call**: If the LLM needs to perform an action (e.g., fetch data), it calls a designated tool. The SDK executes the tool, adds the results to the conversation, and the loop restarts.
3.  **Iteration**: This process repeats until a final answer is achieved.

**Safety Feature**: To prevent endless loops, the built-in agent loop has a `max_turns` limit (defaulting to 10). If this limit is exceeded, a `MaxTurnsExceeded` error is raised.

**Example**: If you ask, "What's the weather in Paris?", the LLM might call a `get_weather('Paris')` tool. The SDK runs this, gets "sunny, 20°C," and the LLM then provides the final answer: "The weather in Paris is sunny, 20°C."

## OpenAI Agent SDK Core Principles
The SDK’s design focuses on:

- **Agents:** LLM-driven assistants with a name, instructions, and optional tools that process input into text or tool calls.
- **Handoffs:** One agent passes tasks to another with specialized skills, chaining agents in workflows.
- **Guardrails:** Checks (using Pydantic schemas) ensure inputs and outputs are valid and safe.
- **Agent Loop:** An automatic cycle driving the agent’s operation.
- **Function Tools:** Python functions agents can call to perform tasks.
- **Tracing:** Logs every step (LLM calls, tool usage, handoffs) for debugging and visualization.

These let you build complex systems without redoing orchestration logic.



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

---
# What is an LLM?
A Large Language Model (LLM) is the “brain” of an AI agent. It’s an advanced AI trained on massive amounts of text (like thousands of books and websites) to understand and generate human-like language. Examples include OpenAI’s GPT-4o, Google’s Gemini, Anthropic’s Claude, Bard (Google), Llama (Meta), and Bing Chat. LLMs use deep neural networks (called transformers) to predict and create text based on patterns they’ve learned. For agents, the LLM processes your input, decides what to say, or picks tools to use.

- Large Language Models (LLMs) processing natural language to generate responses or trigger tools. However, LLMs are inherently **stateless**, meaning they don't remember past conversations.

**Example:** If you ask, “What’s the weather in Paris?”, the LLM might reply with text or call a weather tool.


### LLM Limitations & Agent SDK Solutions

The OpenAI Agent SDK addresses these limitations:

* **Short-Term Memory**: The SDK simulates short-term memory by resending the entire session history (instructions, chat, tool results) with each `Runner.run` call.
* **Long-Term Memory**: For persistent memory beyond a single session, external tools are required. Solutions include:
    * **LangMem**: Specifically designed for long-term memory in AI agents, enabling them to learn and adapt across interactions.
    * **RAG (Retrieval-Augmented Generation)**: Fetches relevant information from external data sources (e.g., databases, documents) to augment the LLM's knowledge.
    * **LangGraph**: Can manage complex memory patterns within multi-step workflows.
* **Long-Running Workflows**: The SDK alone doesn't support tasks spanning hours or days. External orchestration tools are needed, such as:
    * **AWS Step Functions**: For managing multi-step processes.
    * **LangGraph Flows**: For complex, cyclical workflows.
    * **AWS Long-Running Containers / Docker Containers**: For running extended jobs in isolated environments.
    * **Temporal.ai**: For robustly executing and tracking long-running tasks.
* **No Direct Actions**: LLMs only generate text. The SDK's **Tool Calling** feature (since June 2023) transforms these text outputs into real-world actions (e.g., calling APIs).
* **No Built-in Human-in-the-Loop (HITL)**: The SDK lacks native features for human approval or intervention. This can be added manually using tools like Dapr or LangGraph for workflow control, or by customizing `tool_use_behavior`.

In essence, while LLMs provide the intelligence, the OpenAI Agent SDK, augmented with external tools, provides the necessary **memory, action capabilities, and workflow management** to build robust and reliable AI agents.

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
# Tool Calling 

**Tool Calling**, introduced by OpenAI in June 2023, empowers LLMs to perform actions, transforming them into "agentic AI." This involves an LLM calling a tool, receiving its output, and using it to formulate a response.

The OpenAI Agent SDK provides three types of tools:
* **Function Tool**: Convert any Python function into a tool using `@function_tool`.
* **Hosted Tools**: Pre-built OpenAI tools like web search or file search.
* **Agents as Tool**: Use one agent as a callable tool for another.

Tools can be enhanced with external functionalities such as:
* **MCP (Model Context Protocol)**: A standard for connecting LLMs to external systems (e.g., web search, databases).
* **Custom Functions, FastAPI, Databases, Custom APIs**: Integrate your own code or services.

The workflow is simple: a user query triggers the LLM to identify and call a relevant tool, which executes and returns a result that the LLM then uses to respond.

### Orchestrator Agent (In Agent as Tool)

The orchestrator agent is like a team leader. It supervises sub-agents, collects their responses after they finish their work, and then sends the final answer to the user.

### Using an Orchestrator Agent

Imagine you ask, “Plan my day.” The orchestrator agent assigns tasks to sub-agents (e.g., a “Schedule Agent” and a “Reminder Agent”), collects their answers, and gives you a full plan.


## The Big Picture: From APIs to Agents

Two years ago, we mostly used APIs—specific commands to get data from services. Now, the vision has changed: everything can be an AI agent. With an agent, you can talk naturally, like saying, “Turn off all lights at home.” The agent will call the right API routes and send “turn off” commands to control physical devices through the Internet of Things (IoT), which connects everyday devices to the internet.

- **APIs**: You learn endpoints (addresses) and mechanisms to get data, needing coding skills.  
- **AI Agents**: You use natural language, and the agent understands and acts without you writing code.

---

### What is an Agent?

An agent is like a human with a brain (LLM), a role (instructions or personality), and tools (like hands or eyes to do tasks). It’s simply a call to an LLM that can work with other agents to get the best result. The OpenAI Agent SDK is very simple and easy to learn, using only a few basic ideas (called abstractions) and three main building blocks (primitives), which are enough to do a lot.

---

## Details with Examples

### How Agents Work with Different Systems

Agents can connect to physical devices via IoT. For example, if you say, “Turn off all lights,” the agent calls API routes for each light and passes “turn off” parameters, turning them all off automatically.

---

# Handoffs (The Delegator)

Handoffs let agents pass tasks to other agents in a multi-agent system, like a team working together.

- **What It Does**: Helps with multi-agent workflows by letting one agent give work to another based on their skills or abilities.
- **Triage Agent**: A triage agent is a special kind of agent that is connected to expert agents from different fields. Its job is to analyze the user’s question and decide which expert agent should handle the task.

When a task is handed off, the entire conversation history is sent along so the receiving expert agent understands the context.

After the handoff, the expert agent (not the triage agent) is the one that responds to the user.
- **Example**: If you ask, “Fix my car,” the triage agent sends it to a “Mechanic Agent.” You give the past chat history, and the Mechanic Agent takes over to answer.
- **Inside Handoff**: It can also involve tool calling (you can see this in tracing logs, which track what happens).

---

# Guardrails (The Safety Guard)

Guardrails are like security guards that check what goes into and comes out of the agent to keep things safe and under control.

- **General Idea**: They enable input and output data validation, restricting what the agent accepts or says. This saves money on input tokens (pieces of text the LLM processes) and ensures safe conversations.

### Input Guardrails

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

# Tracing or Observability (The Built-in Tracker)

Tracing is a feature that automatically logs what the agent does on the OpenAI platform, helping you watch, save, and fix problems.

- **What It Does**: By default, it logs tracing on the OpenAI platform. You can track tool calls, handoffs, and workflows. It helps identify errors (debugging), visualize how the agent works, and fine-tune the model.
- **How to Use**: Run `enable_verbose_stdout_logging()` in the command prompt to see tracing details. You can also use third-party tools like Agents Ops or Langtrace for extra help.

# OpenAI Agents SDK Architecture

## How the SDK Works

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


## APIs Key Points

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

# Context Management 

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

## Benefits of Context

* **Dynamic Instructions:** A function sets unique instructions per user (e.g., “Help Ubaid with his question”).
* **Memory Management:** Adds short-term (current chat), long-term (past chats), episodic (events), semantic (facts), and procedural (steps) memory.
* **Structured Output:** Pydantic or dataclass ensures organized data, enabling UI connections (e.g., apps displaying agent responses).

## Context Window Details

* **Token Limit:** ChatGPT 4.1’s 1 million token limit means it can handle large inputs, but output is typically smaller.
* **Tokenizer:** Converts text into tokens; use an OpenAI tokenizer to count them.

# Lifecycle Events (Hooks)

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

## RunHooks Methods

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

## AgentHooks Methods

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
---
## OpenAI Agent SDK: Quick Takeaways

The **OpenAI Agent SDK** is a user-friendly, Python-first tool for building intelligent AI agents powered by Large Language Models (LLMs). It simplifies the creation of autonomous systems that can handle complex and flexible tasks, making it a more accessible alternative to frameworks like LangChain or CrewAI.

**Core Concepts:**

* **Agents vs. Workflows:** Agents are autonomous and adaptable for flexible tasks, while workflows follow pre-set steps for predictable, routine jobs. Choose based on task needs: workflows for consistency, agents for adaptability.
* **LLMs as the Brain:** LLMs are the agent's "brain," providing natural language understanding and generation. However, they require the SDK to enable actions, memory, and reasoning.
* **Key Principles:** The SDK operates on core principles:
    * **Agents:** Autonomous entities with a brain (LLM), a defined role (instructions), and tools.
    * **Handoffs:** Agents can pass tasks to other specialized agents (e.g., a triage agent handing off to a mechanic agent) for efficient multi-agent workflows.
    * **Guardrails:** Safety mechanisms that check inputs (e.g., blocking abuse) and outputs (e.g., preventing politically charged responses), ensuring cost efficiency and safety.
    * **Tracing:** Built-in logging and support for third-party tools to monitor and debug agent behavior.
    * **Function Tools:** Enable agents to perform actions by calling external functions or APIs.
* **Tooling:**
    * **Tool Calling:** Since June 2023, LLMs can take actions using a two-turn workflow.
    * **Tool Types:** The SDK supports function tools (`@function_tool`), hosted tools, and even agents as tools, all managed by an orchestrator agent. These tools can be enhanced with APIs or databases.
* **Agent Loop & Memory:**
    * The SDK includes a built-in **agent loop** that automates task handling, typically limited to 10 turns to prevent endless cycles.
    * The **Memory Layer** helps agents process and respond, but LLMs often need external tools (like LangGraph or AWS) for long-term memory management or complex workflows.
* **Context Management:**
    * **Local Context:** Safely manages sensitive runtime information locally using `RunContextWrapper`.
    * **LLM Context:** Sends data to the LLM via prompts or tools.
    * Context can be added using dataclass, Pydantic, or any Python object for dynamic instructions and memory types.
    * **Run Context:** Tracks usage and provides data to your code, not the LLM.
    * **Context Window:** Limits input size (e.g., 1 million tokens for ChatGPT 4.1).
* **Lifecycle Events (Hooks):** Checkpoints where you can control or observe an agent's work.
    * **Agent Hooks:** Focus on a single agent's start, end, handoffs, and tool use.
    * **Runner Hooks:** Monitor the overall process.
    * Custom classes inheriting from `AgentHook` or `RunnerHook` can override methods like `on_start` or `on_handoff`.
    * **Prefetching:** Prepare data before events to ensure readiness.

**Advantages & Best Practices:**

* **Ease of Use:** Simpler to use than other frameworks, with built-in debugging and production readiness.
* **Quick Setup:** Use UV and virtual environments for fast, isolated setups.
* **Enhanced LLM Access:** Integrate with OpenRouter (unified API) or LiteLLM (flexible models) for multiple LLMs, including Gemini via compatibility.
* **Interactive Interfaces:** Chainlit can be used to add interactive interfaces.
* **Iterative Development:** Start small, use tracing for debugging, and gradually enhance with external tools for memory or complex workflows.
* **Robust Design:** Anthropic's five design patterns offer structured methods for building robust agentic systems.

For more information, refer to the [OpenAI Agents SDK Official Documentation](https://openai.github.io/openai-agents-python/).