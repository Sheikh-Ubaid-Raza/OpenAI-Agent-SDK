# *Table of Content*

- **[Agent Class Notes](#agent-class-notes)**
- **[Runner Class Notes](#runner-class-notes)**
- [RunResultBase Class Notes](#runresultbase-class-notes)
- [RunResult Class Notes](#runresult-class-notes)
- [RunResultStreaming Class Notes](#runresultstreaming-class-notes)
- **[RunConfig Class Notes](#runconfig-class-notes)**
- [RunOptions Class Notes](#runoptions-class-notes)
- [AgentRunner Class Notes](#agentrunner-class-notes)
- [Baseclient Class Notes](#baseclient-class-notes)
- **[AsyncOpenAI Class Notes](#asyncopenai-class-notes)**
- [Model Class Notes](#model-class-notes)
- [ModelProvider Class Notes](#modelprovider-class-notes)
- **[OpenAiChatCompletionsModel Class Notes](#openaichatcompletionsmodel-class-notes)**
- [FunctionTool Class Notes](#functiontool-class-notes)
  - [function tool Decorator Notes](#function-tool-decorator)
- [InputGuardrail Class Notes](#inputguardrail-class-notes)
  - [input guardrail Decorator Notes](#input-guardrail-decorator)
- [OutputGuardrail Class Notes](#outputguardrail-class-notes)
  - [output guardrail Decorator Notes](#output-guardrail-decorator)


# Agent Class Notes

The **`Agent` class** is the fundamental component of the OpenAI Agents SDK. Think of it as creating a specialized **worker** designed to perform specific tasks. This is where you define the agent's core identity, including its purpose, skills, and limitations.

When you create an `Agent`, you equip it with:
* **Instructions**: The specific commands it should follow (e.g., "You are a helpful assistant that answers questions about the weather.").
* **Tools**: The functions or APIs it can use to perform actions (e.g., a function to get the current temperature).
* **Guardrails**: The rules it must obey to ensure it behaves safely and correctly.
* **Model Configuration**: The specific AI model it should use by default (e.g., `gpt-4o`).

While the `Agent` is the worker, it needs a **`Runner`** to act as its **manager**. The `Runner` takes the agent, gives it a task, and executes the job. An important feature is that the `Runner` can override some of the `Agent`'s default settings for a specific run, such as telling it to use a different AI model for a particular task. This makes the system both structured and flexible.

---

### **Attributes**

#### **1. name**
- **What it does**: Gives the agent a unique name to identify it.
- **Why it’s used**: Helps you know which agent is working, especially when you have many agents.
- **Simple Example**: If you name an agent “WeatherBot,” you can easily tell it’s the one handling weather questions.
- ```python
  name: str
  ```

#### **2. instructions**
- **What it does**: Tells the agent what to do, like a job description or rulebook.
- **Why it’s used**: Guides the agent’s behavior, like making it act like a teacher or a weather expert. Can be a fixed text or a function that changes based on the situation.
- **Simple Example**: Instructions like “Answer as a friendly teacher” make the agent explain things clearly.
- ```python
  instructions: (
      str
      | Callable[
          [RunContextWrapper[TContext], Agent[TContext]],
          MaybeAwaitable[str],
      ]
      | None
  ) = None
  ```

#### **3. prompt**
- **What it does**: Sets up dynamic instructions or tools for the agent, often used with OpenAI’s Responses API.
- **Why it’s used**: Lets you change the agent’s instructions or tools without editing code, making it flexible.
- **Simple Example**: A prompt might say, “Use a weather tool for weather questions,” so the agent knows what to do.
- ```python
  prompt: Prompt | DynamicPromptFunction | None = None
  ```

#### **4. handoff_description**
- **What it does**: Describes what the agent does, so other agents know when to pass tasks to it.
- **Why it’s used**: Helps agents decide who should handle a task, like passing a math question to a math expert.
- **Simple Example**: A description like “Handles weather queries” tells another agent to hand off weather-related tasks.
- ```python
  handoff_description: str | None = None
  ```

#### **5. handoffs**
- **What it does**: Lists other agents or handoff objects this agent can pass tasks to.
- **Why it’s used**: Lets the agent delegate tasks to specialists, keeping things organized.
- **Simple Example**: A general agent might pass a math question to a “MathAgent” listed here.
- ```python
  handoffs: list[Agent[Any] | Handoff[TContext]] = field(default_factory=list)
  ```

#### **6. model**
- **What it does**: Chooses the AI model the agent uses (e.g., “gpt-4o”).
- **Why it’s used**: Decides which AI brain powers the agent, but the `Runner` can override this.
- **Simple Example**: Setting `model="gpt-4o"` means the agent uses GPT-4o, unless the `Runner` picks something else.
- ```python
  model: str | Model | None = None
  ```

#### **7. model_settings**
- **What it does**: Fine-tunes how the AI model behaves, like making it more creative or precise.
- **Why it’s used**: Customizes the agent’s responses, like making them short or detailed.
- **Simple Example**: Setting a low “temperature” makes the agent’s answers more predictable.
- ```python
  model_settings: ModelSettings = field(default_factory=ModelSettings)
  ```

#### **8. tools**
- **What it does**: Lists tools the agent can use, like calculators or weather APIs.
- **Why it’s used**: Gives the agent extra abilities beyond just talking, like fetching data.
- **Simple Example**: A weather agent might have a tool to check real-time weather data.
- ```python
  tools: list[Tool] = field(default_factory=list)
  ```

#### **9. mcp_servers**
- **What it does**: Lists external servers (Model Context Protocol) that provide extra tools.
- **Why it’s used**: Lets the agent access tools from outside sources, but you need to manage these servers.
- **Simple Example**: A server might provide a tool to search the web, which the agent can use.
- ```python
  mcp_servers: list[MCPServer] = field(default_factory=list)
  ```

#### **10. mcp_config**
- **What it does**: Sets up how the agent talks to MCP servers.
- **Why it’s used**: Controls things like timeouts when using external tools.
- **Simple Example**: Ensures the agent doesn’t wait too long for a slow server.
- ```python
  mcp_config: MCPConfig = field(default_factory=lambda: MCPConfig())
  ```

#### **11. input_guardrails**
- **What it does**: Checks the input before the agent starts working to ensure it’s safe or valid.
- **Why it’s used**: Protects the agent from bad inputs, like rude words, and only runs for the first agent.
- **Simple Example**: Blocks a question like “Say something mean” if it fails a safety check.
- ```python
  input_guardrails: list[InputGuardrail[TContext]] = field(default_factory=list)
  ```

#### **12. output_guardrails**
- **What it does**: Checks the agent’s final answer to ensure it’s appropriate or correct.
- **Why it’s used**: Makes sure the output meets your rules, like not being too long, and only runs for the final answer.
- **Simple Example**: Flags an answer if it’s offensive or too wordy.
- ```python
  output_guardrails: list[OutputGuardrail[TContext]] = field(default_factory=list)
  ```

#### **13. output_type**
- **What it does**: Defines the format of the agent’s final answer, like a string or a custom object.
- **Why it’s used**: Ensures the answer fits what your code expects, like a number or a list.
- **Simple Example**: Setting `output_type=int` means the agent must return a number, like 25 for temperature.
- ```python
  output_type: type[Any] | AgentOutputSchemaBase | None = None
  ```

#### **14. hooks**
- **What it does**: Lets you monitor what the agent does, like logging its actions.
- **Why it’s used**: Helps you track or debug the agent’s work, like seeing when it starts or finishes.
- **Simple Example**: A hook might log “Agent started answering” to a file.
- ```python
  hooks: AgentHooks[TContext] | None = None
  ```

#### **15. tool_use_behavior**
- **What it does**: Controls how the agent handles tools, like whether to stop after using one or keep going.
- **Why it’s used**: Customizes how tools affect the agent’s work, like stopping after a calculator gives an answer.
- **Simple Example**: Setting `stop_on_first_tool` means the agent stops after using a weather tool.
- ```python
  tool_use_behavior: (
      Literal["run_llm_again", "stop_on_first_tool"] 
      | StopAtTools 
      | ToolsToFinalOutputFunction
  ) = "run_llm_again"
  ```

#### **16. reset_tool_choice**
- **What it does**: Decides if the agent should rethink which tool to use after each use.
- **Why it’s used**: Prevents the agent from getting stuck using the same tool repeatedly.
- **Simple Example**: If `True`, the agent picks a new tool each time instead of reusing the same one.
- ```python
  reset_tool_choice: bool = True
  ```

---

### **Methods**

#### **1. clone**
- **What it does**: Makes a copy of the agent with some settings changed.
- **Why it’s used**: Lets you reuse the agent with new instructions or tools without changing the original.
- **Simple Example**: You copy a “TeacherAgent” to make a “StrictTeacherAgent” with tougher instructions.
- **Schema**: Method that takes keyword arguments and returns a new `Agent` instance.
- ```python
  def clone(self, **kwargs: Any) -> Agent[TContext]
  ```

#### **2. as_tool**
- **What it does**: Turns the agent into a tool that other agents can use.
- **Why it’s used**: Lets another agent call this agent like a tool, but the original agent keeps control (unlike handoffs).
- **Simple Example**: A general agent uses a “WeatherAgent” as a tool to get the weather, then continues the conversation.
- **Schema**: Method that takes a tool name, description, and optional output extractor, returning a `Tool`.
- ```python
  def as_tool(
      self,
      tool_name: str | None,
      tool_description: str | None,
      custom_output_extractor: Callable[[RunResult], Awaitable[str]] | None = None
  ) -> Tool
  ```

#### **3. get_system_prompt**
- **What it does**: Gets the agent’s instructions as a string.
- **Why it’s used**: Prepares the instructions for the AI model, whether they’re fixed text or created by a function.
- **Simple Example**: Returns “Act like a friendly teacher” or runs a function to create instructions based on the user.
- **Schema**: Async method that takes a run context and returns a string or `None`.
- ```python
  async def get_system_prompt(self, run_context: RunContextWrapper[TContext]) -> str | None
  ```

#### **4. get_prompt**
- **What it does**: Gets the agent’s prompt for OpenAI’s Responses API.
- **Why it’s used**: Converts the prompt (object or function) into a format the AI model can use.
- **Simple Example**: Turns a prompt object into instructions like “Use a calculator for math questions.”
- **Schema**: Async method that takes a run context and returns a `ResponsePromptParam` or `None`.
- ```python
  async def get_prompt(self, run_context: RunContextWrapper[TContext]) -> ResponsePromptParam | None
  ```

#### **5. get_mcp_tools**
- **What it does**: Fetches tools from external MCP servers.
- **Why it’s used**: Adds extra tools from servers, like a web search tool, for the agent to use.
- **Simple Example**: Gets a tool from a server to check stock prices for the agent.
- **Schema**: Async method that takes a run context and returns a list of `Tool` objects.
- ```python
  async def get_mcp_tools(self, run_context: RunContextWrapper[TContext]) -> list[Tool]
  ```

#### **6. get_all_tools**
- **What it does**: Combines all tools (MCP and regular) that the agent can use.
- **Why it’s used**: Gives the agent a complete list of tools it can pick from during its work.
- **Simple Example**: Includes a calculator tool and a web search tool from an MCP server.
- **Schema**: Async method that takes a run context and returns a list of `Tool` objects.
- ```python
  async def get_all_tools(self, run_context: RunContextWrapper[Any]) -> list[Tool]
  ```

---

# Runner Class Notes

The `Runner` class in the OpenAI Agents SDK is like a **remote control** that runs an agent’s work. Think of `Agents` as TV channels with their own settings (like instructions or tools), and the `Runner` as the remote that starts and controls them. The `Runner` sends the agent’s instructions each time it runs and can override settings, like choosing a different AI model (e.g., `gpt-4o` instead of the agent’s default). Since the `Runner` has higher priority, its settings (like `model` in `run_config`) take precedence over the agent’s settings. 

---

### **Methods**

#### **1. run**
- **What it does**: Runs an agent asynchronously (in the background) until it gives a final answer or hits a problem, like too many tries or a safety issue.
- **Why it’s used**: Starts the agent’s work, handling tasks like answering questions, using tools, or passing tasks to other agents. It can override agent settings (e.g., model) for more control.
- **Simple Example**: Imagine asking a weather agent, “Is it sunny?” The `Runner` starts the agent, checks if it needs a tool (like a weather API), and keeps going until you get “It’s sunny!” or it fails (e.g., after 5 tries). If you set a different model in the `Runner`, it uses that instead of the agent’s model.
- **Schema**: Async class method that takes an agent, input, and optional settings, returning a `RunResult` with all details.
- ```python
  @classmethod
  async def run(
      cls,
      starting_agent: Agent[TContext],
      input: str | list[TResponseInputItem],
      *,
      context: TContext | None = None,
      max_turns: int = DEFAULT_MAX_TURNS,
      hooks: RunHooks[TContext] | None = None,
      run_config: RunConfig | None = None,
      previous_response_id: str | None = None,
  ) -> RunResult
  ```

#### **2. run_sync**
- **What it does**: Runs an agent synchronously (not in the background), waiting for the answer before moving on, similar to `run` but for non-async environments.
- **Why it’s used**: Useful when you can’t use async code (e.g., in simple scripts or non-async apps). It still overrides agent settings like the model if specified.
- **Simple Example**: You ask a math agent, “What’s 2 + 2?” The `Runner` waits for the agent to answer “4” before doing anything else. If you set `max_turns=3`, it stops after 3 tries if the agent gets stuck. If you choose a different model in `run_config`, it uses that model.
- **Schema**: Class method that takes an agent, input, and optional settings, returning a `RunResult` with all details.
- ```python
  @classmethod
  def run_sync(
      cls,
      starting_agent: Agent[TContext],
      input: str | list[TResponseInputItem],
      *,
      context: TContext | None = None,
      max_turns: int = DEFAULT_MAX_TURNS,
      hooks: RunHooks[TContext] | None = None,
      run_config: RunConfig | None = None,
      previous_response_id: str | None = None,
  ) -> RunResult
  ```

#### **3. run_streamed**
- **What it does**: Runs an agent asynchronously in streaming mode, sending updates live as the agent works, until it finishes or hits a problem.
- **Why it’s used**: Lets you see the agent’s progress in real-time (like a live chat) and can override agent settings for more control, like choosing a specific model.
- **Simple Example**: You ask a story agent, “Tell me a story.” The `Runner` streams each sentence as the agent writes it, like “Once upon a time…” appearing live. If you set a different model in `run_config`, it uses that model instead of the agent’s default.
- **Schema**: Async class method that takes an agent, input, and optional settings, returning a `RunResultStreaming` object for live updates.
- ```python
  @classmethod
  def run_streamed(
      cls,
      starting_agent: Agent[TContext],
      input: str | list[TResponseInputItem],
      context: TContext | None = None,
      max_turns: int = DEFAULT_MAX_TURNS,
      hooks: RunHooks[TContext] | None = None,
      run_config: RunConfig | None = None,
      previous_response_id: str | None = None,
  ) -> RunResultStreaming
  ```

---

# RunResultBase Class Notes

The `RunResultBase` class is like a report card for an agent’s work after it runs. It collects all the important details about what the agent did, like what input it got, what it produced, and whether it passed safety checks. Think of it as a summary of everything that happened when the agent was "working" on a task. This is an abstract class, meaning it’s a blueprint that other classes (like `RunResult` and `RunResultStreaming`) build upon.

### **Attributes**

#### **1. input**
- **What it does**: Stores the original question or data the agent was given to work on.
- **Why it’s used**: Helps you see what the agent started with. If another agent changes the input (e.g., through a handoff), this keeps a record of it.
- **Simple Example**: Imagine you ask an agent, "What's the weather?" This attribute saves that question, even if the agent passes it to another agent to answer.
- ```python
  input: str | list[TResponseInputItem]
  ```

#### **2. new_items**
- **What it does**: Lists new things the agent created, like answers, messages, or tool results (e.g., a weather report from a tool).
- **Why it’s used**: Tracks everything the agent did during its work, so you can see the full history of its actions.
- **Simple Example**: If the agent answers "It’s sunny!" and uses a tool to check the temperature, this list includes the answer and the tool’s output.
- ```python
  new_items: list[RunItem]
  ```

#### **3. raw_responses**
- **What it does**: Saves the exact, unedited responses from the AI model (like GPT-4o).
- **Why it’s used**: Useful for debugging or checking what the AI model said before it was processed into a final answer.
- **Simple Example**: Think of this as the AI’s raw notes before it turns them into a neat answer for you.
- ```python
  raw_responses: list[ModelResponse]
  ```

#### **4. final_output**
- **What it does**: Holds the final answer or result from the last agent that worked on the task.
- **Why it’s used**: Gives you the end result of the agent’s work, like the final answer to your question.
- **Simple Example**: If you asked for the weather and the agent says "25°C, sunny," this is where that answer is stored.
- ```python
  final_output: Any
  ```

#### **5. input_guardrail_results**
- **What it does**: Records whether the input passed safety or validity checks.
- **Why it’s used**: Ensures the input was okay (e.g., not rude or invalid) before the agent started working.
- **Simple Example**: If you send a bad word, this might show that a guardrail blocked it.
- ```python
  input_guardrail_results: list[InputGuardrailResult]
  ```

#### **6. output_guardrail_results**
- **What it does**: Records whether the final answer passed safety or quality checks.
- **Why it’s used**: Makes sure the agent’s answer is appropriate and meets your rules.
- **Simple Example**: If the agent’s answer is too long, this might show that a guardrail flagged it.
- ```python
  output_guardrail_results: list[OutputGuardrailResult]
  ```

#### **7. context_wrapper**
- **What it does**: Holds the custom data (context) used during the agent’s work.
- **Why it’s used**: Lets the agent access extra information (like user preferences) for tools or guardrails.
- **Simple Example**: If you tell the agent your location is "Delhi," this stores that info for the agent to use.
- ```python
  context_wrapper: RunContextWrapper[Any]
  ```

### **Methods**

#### **1. last_agent**
- **What it does**: Tells you which agent finished the task (it’s abstract, so subclasses define it).
- **Why it’s used**: Helps track which agent gave the final answer, especially if tasks were passed between agents.
- **Simple Example**: If your weather question went from a general agent to a weather specialist agent, this points to the specialist.
- **Schema**: Property that returns an `Agent` instance.
- ```python
  @property
  @abc.abstractmethod
  def last_agent(self) -> Agent[Any]
  ```

#### **2. final_output_as**
- **What it does**: Converts the final output to a specific format you want, like a number or custom object.
- **Why it’s used**: Makes sure the output fits what your code expects, and can throw an error if it doesn’t match.
- **Simple Example**: If you expect a number (like 25 for temperature) but get a string, this helps you catch the mismatch.
- **Schema**: Method that takes a type and optional boolean, returning the converted output.
- ```python
  def final_output_as(self, cls: type[T], raise_if_incorrect_type: bool = False) -> T
  ```

#### **3. to_input_list**
- **What it does**: Combines the original input and new items into one list.
- **Why it’s used**: Gives you a full history of inputs and outputs, useful for continuing the conversation or debugging.
- **Simple Example**: If you asked "What’s the weather?" and the agent added "It’s sunny," this creates a list with both.
- **Schema**: Method that returns a list of `TResponseInputItem`.
- ```python
  def to_input_list(self) -> list[TResponseInputItem]
  ```

#### **4. last_response_id**
- **What it does**: Gets the ID of the last AI model response.
- **Why it’s used**: Helps you track or reuse the latest response when working with OpenAI’s Responses API.
- **Simple Example**: Like getting the receipt number for the last thing the AI said.
- **Schema**: Property that returns a string or `None`.
- ```python
  @property
  def last_response_id(self) -> str | None
  ```

---

# RunResult Class Notes

The `RunResult` class builds on `RunResultBase` for non-streaming agent runs (when you get the full result at once, not in real-time). It adds a way to store and access the last agent that ran.

### **Attributes**

#### **1. _last_agent**
- **What it does**: Stores the agent that gave the final answer.
- **Why it’s used**: Lets you know which agent finished the task, especially if multiple agents were involved.
- **Simple Example**: If a math agent solved your problem after a general agent passed it on, this points to the math agent.
- ```python
  _last_agent: Agent[Any]
  ```

### **Methods**

#### **1. last_agent**
- **What it does**: Returns the last agent that worked on the task.
- **Why it’s used**: Makes it easy to check which agent gave the final result for tracking or debugging.
- **Simple Example**: If your question went through three agents, this tells you the last one.
- **Schema**: Property that returns the `_last_agent` as an `Agent` instance.
- ```python
  @property
  def last_agent(self) -> Agent[Any]
  ```

#### **2. __str__**
- **What it does**: Turns the run result into a readable string.
- **Why it’s used**: Makes it easy to print or log the result in a way humans can understand.
- **Simple Example**: Prints something like "Input: What’s the weather? Output: Sunny, 25°C."
- **Schema**: Method that returns a string using a pretty-print function.
- ```python
  def __str__(self) -> str
  ```

---

# RunResultStreaming Class Notes

The `RunResultStreaming` class builds on `RunResultBase` for streaming agent runs, where you get updates in real-time (like watching a live video instead of a recorded one). It adds attributes and methods to handle streaming events and manage the process.

### **Attributes**

#### **1. current_agent**
- **What it does**: Tracks the agent currently working on the task.
- **Why it’s used**: Shows which agent is active during streaming, as it may change with handoffs.
- **Simple Example**: If a general agent hands off to a weather agent, this updates to the weather agent.
- ```python
  current_agent: Agent[Any]
  ```

#### **2. current_turn**
- **What it does**: Counts how many times the agent has run (each run is a "turn").
- **Why it’s used**: Helps keep track of progress and ensures the agent doesn’t run too many times.
- **Simple Example**: If the agent has tried three times to answer, this says "3".
- ```python
  current_turn: int
  ```

#### **3. max_turns**
- **What it does**: Sets the maximum number of times the agent can try to answer.
- **Why it’s used**: Stops the agent from running forever by limiting its attempts.
- **Simple Example**: If set to 5, the agent stops after 5 tries to avoid getting stuck.
- ```python
  max_turns: int
  ```

#### **4. final_output**
- **What it does**: Holds the final answer, starting as `None` until the agent finishes.
- **Why it’s used**: Stores the end result of the streaming run once it’s complete.
- **Simple Example**: When the agent finishes, this might hold "Sunny, 25°C."
- ```python
  final_output: Any
  ```

#### **5. _current_agent_output_schema**
- **What it does**: Defines the expected format of the current agent’s output (hidden from output).
- **Why it’s used**: Ensures the agent’s output matches the format you want, like a number or text.
- **Simple Example**: Like a rule saying the answer must be a temperature number.
- ```python
  _current_agent_output_schema: AgentOutputSchemaBase | None = field(repr=False)
  ```

#### **6. trace**
- **What it does**: Keeps a log of what the agent did during the run (hidden from output).
- **Why it’s used**: Helps developers debug by showing the agent’s steps.
- **Simple Example**: Like a diary of every step the agent took to answer your question.
- ```python
  trace: Trace | None = field(repr=False)
  ```

#### **7. is_complete**
- **What it does**: Shows if the agent has finished its work.
- **Why it’s used**: Tells you when the streaming is done so you can stop waiting for updates.
- **Simple Example**: Becomes `True` when the agent gives its final answer.
- ```python
  is_complete: bool = False
  ```

#### **8. _event_queue**
- **What it does**: Holds real-time events (like new messages) as they happen (hidden from output).
- **Why it’s used**: Manages updates so you can see them live during streaming.
- **Simple Example**: Like a live feed of the agent’s thoughts as it works.
- ```python
  _event_queue: asyncio.Queue[StreamEvent | QueueCompleteSentinel] = field(default_factory=asyncio.Queue, repr=False)
  ```

#### **9. _input_guardrail_queue**
- **What it does**: Stores input guardrail results as they’re checked (hidden from output).
- **Why it’s used**: Keeps track of input safety checks during streaming.
- **Simple Example**: Records if your question passed a "no bad words" check.
- ```python
  _input_guardrail_queue: asyncio.Queue[InputGuardrailResult] = field(default_factory=asyncio.Queue, repr=False)
  ```

#### **10. _run_impl_task**
- **What it does**: Tracks the main task running the agent (hidden from output).
- **Why it’s used**: Manages the background work of the agent’s execution.
- **Simple Example**: Like a worker thread handling the agent’s thinking.
- ```python
  _run_impl_task: asyncio.Task[Any] | None = field(default=None, repr=False)
  ```

#### **11. _input_guardrails_task**
- **What it does**: Tracks the task checking input safety (hidden from output).
- **Why it’s used**: Manages the background process for input validation.
- **Simple Example**: Like a security guard checking your question before the agent sees it.
- ```python
  _input_guardrails_task: asyncio.Task[Any] | None = field(default=None, repr=False)
  ```

#### **12. _output_guardrails_task**
- **What it does**: Tracks the task checking output safety (hidden from output).
- **Why it’s used**: Manages the background process for output validation.
- **Simple Example**: Like a proofreader checking the agent’s answer before it’s sent.
- ```python
  _output_guardrails_task: asyncio.Task[Any] | None = field(default=None, repr=False)
  ```

#### **13. _stored_exception**
- **What it does**: Saves any errors that happen during the run (hidden from output).
- **Why it’s used**: Keeps errors for later review or to stop the run properly.
- **Simple Example**: If the agent fails, this stores the reason, like "too many tries."
- ```python
  _stored_exception: Exception | None = field(default=None, repr=False)
  ```

### **Methods**

#### **1. last_agent**
- **What it does**: Returns the current agent as the last one that ran.
- **Why it’s used**: Tracks the active agent during streaming, updating if handoffs occur.
- **Simple Example**: If a weather agent is working now, this points to it until another agent takes over.
- **Schema**: Property that returns the `current_agent` as an `Agent` instance.
- ```python
  @property
  def last_agent(self) -> Agent[Any]
  ```

#### **2. cancel**
- **What it does**: Stops the streaming run and cleans up tasks.
- **Why it’s used**: Lets you end the run early, like pressing a stop button on a video.
- **Simple Example**: If the agent is taking too long, you can stop it with this.
- **Schema**: Method that takes no arguments and returns None.
- ```python
  def cancel(self) -> None
  ```

#### **3. stream_events**
- **What it does**: Sends live updates (events) as the agent works, like new messages or tool results.
- **Why it’s used**: Lets you see the agent’s progress in real-time, like a live chat.
- **Simple Example**: As the agent types "It’s sunny," you see each word appear live.
- **Schema**: Async method that yields `StreamEvent` objects until the run completes.
- ```python
  async def stream_events(self) -> AsyncIterator[StreamEvent]
  ```

#### **4. _create_error_details**
- **What it does**: Packages run details into an error report if something goes wrong.
- **Why it’s used**: Helps explain why the agent failed, including inputs and outputs.
- **Simple Example**: If the agent crashes, this creates a report like "Failed because input was invalid."
- **Schema**: Method that returns a `RunErrorDetails` object.
- ```python
  def _create_error_details(self) -> RunErrorDetails
  ```

#### **5. _check_errors**
- **What it does**: Looks for problems like too many tries or failed guardrails.
- **Why it’s used**: Catches errors during streaming to stop the agent if needed.
- **Simple Example**: If the agent tries 6 times but the limit is 5, this flags it.
- **Schema**: Method that takes no arguments and returns None, updating `_stored_exception`.
- ```python
  def _check_errors(self)
  ```

#### **6. _cleanup_tasks**
- **What it does**: Stops all background tasks when the run ends.
- **Why it’s used**: Cleans up resources to avoid wasting memory or processing power.
- **Simple Example**: Like shutting down a computer after you’re done working.
- **Schema**: Method that takes no arguments and returns None.
- ```python
  def _cleanup_tasks(self)
  ```

#### **7. __str__**
- **What it does**: Turns the streaming run result into a readable string.
- **Why it’s used**: Makes it easy to print or log the result in a clear way.
- **Simple Example**: Prints something like "Streaming: Agent said ‘Sunny’ so far."
- **Schema**: Method that returns a string using a pretty-print function.
- ```python
  def __str__(self) -> str
  ```

---

## RunConfig and RunOptions Classes Notes

The `RunConfig` and `RunOptions` classes in the OpenAI Agents SDK are like **settings panels** for controlling how an agent runs. `RunConfig` sets global settings for the entire agent run, such as which AI model to use or safety checks, and it can override the agent’s own settings (like the model). `RunOptions` is a dictionary that holds the arguments you pass when starting a run, like the maximum number of tries or custom data. 

---

# RunConfig Class Notes

The `RunConfig` class is like a **master control panel** that sets rules for the entire agent run. It can override settings in the `Agent` class, such as the AI model, to ensure consistency across all agents in the run.

### **Attributes**

#### **1. model**
- **What it does**: Chooses the AI model for the entire run (e.g., “gpt-4o”).
- **Why it’s used**: Overrides the model set in each agent, ensuring all agents use the same model if specified.
- **Simple Example**: If you set `model="gpt-4o"` here, all agents use GPT-4o, even if an agent was set to use a different model.
- ```python
  model: str | Model | None = None
  ```

#### **2. model_provider**
- **What it does**: Defines where to find the AI model (defaults to OpenAI’s provider).
- **Why it’s used**: Tells the system which service provides the model, like OpenAI or another provider.
- **Simple Example**: If you set `model="gpt-4o"`, this ensures the system knows to get it from OpenAI.
- ```python
  model_provider: ModelProvider = field(default_factory=MultiProvider)
  ```

#### **3. model_settings**
- **What it does**: Fine-tunes the AI model’s behavior, like making answers more creative or strict.
- **Why it’s used**: Overrides agent-specific settings to control how all agents respond during the run.
- **Simple Example**: Setting a low “temperature” makes all agents give predictable answers, like “4” for “2 + 2.”
- ```python
  model_settings: ModelSettings | None = None
  ```

#### **4. handoff_input_filter**
- **What it does**: Modifies inputs before they’re passed to a new agent during a handoff.
- **Why it’s used**: Lets you change or filter inputs globally for all handoffs, unless the handoff has its own filter.
- **Simple Example**: If an agent passes “What’s the weather?” to another, this can simplify it to “Weather?” before sending.
- ```python
  handoff_input_filter: HandoffInputFilter | None = None
  ```

#### **5. input_guardrails**
- **What it does**: Lists safety or validity checks for the initial input to the run.
- **Why it’s used**: Ensures the input is safe or valid before any agent starts working.
- **Simple Example**: Blocks a rude question like “Say something mean” before the agent sees it.
- ```python
  input_guardrails: list[InputGuardrail[Any]] | None = None
  ```

#### **6. output_guardrails**
- **What it does**: Lists checks for the final output of the entire run.
- **Why it’s used**: Ensures the final answer is appropriate or meets your rules, like not being too long.
- **Simple Example**: Flags an answer like “Blah blah...” if it’s too vague or offensive.
- ```python
  output_guardrails: list[OutputGuardrail[Any]] | None = None
  ```

#### **7. tracing_disabled**
- **What it does**: Turns off tracking of the agent’s actions (tracing).
- **Why it’s used**: Saves resources if you don’t need a detailed log of what the agent did.
- **Simple Example**: If set to `True`, the system won’t record steps like “Agent checked weather.”
- ```python
  tracing_disabled: bool = False
  ```

#### **8. trace_include_sensitive_data**
- **What it does**: Decides whether to include private data (like user inputs) in the tracking log.
- **Why it’s used**: Protects sensitive information by excluding it from logs if set to `False`.
- **Simple Example**: If `False`, the log skips your question “What’s my bank balance?” but still tracks that the agent ran.
- ```python
  trace_include_sensitive_data: bool = True
  ```

#### **9. workflow_name**
- **What it does**: Names the run for tracking purposes.
- **Why it’s used**: Helps you identify the run in logs, like labeling it “Weather Check” or “Math Solver.”
- **Simple Example**: Naming it “Customer Support” makes it easy to find in logs.
- ```python
  workflow_name: str = "Agent workflow"
  ```

#### **10. trace_id**
- **What it does**: Sets a unique ID for tracking the run.
- **Why it’s used**: Lets you track a specific run, or the system generates an ID if not provided.
- **Simple Example**: Like a ticket number for your agent’s task, like “Run123.”
- ```python
  trace_id: str | None = None
  ```

#### **11. trace_metadata**
- **What it does**: Adds extra details to the tracking log, like user ID or session info.
- **Why it’s used**: Helps you add custom information to understand the context of the run.
- **Simple Example**: You might add `{ "user": "Alice" }` to know who asked the question.
- ```python
  trace_metadata: dict[str, Any] | None = None
  ```

---

# RunOptions Class Notes

The `RunOptions` class is like a **form** you fill out when starting an agent run. It’s a dictionary that holds all the settings you pass to the `Runner` class methods (`run`, `run_sync`, or `run_streamed`). These settings are optional, so you only include what you need.

### **Keys**

#### **1. context**
- **What it does**: Provides custom data for the agent to use during the run.
- **Why it’s used**: Gives the agent extra information, like user preferences or location.
- **Simple Example**: If you set `context={"city": "Delhi"}`, the agent knows to check Delhi’s weather.
- ```python
  context: NotRequired[TContext | None]
  ```

#### **2. max_turns**
- **What it does**: Sets the maximum number of times the agent can try to answer.
- **Why it’s used**: Prevents the agent from getting stuck in a loop by limiting attempts.
- **Simple Example**: Setting `max_turns=5` stops the agent after 5 tries if it can’t answer.
- ```python
  max_turns: NotRequired[int]
  ```

#### **3. hooks**
- **What it does**: Lets you monitor the run with callbacks, like logging when it starts or ends.
- **Why it’s used**: Helps track or debug the agent’s actions during the run.
- **Simple Example**: A hook might log “Agent finished” to a file when the run ends.
- ```python
  hooks: NotRequired[RunHooks[TContext] | None]
  ```

#### **4. run_config**
- **What it does**: Includes the `RunConfig` object to set global run settings.
- **Why it’s used**: Lets you apply settings like the model or guardrails for the entire run.
- **Simple Example**: Setting `run_config.model="gpt-4o"` makes all agents use GPT-4o.
- ```python
  run_config: NotRequired[RunConfig | None]
  ```

#### **5. previous_response_id**
- **What it does**: Provides the ID of a previous AI response to reuse it.
- **Why it’s used**: Saves time by not resending old inputs when using OpenAI’s Responses API.
- **Simple Example**: If you have a response ID from a previous weather query, this lets the agent pick up from there.
- ```python
  previous_response_id: NotRequired[str | None]
  ```

---
# AgentRunner Class Notes

The `AgentRunner` class in the OpenAI Agents SDK is like a **manager** who oversees an agent’s work. It’s responsible for starting, running, and tracking the agent’s tasks, ensuring everything goes smoothly. It uses settings from `RunConfig` and `RunOptions` to control the run, like choosing the AI model or setting limits on attempts. 

>**Warning**: This class is experimental and not part of the public API, so it shouldn’t be used directly or subclassed. 
---

### **Methods**

#### **1. run**
- **What it does**: Runs an agent asynchronously (in the background) until it produces a final answer or hits a problem, like too many tries or a safety issue.
- **Why it’s used**: Manages the agent’s work, including checking inputs, running tools, and handling handoffs to other agents. It uses settings from `RunOptions` and `RunConfig` to control the run.
- **Simple Example**: You ask a weather agent, “Is it sunny?” The `AgentRunner` starts the agent, checks if the question is safe, runs a weather tool if needed, and returns “It’s sunny!” or stops if it fails after a set number of tries (e.g., 5).
- **Schema**: Async method that takes an agent, input, and optional `RunOptions`, returning a `RunResult` with all details.
- ```python
  async def run(
      self,
      starting_agent: Agent[TContext],
      input: str | list[TResponseInputItem],
      **kwargs: Unpack[RunOptions[TContext]]
  ) -> RunResult
  ```

#### **2. run_sync**
- **What it does**: Runs an agent synchronously (waiting for the answer before moving on), wrapping the `run` method for non-async environments.
- **Why it’s used**: Useful for simple scripts where async code isn’t possible, still managing the agent’s work with `RunOptions` and `RunConfig`.
- **Simple Example**: You ask a math agent, “What’s 2 + 2?” The `AgentRunner` waits for “4” before continuing, checking safety and tools, and stops after a set number of tries if needed.
- **Schema**: Method that takes an agent, input, and optional `RunOptions`, returning a `RunResult`.
- ```python
  def run_sync(
      self,
      starting_agent: Agent[TContext],
      input: str | list[TResponseInputItem],
      **kwargs: Unpack[RunOptions[TContext]]
  ) -> RunResult
  ```

#### **3. run_streamed**
- **What it does**: Runs an agent asynchronously in streaming mode, sending live updates as the agent works, until it finishes or fails.
- **Why it’s used**: Lets you see the agent’s progress in real-time (like a live chat) while managing settings like model or guardrails.
- **Simple Example**: You ask a story agent, “Tell me a story.” The `AgentRunner` streams “Once upon a time…” as it’s written, stopping if it hits a limit or safety issue.
- **Schema**: Method that takes an agent, input, and optional `RunOptions`, returning a `RunResultStreaming` object for live updates.
- ```python
  def run_streamed(
      self,
      starting_agent: Agent[TContext],
      input: str | list[TResponseInputItem],
      **kwargs: Unpack[RunOptions[TContext]]
  ) -> RunResultStreaming
  ```

#### **4. _run_input_guardrails_with_queue**
- **What it does**: Runs input safety checks for streaming mode and adds results to a queue.
- **Why it’s used**: Ensures the input is safe or valid in real-time, storing results for the streaming process.
- **Simple Example**: For “What’s the weather?”, it checks if the question is safe and queues the result for live updates.
- **Schema**: Async class method that takes an agent, guardrails, input, context, streaming result, and parent span, updating the queue.
- ```python
  @classmethod
  async def _run_input_guardrails_with_queue(
      cls,
      agent: Agent[Any],
      guardrails: list[InputGuardrail[TContext]],
      input: str | list[TResponseInputItem],
      context: RunContextWrapper[TContext],
      streamed_result: RunResultStreaming,
      parent_span: Span[Any]
  )
  ```

#### **5. _start_streaming**
- **What it does**: Starts the streaming process, managing the agent loop and sending live updates.
- **Why it’s used**: Handles the core logic for streaming, like running tools, handoffs, or stopping when done.
- **Simple Example**: For a story agent, it sends each sentence live, stops if the story is complete, or flags errors like too many tries.
- **Schema**: Async class method that takes input, streaming result, agent, and settings, managing the streaming loop.
- ```python
  @classmethod
  async def _start_streaming(
      cls,
      starting_input: str | list[TResponseInputItem],
      streamed_result: RunResultStreaming,
      starting_agent: Agent[TContext],
      max_turns: int,
      hooks: RunHooks[TContext],
      context_wrapper: RunContextWrapper[TContext],
      run_config: RunConfig,
      previous_response_id: str | None
  )
  ```

#### **6. _run_single_turn_streamed**
- **What it does**: Runs one step of the agent in streaming mode, sending live events like messages or tool results.
- **Why it’s used**: Processes a single turn, streaming updates and deciding what to do next (e.g., handoff or finish).
- **Simple Example**: For “What’s 2 + 2?”, it streams “Let me calculate…” and then “4”, checking tools or guardrails.
- **Schema**: Async class method that takes streaming result, agent, and settings, returning a `SingleStepResult`.
- ```python
  @classmethod
  async def _run_single_turn_streamed(
      cls,
      streamed_result: RunResultStreaming,
      agent: Agent[TContext],
      hooks: RunHooks[TContext],
      context_wrapper: RunContextWrapper[TContext],
      run_config: RunConfig,
      should_run_agent_start_hooks: bool,
      tool_use_tracker: AgentToolUseTracker,
      all_tools: list[Tool],
      previous_response_id: str | None
  ) -> SingleStepResult
  ```

#### **7. _run_single_turn**
- **What it does**: Runs one step of the agent in non-streaming mode, handling tools, prompts, and responses.
- **Why it’s used**: Processes a single turn for non-streaming runs, deciding if the agent should continue or stop.
- **Simple Example**: For “What’s the weather?”, it runs the agent, checks a weather tool, and prepares the next step.
- **Schema**: Async class method that takes agent, tools, input, and settings, returning a `SingleStepResult`.
- ```python
  @classmethod
  async def _run_single_turn(
      cls,
      *,
      agent: Agent[TContext],
      all_tools: list[Tool],
      original_input: str | list[TResponseInputItem],
      generated_items: list[RunItem],
      hooks: RunHooks[TContext],
      context_wrapper: RunContextWrapper[TContext],
      run_config: RunConfig,
      should_run_agent_start_hooks: bool,
      tool_use_tracker: AgentToolUseTracker,
      previous_response_id: str | None
  ) -> SingleStepResult
  ```

#### **8. _get_single_step_result_from_response**
- **What it does**: Processes the AI’s response to create a result for one turn, handling tools or handoffs.
- **Why it’s used**: Turns the raw AI response into a structured result, deciding the next step (e.g., finish or continue).
- **Simple Example**: If the AI says “It’s sunny” after a weather tool, this packages it as a final result.
- **Schema**: Async class method that takes response details and returns a `SingleStepResult`.
- ```python
  @classmethod
  async def _get_single_step_result_from_response(
      cls,
      *,
      agent: Agent[TContext],
      all_tools: list[Tool],
      original_input: str | list[TResponseInputItem],
      pre_step_items: list[RunItem],
      new_response: ModelResponse,
      output_schema: AgentOutputSchemaBase | None,
      handoffs: list[Handoff],
      hooks: RunHooks[TContext],
      context_wrapper: RunContextWrapper[TContext],
      run_config: RunConfig,
      tool_use_tracker: AgentToolUseTracker
  ) -> SingleStepResult
  ```

#### **9. _run_input_guardrails**
- **What it does**: Runs safety checks on the input and stops if any fail.
- **Why it’s used**: Ensures the input is safe or valid before the agent processes it.
- **Simple Example**: Blocks a question like “Say something rude” if it fails a safety check.
- **Schema**: Async class method that takes guardrails, input, and context, returning a list of `InputGuardrailResult`.
- ```python
  @classmethod
  async def _run_input_guardrails(
      cls,
      agent: Agent[Any],
      guardrails: list[InputGuardrail[TContext]],
      input: str | list[TResponseInputItem],
      context: RunContextWrapper[TContext]
  ) -> list[InputGuardrailResult]
  ```

#### **10. _run_output_guardrails**
- **What it does**: Runs safety or quality checks on the agent’s final output, stopping if any fail.
- **Why it’s used**: Ensures the final answer is appropriate, like not being offensive or too long.
- **Simple Example**: Flags an answer like “Blah blah...” if it’s too vague.
- **Schema**: Async class method that takes guardrails, agent, output, and context, returning a list of `OutputGuardrailResult`.
- ```python
  @classmethod
  async def _run_output_guardrails(
      cls,
      guardrails: list[OutputGuardrail[TContext]],
      agent: Agent[TContext],
      agent_output: Any,
      context: RunContextWrapper[TContext]
  ) -> list[OutputGuardrailResult]
  ```

#### **11. _get_new_response**
- **What it does**: Gets a new response from the AI model for one turn, using the agent’s settings.
- **Why it’s used**: Fetches the AI’s answer, including tools or handoffs, for the current step.
- **Simple Example**: For “What’s 2 + 2?”, it gets the AI’s response, like “Let me calculate… 4.”
- **Schema**: Async class method that takes agent, input, and settings, returning a `ModelResponse`.
- ```python
  @classmethod
  async def _get_new_response(
      cls,
      agent: Agent[TContext],
      system_prompt: str | None,
      input: list[TResponseInputItem],
      output_schema: AgentOutputSchemaBase | None,
      all_tools: list[Tool],
      handoffs: list[Handoff],
      context_wrapper: RunContextWrapper[TContext],
      run_config: RunConfig,
      tool_use_tracker: AgentToolUseTracker,
      previous_response_id: str | None,
      prompt_config: ResponsePromptParam | None
  ) -> ModelResponse
  ```

#### **12. _get_output_schema**
- **What it does**: Gets the expected format of the agent’s output.
- **Why it’s used**: Ensures the AI’s answer matches the format you want, like a number or string.
- **Simple Example**: If the agent should return a number for temperature, this sets it to expect an integer.
- **Schema**: Class method that takes an agent and returns an `AgentOutputSchemaBase` or `None`.
- ```python
  @classmethod
  def _get_output_schema(cls, agent: Agent[Any]) -> AgentOutputSchemaBase | None
  ```

#### **13. _get_handoffs**
- **What it does**: Gets the list of enabled handoff agents or objects for the current agent.
- **Why it’s used**: Identifies which agents can take over tasks, ensuring only active ones are used.
- **Simple Example**: If a general agent has a “MathAgent” handoff, this lists it if enabled.
- **Schema**: Async class method that takes an agent and context, returning a list of `Handoff` objects.
- ```python
  @classmethod
  async def _get_handoffs(
      cls, agent: Agent[Any], context_wrapper: RunContextWrapper[Any]
  ) -> list[Handoff]
  ```

#### **14. _get_all_tools**
- **What it does**: Gets all tools available to the agent, including external ones.
- **Why it’s used**: Provides a complete list of tools the agent can use, like calculators or APIs.
- **Simple Example**: Includes a weather tool and a web search tool for the agent to choose from.
- **Schema**: Async class method that takes an agent and context, returning a list of `Tool` objects.
- ```python
  @classmethod
  async def _get_all_tools(
      cls, agent: Agent[Any], context_wrapper: RunContextWrapper[Any]
  ) -> list[Tool]
  ```

#### **15. _get_model**
- **What it does**: Chooses the AI model to use, prioritizing `RunConfig` over the agent’s model.
- **Why it’s used**: Ensures the correct model is used, like “gpt-4o” if set in `RunConfig`.
- **Simple Example**: Uses “gpt-4o” from `RunConfig` even if the agent specified a different model.
- **Schema**: Class method that takes an agent and `RunConfig`, returning a `Model` object.
- ```python
  @classmethod
  def _get_model(cls, agent: Agent[Any], run_config: RunConfig) -> Model
  ```

---

### BaseClient and AsyncOpenAI Class Notes

The `BaseClient` and `AsyncOpenAI` classes are part of the OpenAI Agents SDK and handle communication with APIs, like sending requests to OpenAI’s servers. 

`BaseClient` is like a **toolbox** for making HTTP requests, managing retries, and handling responses. 

`AsyncOpenAI` builds on it to create a client specifically for OpenAI’s API, adding features like API key authentication and access to resources like chat or images. 

---

# BaseClient Class Notes

The `BaseClient` class is a generic foundation for making HTTP requests to APIs. It handles things like retries, timeouts, and formatting requests and responses. It’s like a **mail carrier** who ensures your letters (requests) are sent correctly and handles any delivery issues.

### **Attributes**

#### **1. _client**
- **What it does**: Holds the HTTP client (e.g., `httpx.Client`) used to send requests.
- **Why it’s used**: Acts as the engine for sending and receiving data from the API.
- **Simple Example**: Like a delivery truck that carries your request to the API and brings back the response.
- ```python
  _client: _HttpxClientT
  ```

#### **2. _version**
- **What it does**: Stores the version of the API or client.
- **Why it’s used**: Helps track which version of the API you’re using for compatibility.
- **Simple Example**: If the API is version “1.0,” this ensures your requests match that version.
- ```python
  _version: str
  ```

#### **3. _base_url**
- **What it does**: Sets the main URL for the API (e.g., `https://api.openai.com/v1`).
- **Why it’s used**: Tells the client where to send requests.
- **Simple Example**: Like the main address of a post office where all your API requests go.
- ```python
  _base_url: URL
  ```

#### **4. max_retries**
- **What it does**: Sets how many times to retry a failed request.
- **Why it’s used**: Prevents giving up too soon if the API is busy or fails temporarily.
- **Simple Example**: If set to 3, it tries sending a request up to 3 times if it fails.
- ```python
  max_retries: int = DEFAULT_MAX_RETRIES
  ```

#### **5. timeout**
- **What it does**: Sets how long to wait for a response before giving up.
- **Why it’s used**: Avoids waiting forever if the API is slow or down.
- **Simple Example**: If set to 30 seconds, it stops waiting after 30 seconds.
- ```python
  timeout: Union[float, Timeout, None] = DEFAULT_TIMEOUT
  ```

#### **6. _strict_response_validation**
- **What it does**: Decides whether to strictly check if API responses match expected formats.
- **Why it’s used**: Ensures responses are correct, catching errors early if enabled.
- **Simple Example**: If `True`, it checks “‘sunny’ is a string” for a weather response.
- ```python
  _strict_response_validation: bool
  ```

#### **7. _idempotency_header**
- **What it does**: Sets a header to ensure safe retries of the same request.
- **Why it’s used**: Prevents duplicate actions if a request is retried.
- **Simple Example**: Like a unique ticket number to avoid sending the same payment twice.
- ```python
  _idempotency_header: str | None
  ```

#### **8. _default_stream_cls**
- **What it does**: Defines the default class for streaming responses.
- **Why it’s used**: Sets how streaming data (like live chat) is handled.
- **Simple Example**: Used to stream a story sentence-by-sentence instead of waiting for the whole thing.
- ```python
  _default_stream_cls: type[_DefaultStreamT] | None = None
  ```

### **Methods**

#### **1. __init__**
- **What it does**: Sets up the client with settings like URL, retries, and timeout.
- **Why it’s used**: Initializes the client to start sending requests.
- **Simple Example**: Like setting up a delivery service with an address, retry policy, and wait time.
- **Schema**: Constructor that takes version, base URL, validation setting, retries, timeout, and headers.
- ```python
  def __init__(
      self,
      *,
      version: str,
      base_url: str | URL,
      _strict_response_validation: bool,
      max_retries: int = DEFAULT_MAX_RETRIES,
      timeout: float | Timeout | None = DEFAULT_TIMEOUT,
      custom_headers: Mapping[str, str] | None = None,
      custom_query: Mapping[str, object] | None = None
  ) -> None
  ```

#### **2. _enforce_trailing_slash**
- **What it does**: Adds a “/” to the end of a URL if missing.
- **Why it’s used**: Ensures URLs are consistent for API requests.
- **Simple Example**: Changes `https://api.openai.com` to `https://api.openai.com/`.
- **Schema**: Takes a URL and returns it with a trailing slash.
- ```python
  def _enforce_trailing_slash(self, url: URL) -> URL
  ```

#### **3. _make_status_error_from_response**
- **What it does**: Creates an error from an API response if it fails.
- **Why it’s used**: Turns HTTP errors (like 404) into specific error types.
- **Simple Example**: If the API returns “404 Not Found,” it creates a `NotFoundError`.
- **Schema**: Takes an HTTP response and returns an `APIStatusError`.
- ```python
  def _make_status_error_from_response(self, response: httpx.Response) -> APIStatusError
  ```

#### **4. _make_status_error**
- **What it does**: Creates a specific error based on the response status code (not implemented in `BaseClient`).
- **Why it’s used**: Allows subclasses to define custom error types (e.g., `BadRequestError`).
- **Simple Example**: Subclasses might turn a 400 status into a `BadRequestError`.
- **Schema**: Takes an error message, body, and response, returning an `APIStatusError`.
- ```python
  def _make_status_error(
      self,
      err_msg: str,
      *,
      body: object,
      response: httpx.Response
  ) -> _exceptions.APIStatusError
  ```

#### **5. _build_headers**
- **What it does**: Creates headers for HTTP requests, like content type or retry count.
- **Why it’s used**: Ensures requests have the right metadata, like authentication or retry info.
- **Simple Example**: Adds “Content-Type: application/json” to tell the API to expect JSON.
- **Schema**: Takes request options and retry count, returning `httpx.Headers`.
- ```python
  def _build_headers(self, options: FinalRequestOptions, *, retries_taken: int = 0) -> httpx.Headers
  ```

#### **6. _prepare_url**
- **What it does**: Combines the base URL with a specific path for the request.
- **Why it’s used**: Ensures the full URL is correct, like `base_url + /chat`.
- **Simple Example**: Turns `/chat` into `https://api.openai.com/v1/chat`.
- **Schema**: Takes a URL path and returns a complete `URL`.
- ```python
  def _prepare_url(self, url: str) -> URL
  ```

#### **7. _make_sse_decoder**
- **What it does**: Creates a decoder for Server-Sent Events (SSE) for streaming.
- **Why it’s used**: Helps process live data streams, like real-time chat responses.
- **Simple Example**: Decodes live updates for a streaming story response.
- **Schema**: Returns an `SSEDecoder` or `SSEBytesDecoder`.
- ```python
  def _make_sse_decoder(self) -> SSEDecoder | SSEBytesDecoder
  ```

#### **8. _build_request**
- **What it does**: Builds an HTTP request with method, URL, headers, and data.
- **Why it’s used**: Prepares everything needed to send a request to the API.
- **Simple Example**: Builds a request to ask for weather data with JSON headers.
- **Schema**: Takes request options and retry count, returning an `httpx.Request`.
- ```python
  def _build_request(self, options: FinalRequestOptions, *, retries_taken: int = 0) -> httpx.Request
  ```

#### **9. _serialize_multipartform**
- **What it does**: Converts data into a format for multipart form requests (e.g., file uploads).
- **Why it’s used**: Prepares data like files or forms for API requests.
- **Simple Example**: Formats an image file and description for an upload request.
- **Schema**: Takes a data mapping and returns a dictionary for multipart forms.
- ```python
  def _serialize_multipartform(self, data: Mapping[object, object]) -> dict[str, object]
  ```

#### **10. _maybe_override_cast_to**
- **What it does**: Checks if the response type should be changed based on headers.
- **Why it’s used**: Allows custom response handling for raw or streaming responses.
- **Simple Example**: If a header says “return raw response,” it adjusts the output type.
- **Schema**: Takes the expected type and options, returning the adjusted type.
- ```python
  def _maybe_override_cast_to(self, cast_to: type[ResponseT], options: FinalRequestOptions) -> type[ResponseT]
  ```

#### **11. _should_stream_response_body**
- **What it does**: Checks if the response should be streamed based on headers.
- **Why it’s used**: Decides whether to handle the response as a live stream.
- **Simple Example**: Streams a chat response if the header says “stream.”
- **Schema**: Takes an `httpx.Request` and returns a boolean.
- ```python
  def _should_stream_response_body(self, request: httpx.Request) -> bool
  ```

#### **12. _process_response_data**
- **What it does**: Converts API response data into the expected format.
- **Why it’s used**: Ensures the response matches the format your code expects, like a string or object.
- **Simple Example**: Turns “sunny” into a string or a JSON object into a custom class.
- **Schema**: Takes data, expected type, and response, returning the processed data.
- ```python
  def _process_response_data(
      self,
      *,
      data: object,
      cast_to: type[ResponseT],
      response: httpx.Response
  ) -> ResponseT
  ```

#### **13. _idempotency_key**
- **What it does**: Generates a unique key for safe retries.
- **Why it’s used**: Prevents duplicate actions if a request is retried.
- **Simple Example**: Creates a key like “retry-123” to avoid double-charging a payment.
- **Schema**: Returns a string key.
- ```python
  def _idempotency_key(self) -> str
  ```

---

# AsyncOpenAI Class Notes

The `AsyncOpenAI` class is a specialized client for OpenAI’s API, built on top of `AsyncAPIClient` (which extends `BaseClient`). It’s like a **customized mail carrier** for OpenAI, handling authentication with an API key and providing access to resources like chat, images, or completions. It supports asynchronous operations for faster, non-blocking requests.

### **Attributes**

#### **1. api_key**
- **What it does**: Stores the OpenAI API key for authentication.
- **Why it’s used**: Proves your identity to access OpenAI’s API.
- **Simple Example**: Like a password to log into OpenAI’s services.
- ```python
  api_key: str
  ```

#### **2. organization**
- **What it does**: Specifies the organization ID for your OpenAI account.
- **Why it’s used**: Links requests to a specific organization if you have multiple.
- **Simple Example**: Identifies your company’s account for billing or access control.
- ```python
  organization: str | None
  ```

#### **3. project**
- **What it does**: Specifies the project ID for your OpenAI account.
- **Why it’s used**: Organizes requests under a specific project for tracking.
- **Simple Example**: Like labeling requests for a “Weather App” project.
- ```python
  project: str | None
  ```

#### **4. webhook_secret**
- **What it does**: Stores a secret key for verifying webhook events.
- **Why it’s used**: Ensures webhook messages from OpenAI are genuine.
- **Simple Example**: Like a code to confirm a delivery is from OpenAI.
- ```python
  webhook_secret: str | None
  ```

#### **5. websocket_base_url**
- **What it does**: Sets the URL for WebSocket connections (defaults to `wss://` version of `base_url`).
- **Why it’s used**: Used for real-time communication, like live updates.
- **Simple Example**: Connects to `wss://api.openai.com` for live chat streams.
- ```python
  websocket_base_url: str | httpx.URL | None
  ```

### **Methods**

#### **1. __init__**
- **What it does**: Sets up the OpenAI client with API key, URL, and other settings.
- **Why it’s used**: Prepares the client to make requests to OpenAI’s API.
- **Simple Example**: Like registering a delivery service with OpenAI’s address and your API key.
- **Schema**: Constructor that takes API key, organization, project, and other settings.
- ```python
  def __init__(
      self,
      *,
      api_key: str | None = None,
      organization: str | None = None,
      project: str | None = None,
      webhook_secret: str | None = None,
      base_url: str | httpx.URL | None = None,
      websocket_base_url: str | httpx.URL | None = None,
      timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
      max_retries: int = DEFAULT_MAX_RETRIES,
      default_headers: Mapping[str, str] | None = None,
      default_query: Mapping[str, object] | None = None,
      http_client: httpx.AsyncClient | None = None,
      _strict_response_validation: bool = False
  ) -> None
  ```

#### **2. completions**
- **What it does**: Provides access to text completion features (e.g., generating text).
- **Why it’s used**: Lets you generate text, like finishing a sentence.
- **Simple Example**: Ask “Once upon a time” and get a completed story.
- **Schema**: Cached property returning an `AsyncCompletions` object.
- ```python
  @cached_property
  def completions(self) -> AsyncCompletions
  ```

#### **3. chat**
- **What it does**: Provides access to chat features (e.g., conversational AI).
- **Why it’s used**: Enables building chatbots or conversational apps.
- **Simple Example**: Send “Hi, how’s the weather?” and get a chat response.
- **Schema**: Cached property returning an `AsyncChat` object.
- ```python
  @cached_property
  def chat(self) -> AsyncChat
  ```

#### **4. embeddings**
- **What it does**: Provides access to embedding features (e.g., text-to-vector conversion).
- **Why it’s used**: Converts text to numbers for tasks like search or clustering.
- **Simple Example**: Turn “cat” into a vector for similarity comparisons.
- **Schema**: Cached property returning an `AsyncEmbeddings` object.
- ```python
  @cached_property
  def embeddings(self) -> AsyncEmbeddings
  ```

#### **5. files**
- **What it does**: Provides access to file management (e.g., uploading files).
- **Why it’s used**: Manages files for training or processing data.
- **Simple Example**: Upload a dataset for fine-tuning a model.
- **Schema**: Cached property returning an `AsyncFiles` object.
- ```python
  @cached_property
  def files(self) -> AsyncFiles
  ```

#### **6. images**
- **What it does**: Provides access to image generation or processing features.
- **Why it’s used**: Creates or edits images, like generating artwork.
- **Simple Example**: Generate an image from “A sunset over mountains.”
- **Schema**: Cached property returning an `AsyncImages` object.
- ```python
  @cached_property
  def images(self) -> AsyncImages
  ```

#### **7. audio**
- **What it does**: Provides access to audio features (e.g., speech-to-text or text-to-speech).
- **Why it’s used**: Handles audio tasks, like transcribing speech.
- **Simple Example**: Convert spoken words to text for a voice assistant.
- **Schema**: Cached property returning an `AsyncAudio` object.
- ```python
  @cached_property
  def audio(self) -> AsyncAudio
  ```

#### **8. moderations**
- **What it does**: Provides access to content moderation features.
- **Why it’s used**: Checks if text is safe or appropriate.
- **Simple Example**: Flags “hate speech” in a user comment.
- **Schema**: Cached property returning an `AsyncModerations` object.
- ```python
  @cached_property
  def moderations(self) -> AsyncModerations
  ```

#### **9. models**
- **What it does**: Provides access to model management (e.g., listing available models).
- **Why it’s used**: Lets you check or select models like “gpt-4o.”
- **Simple Example**: List all models you can use with your API key.
- **Schema**: Cached property returning an `AsyncModels` object.
- ```python
  @cached_property
  def models(self) -> AsyncModels
  ```

#### **10. fine_tuning**
- **What it does**: Provides access to fine-tuning features for customizing models.
- **Why it’s used**: Lets you train models for specific tasks.
- **Simple Example**: Fine-tune a model to answer math questions better.
- **Schema**: Cached property returning an `AsyncFineTuning` object.
- ```python
  @cached_property
  def fine_tuning(self) -> AsyncFineTuning
  ```

#### **11. vector_stores**
- **What it does**: Provides access to vector storage for managing embeddings.
- **Why it’s used**: Stores and retrieves vectors for search or analysis.
- **Simple Example**: Store vectors for “cat” and “dog” to compare similarity.
- **Schema**: Cached property returning an `AsyncVectorStores` object.
- ```python
  @cached_property
  def vector_stores(self) -> AsyncVectorStores
  ```

#### **12. webhooks**
- **What it does**: Provides access to webhook management for event notifications.
- **Why it’s used**: Handles real-time updates from OpenAI, like job completion.
- **Simple Example**: Get notified when a fine-tuning job finishes.
- **Schema**: Cached property returning an `AsyncWebhooks` object.
- ```python
  @cached_property
  def webhooks(self) -> AsyncWebhooks
  ```

#### **13. beta**
- **What it does**: Provides access to experimental (beta) features.
- **Why it’s used**: Lets you try new OpenAI features before they’re official.
- **Simple Example**: Test a new chat feature still in development.
- **Schema**: Cached property returning an `AsyncBeta` object.
- ```python
  @cached_property
  def beta(self) -> AsyncBeta
  ```

#### **14. batches**
- **What it does**: Provides access to batch processing for multiple requests.
- **Why it’s used**: Handles large sets of requests efficiently.
- **Simple Example**: Process 100 questions at once instead of one-by-one.
- **Schema**: Cached property returning an `AsyncBatches` object.
- ```python
  @cached_property
  def batches(self) -> AsyncBatches
  ```

#### **15. uploads**
- **What it does**: Provides access to upload features for large data.
- **Why it’s used**: Manages uploading big files, like datasets.
- **Simple Example**: Upload a large text file for model training.
- **Schema**: Cached property returning an `AsyncUploads` object.
- ```python
  @cached_property
  def uploads(self) -> AsyncUploads
  ```

#### **16. responses**
- **What it does**: Provides access to response management for API interactions.
- **Why it’s used**: Handles responses from OpenAI’s API, like chat replies.
- **Simple Example**: Get a chat response for “Tell me a joke.”
- **Schema**: Cached property returning an `AsyncResponses` object.
- ```python
  @cached_property
  def responses(self) -> AsyncResponses
  ```

#### **17. evals**
- **What it does**: Provides access to evaluation features for testing models.
- **Why it’s used**: Tests how well a model performs on specific tasks.
- **Simple Example**: Check if a model answers math questions correctly.
- **Schema**: Cached property returning an `AsyncEvals` object.
- ```python
  @cached_property
  def evals(self) -> AsyncEvals
  ```

#### **18. containers**
- **What it does**: Provides access to container management (e.g., for model deployment).
- **Why it’s used**: Manages environments for running models.
- **Simple Example**: Set up a container to run a custom model.
- **Schema**: Cached property returning an `AsyncContainers` object.
- ```python
  @cached_property
  def containers(self) -> AsyncContainers
  ```

#### **19. with_raw_response**
- **What it does**: Returns a client that gives raw API responses.
- **Why it’s used**: Lets you access unprocessed responses for custom handling.
- **Simple Example**: Get the raw JSON from a chat response for debugging.
- **Schema**: Cached property returning an `AsyncOpenAIWithRawResponse` object.
- ```python
  @cached_property
  def with_raw_response(self) -> AsyncOpenAIWithRawResponse
  ```

#### **20. with_streaming_response**
- **What it does**: Returns a client for streaming API responses.
- **Why it’s used**: Handles live updates, like streaming a chat reply.
- **Simple Example**: Stream “Once upon a time…” as it’s generated.
- **Schema**: Cached property returning an `AsyncOpenAIWithStreamedResponse` object.
- ```python
  @cached_property
  def with_streaming_response(self) -> AsyncOpenAIWithStreamedResponse
  ```

#### **21. copy (and with_options alias)**
- **What it does**: Creates a new client with the same settings, allowing overrides.
- **Why it’s used**: Lets you reuse settings but tweak things like timeout.
- **Simple Example**: Copy a client but change the timeout to 10 seconds.
- **Schema**: Takes optional settings and returns a new `AsyncOpenAI` instance.
- ```python
  def copy(
      self,
      *,
      api_key: str | None = None,
      organization: str | None = None,
      project: str | None = None,
      webhook_secret: str | None = None,
      websocket_base_url: str | httpx.URL | None = None,
      base_url: str | httpx.URL | None = None,
      timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
      http_client: httpx.AsyncClient | None = None,
      max_retries: int | NotGiven = NOT_GIVEN,
      default_headers: Mapping[str, str] | None = None,
      set_default_headers: Mapping[str, str] | None = None,
      default_query: Mapping[str, object] | None = None,
      set_default_query: Mapping[str, object] | None = None,
      _extra_kwargs: Mapping[str, Any] = {}
  ) -> Self
  ```

#### **22. _make_status_error**
- **What it does**: Creates specific error types based on HTTP status codes.
- **Why it’s used**: Turns errors like 404 into meaningful errors like `NotFoundError`.
- **Simple Example**: A 429 response becomes a `RateLimitError` to handle rate limits.
- **Schema**: Takes an error message, body, and response, returning an `APIStatusError`.
- ```python
  def _make_status_error(
      self,
      err_msg: str,
      *,
      body: object,
      response: httpx.Response
  ) -> APIStatusError
  ```

---
### Model, ModelProvider, and OpenAIChatCompletionsModel Class Notes

The `Model`, `ModelProvider`, and `OpenAIChatCompletionsModel` classes are part of the OpenAI Agents SDK. They work together to interact with language models (LLMs) like those from OpenAI, handling tasks like generating responses or streaming live answers. `Model` is like a **blueprint** for how to talk to an LLM, `ModelProvider` is a **lookup service** to find the right model, and `OpenAIChatCompletionsModel` is a **specific worker** that uses OpenAI’s API to get responses. 

---

# Model Class Notes

The `Model` class is an abstract base class (ABC) that defines the basic structure for interacting with an LLM. It’s like a **recipe** that outlines how to ask a model for answers, but it doesn’t cook the meal itself—other classes do that.

### **Methods**

#### **1. get_response**
- **What it does**: Asynchronously gets a complete response from the LLM based on input and settings.
- **Why it’s used**: Fetches a full answer, like a story or calculation, in one go.
- **Simple Example**: You ask, “What’s 2 + 2?” and it returns “4” after processing with tools or settings.
- **Schema**: Async method that takes instructions, input, settings, tools, schema, handoffs, tracing, and optional parameters, returning a `ModelResponse`.
- ```python
  async def get_response(
      self,
      system_instructions: str | None,
      input: str | list[TResponseInputItem],
      model_settings: ModelSettings,
      tools: list[Tool],
      output_schema: AgentOutputSchemaBase | None,
      handoffs: list[Handoff],
      tracing: ModelTracing,
      *,
      previous_response_id: str | None,
      prompt: ResponsePromptParam | None
  ) -> ModelResponse
  ```

#### **2. stream_response**
- **What it does**: Asynchronously streams partial responses from the LLM as they’re generated.
- **Why it’s used**: Provides live updates, like seeing a story written sentence by sentence.
- **Simple Example**: For “Tell me a story,” it streams “Once upon a time…” as it’s written.
- **Schema**: Async method that takes the same parameters as `get_response`, returning an iterator of `TResponseStreamEvent`.
- ```python
  async def stream_response(
      self,
      system_instructions: str | None,
      input: str | list[TResponseInputItem],
      model_settings: ModelSettings,
      tools: list[Tool],
      output_schema: AgentOutputSchemaBase | None,
      handoffs: list[Handoff],
      tracing: ModelTracing,
      *,
      previous_response_id: str | None,
      prompt: ResponsePromptParam | None
  ) -> AsyncIterator[TResponseStreamEvent]
  ```

---

# ModelProvider Class Notes

The `ModelProvider` class is an abstract base class that acts like a **librarian** who finds the right model (like “gpt-4o”) when you ask for it by name.

### **Methods**

#### **1. get_model**
- **What it does**: Retrieves a model based on its name.
- **Why it’s used**: Helps you select the correct LLM for your task.
- **Simple Example**: You say “gpt-4o,” and it hands you the `OpenAIChatCompletionsModel` for that model.
- **Schema**: Takes a model name and returns a `Model` instance.
- ```python
  def get_model(self, model_name: str | None) -> Model
  ```

---

# OpenAIChatCompletionsModel Class Notes

The `OpenAIChatCompletionsModel` class is a concrete implementation of `Model` that uses OpenAI’s API to interact with chat models like “gpt-4o.” It’s like a **chef** who follows the `Model` recipe to cook up responses using OpenAI’s tools.

### **Attributes**

#### **1. model**
- **What it does**: Stores the name or type of the OpenAI model (e.g., “gpt-4o”).
- **Why it’s used**: Specifies which model to use for generating responses.
- **Simple Example**: If set to “gpt-4o,” it uses that model to answer questions.
- ```python
  model: str | ChatModel
  ```

#### **2. _client**
- **What it does**: Holds the `AsyncOpenAI` client for making API requests.
- **Why it’s used**: Connects to OpenAI’s servers to send and receive data.
- **Simple Example**: Like a phone line to OpenAI’s API for sending questions.
- ```python
  _client: AsyncOpenAI
  ```

### **Methods**

#### **1. __init__**
- **What it does**: Initializes the model with a name and OpenAI client.
- **Why it’s used**: Sets up the model to start making API calls.
- **Simple Example**: Like hiring a chef and giving them a recipe book (model name) and ingredients (client).
- **Schema**: Takes a model name and `AsyncOpenAI` client.
- ```python
  def __init__(self, model: str | ChatModel, openai_client: AsyncOpenAI) -> None
  ```

#### **2. _non_null_or_not_given**
- **What it does**: Returns a value if it’s not `None`, otherwise returns `NOT_GIVEN`.
- **Why it’s used**: Handles optional parameters to avoid sending `None` to the API.
- **Simple Example**: If `temperature` is `None`, it sends `NOT_GIVEN` to use the API’s default.
- **Schema**: Takes any value and returns it or `NOT_GIVEN`.
- ```python
  def _non_null_or_not_given(self, value: Any) -> Any
  ```

#### **3. get_response**
- **What it does**: Fetches a complete response from OpenAI’s chat API.
- **Why it’s used**: Gets a full answer, like a completed story or calculation.
- **Simple Example**: Ask “What’s the weather?” and get “It’s sunny!” with usage stats.
- **Schema**: Takes instructions, input, settings, tools, schema, handoffs, tracing, and optional parameters, returning a `ModelResponse`.
- ```python
  async def get_response(
      self,
      system_instructions: str | None,
      input: str | list[TResponseInputItem],
      model_settings: ModelSettings,
      tools: list[Tool],
      output_schema: AgentOutputSchemaBase | None,
      handoffs: list[Handoff],
      tracing: ModelTracing,
      previous_response_id: str | None,
      prompt: ResponsePromptParam | None = None
  ) -> ModelResponse
  ```

#### **4. stream_response**
- **What it does**: Streams partial responses from OpenAI’s chat API as they’re generated.
- **Why it’s used**: Provides live updates, like seeing a chatbot type in real-time.
- **Simple Example**: For “Tell me a joke,” it streams “Why did the chicken…” as it’s written.
- **Schema**: Takes the same parameters as `get_response`, returning an iterator of `TResponseStreamEvent`.
- ```python
  async def stream_response(
      self,
      system_instructions: str | None,
      input: str | list[TResponseInputItem],
      model_settings: ModelSettings,
      tools: list[Tool],
      output_schema: AgentOutputSchemaBase | None,
      handoffs: list[Handoff],
      tracing: ModelTracing,
      previous_response_id: str | None,
      prompt: ResponsePromptParam | None = None
  ) -> AsyncIterator[TResponseStreamEvent]
  ```

#### **5. _fetch_response**
- **What it does**: Makes the actual API call to OpenAI’s chat completions endpoint, either streaming or non-streaming.
- **Why it’s used**: Handles the core logic of sending requests and getting responses.
- **Simple Example**: Sends “What’s 2 + 2?” to the API and gets “4” or streams the response.
- **Schema**: Overloaded method that returns a `ChatCompletion` (non-streaming) or a tuple of `Response` and `AsyncStream[ChatCompletionChunk]` (streaming).
- ```python
  async def _fetch_response(
      self,
      system_instructions: str | None,
      input: str | list[TResponseInputItem],
      model_settings: ModelSettings,
      tools: list[Tool],
      output_schema: AgentOutputSchemaBase | None,
      handoffs: list[Handoff],
      span: Span[GenerationSpanData],
      tracing: ModelTracing,
      stream: bool = False,
      prompt: ResponsePromptParam | None = None
  ) -> ChatCompletion | tuple[Response, AsyncStream[ChatCompletionChunk]]
  ```

#### **6. _get_client**
- **What it does**: Returns the `AsyncOpenAI` client, creating one if it doesn’t exist.
- **Why it’s used**: Ensures there’s always a client to make API calls.
- **Simple Example**: Like checking if you have a phone to call OpenAI, and getting one if not.
- **Schema**: Returns an `AsyncOpenAI` instance.
- ```python
  def _get_client(self) -> AsyncOpenAI
  ```

---

# RunContextWrapper Class Notes 

The `RunContextWrapper` dataclass is part of the OpenAI Agents SDK and acts like a **container** that holds your custom context (data you provide) and tracks usage information during an agent’s run. It’s designed to pass data to your tools, callbacks, or hooks without sending it to the language model (LLM). 


### **What It Is**
The `RunContextWrapper` is a Python dataclass that wraps the context object you pass to `Runner.run()`. It’s like a **lunchbox** that holds your custom data (context) and adds a note about how much the agent has "eaten" (usage) during its work.

### **Note**

It uses `Generic[TContext]`, which means it can work with any type of context you provide, like a dataclass, a Pydantic model, or even `None`. This makes it flexible for different use cases.

The context in `RunContextWrapper` is **not** sent to the LLM. It’s only for your code, such as tools, callbacks, or hooks, to use during the agent’s run.

---

## Attributes

#### **1. context**
- **What it does**: Holds the context object you pass to `Runner.run()` (or `None` if you don’t provide one).
- **Why it’s used**: Lets you share custom data, like a user’s name or settings, with your tools or hooks.
- **Simple Example**: If you pass a `UserInfo` object with `name="Ali"`, your tools can access `Ali` to personalize responses.
- **Type**: `TContext` (can be any type you define, or `None`).
- ```python
  context: TContext
  ```

#### **2. usage**
- **What it does**: Tracks how much the agent has used, like input/output tokens or requests.
- **Why it’s used**: Helps monitor the agent’s resource consumption, useful for debugging or cost tracking.
- **Simple Example**: Shows you used 50 input tokens and 20 output tokens after answering a question.
- **Type**: `Usage` (defaults to an empty `Usage` object created by `field(default_factory=Usage)`).
- **Note**: For streaming responses, `usage` is incomplete ("stale") until the final chunk is processed.
- ```python
  usage: Usage = field(default_factory=Usage)
  ```

---

## How It Works
When you run an agent with `Runner.run()`, the `RunContextWrapper` bundles your context object (e.g., user data) and tracks usage (e.g., tokens). This wrapped data is passed to your tools, hooks, or callbacks, so they can use it without sending it to the LLM. It’s like giving your tools a **notebook** with your custom info and a tally of the agent’s work.

### **Simple Example**
Imagine you’re building a chatbot that greets users by name and tracks how many tokens it uses.

```python
from dataclasses import dataclass
from agents import Agent, RunContextWrapper, Runner, function_tool

# Define a simple context with user info
@dataclass
class UserInfo:
    name: str

# Create a tool that uses the context
@function_tool
async def greet_user(wrapper: RunContextWrapper[UserInfo]) -> str:
    return f"Hello, {wrapper.context.name}! Usage so far: {wrapper.usage}"

# Main function to run the agent
async def main():
    # Create context with user info
    user_info = UserInfo(name="Ali")
    
    # Create an agent with the greeting tool
    agent = Agent[UserInfo](name="GreetBot", tools=[greet_user])
    
    # Run the agent with input and context
    result = await Runner.run(agent, "Say hello", context=user_info)
    
    # Print the final output
    print(result.final_output)  # Output: Hello, Ali! Usage so far: Usage(requests=1, input_tokens=..., output_tokens=...)

# Run the example
import asyncio
asyncio.run(main())
```

**Explanation**:
- The `UserInfo` context with `name="Ali"` is wrapped by `RunContextWrapper`.
- The `greet_user` tool accesses `wrapper.context.name` to get “Ali” and `wrapper.usage` to see token usage.
- The agent processes “Say hello” and returns a personalized greeting with usage details.

**Note**: If the response is streamed (e.g., live chat), the `usage` field may not be fully updated until the stream finishes.

---
# FunctionTool Class Notes

The `FunctionTool` dataclass is part of the OpenAI Agents SDK and represents a tool that wraps a Python function, allowing an agent to call it during a run. It’s like a **button** the agent can press to run your code, such as fetching weather data or calculating something. You typically create a `FunctionTool` using the `function_tool` helper, which simplifies wrapping a function. 

---

## FunctionTool Dataclass

### **What It Is**
The `FunctionTool` dataclass defines a tool that lets an agent run a specific Python function. It’s like a **remote control** that tells the agent what the function does, how to use it, and what input it expects, then runs the function when called.

### **Based On**
It’s a Python dataclass, making it easy to define and use with structured attributes.

### **Source**
Defined in the OpenAI Agents SDK (likely in a tools-related module, e.g., `src/agents/tools.py`).

### **Note**
You should usually use the `function_tool` helper to create a `FunctionTool`, as it simplifies wrapping a Python function and handles details like JSON schema generation.

---

## Attributes

#### **1. name**
- **What it does**: The name of the tool, shown to the LLM.
- **Why it’s used**: Helps the LLM identify the tool (usually matches the function name).
- **Simple Example**: If your function is `get_weather`, the tool name is “get_weather” so the LLM knows what to call.
- **Type**: `str`
- ```python
  name: str
  ```

#### **2. description**
- **What it does**: A description of what the tool does, shown to the LLM.
- **Why it’s used**: Tells the LLM the tool’s purpose, helping it decide when to use it.
- **Simple Example**: For a weather tool, the description might be “Fetches the current weather for a city.”
- **Type**: `str`
- ```python
  description: str
  ```

#### **3. params_json_schema**
- **What it does**: Defines the JSON schema for the tool’s input parameters.
- **Why it’s used**: Specifies the format and type of inputs the tool expects (e.g., a city name as a string).
- **Simple Example**: For a weather tool, the schema might say `{ "city": { "type": "string" } }` to expect a city name.
- **Type**: `dict[str, Any]`
- ```python
  params_json_schema: dict[str, Any]
  ```

#### **4. on_invoke_tool**
- **What it does**: A function that runs when the tool is called, taking a context and JSON parameters.
- **Why it’s used**: Executes the actual logic of the tool and returns a result as a string (or something convertible to a string).
- **Simple Example**: For a weather tool, it might take a city name and return “It’s sunny in London!” or an error message if it fails.
- **Type**: `Callable[[ToolContext[Any], str], Awaitable[Any]]`
- **Note**: You can raise an exception to fail the run or return a string error to let the LLM handle it.
- ```python
  on_invoke_tool: Callable[[ToolContext[Any], str], Awaitable[Any]]
  ```

#### **5. strict_json_schema**
- **What it does**: Decides if the JSON schema is strictly enforced.
- **Why it’s used**: Ensures the LLM provides correct input formats, reducing errors.
- **Simple Example**: If `True`, the LLM must send a valid city name; if `False`, it might accept invalid inputs.
- **Type**: `bool` (defaults to `True`)
- **Note**: Strongly recommended to set to `True` for reliable input validation.
- ```python
  strict_json_schema: bool = True
  ```

#### **6. is_enabled**
- **What it does**: Determines if the tool is available for use, either as a boolean or a function.
- **Why it’s used**: Lets you enable or disable the tool based on conditions, like user permissions or context.
- **Simple Example**: A weather tool might be disabled if the user isn’t in a premium plan, checked via a function.
- **Type**: `bool | Callable[[RunContextWrapper[Any], Agent[Any]], MaybeAwaitable[bool]]` (defaults to `True`)
- ```python
  is_enabled: bool | Callable[[RunContextWrapper[Any], Agent[Any]], MaybeAwaitable[bool]] = True
  ```

---

## How It Works
The `FunctionTool` dataclass wraps a Python function so an agent can call it during a run. It tells the LLM the tool’s name, purpose, and expected inputs (via JSON schema). When the LLM decides to use the tool, `on_invoke_tool` runs the function with the provided context and parameters, returning a result. The `is_enabled` attribute lets you control when the tool is available, and `strict_json_schema` ensures the inputs are valid.

### **Simple Example**
Imagine you’re building a chatbot that can fetch the weather for a city. You create a `FunctionTool` to handle this.

```python
from dataclasses import dataclass
from agents import Agent, Runner, function_tool, RunContextWrapper

# Define a context for user data
@dataclass
class UserInfo:
    city: str

# Create a weather tool using the function_tool decorator
@function_tool
async def get_weather(wrapper: RunContextWrapper[UserInfo], params: str) -> str:
    import json
    city = json.loads(params).get("city", wrapper.context.city)
    # Simulate fetching weather (replace with real API call)
    return f"It's sunny in {city}!"

# Main function to run the agent
async def main():
    # Create context with user info
    user_info = UserInfo(city="London")
    
    # Create an agent with the weather tool
    agent = Agent[UserInfo](name="WeatherBot", tools=[get_weather])
    
    # Run the agent with input
    result = await Runner.run(agent, "What's the weather?", context=user_info)
    
    # Print the final output
    print(result.final_output)  # Output: It's sunny in London!

# Run the example
import asyncio
asyncio.run(main())
```

**Explanation**:
- The `get_weather` function is wrapped as a `FunctionTool` using the `@function_tool` decorator, which sets the `name` (“get_weather”), `description`, and `params_json_schema` automatically.
- The tool expects a JSON string with a “city” parameter, but it can fall back to the `wrapper.context.city` (“London”).
- The `on_invoke_tool` function runs when the LLM calls the tool, returning “It’s sunny in London!”.
- The `is_enabled` defaults to `True`, so the tool is always available unless you add logic to disable it.
- The `strict_json_schema` ensures the LLM sends a valid city name.

**Note**: If the LLM sends invalid JSON (e.g., missing “city”), `strict_json_schema=True` helps catch the error early.

---

### @function_tool Decorator Notes

The `@function_tool` decorator is part of the OpenAI Agents SDK and is used to turn a Python function into a `FunctionTool` that an agent can use. It’s like a **wrapper** that packages your function so the agent’s language model (LLM) knows how to call it, what it does, and what inputs it expects. 

---

# function tool decorator

### **What It Is**
The `@function_tool` decorator transforms a Python function into a `FunctionTool`, which is a tool an agent can call during its run. It’s like turning a regular tool (your function) into a **smart tool** that the LLM understands by adding instructions, input rules, and error handling.

### **Based On**
It’s a Python decorator with two overloads: one for use without parentheses (`@function_tool`) and one with parentheses for customization (`@function_tool(...)`). It generates a `FunctionTool` dataclass.

### **Source**
Defined in the OpenAI Agents SDK (likely in a tools-related module, e.g., `src/agents/tools.py`).

### **Note**
The decorator automatically creates a JSON schema for the function’s parameters and uses its docstring for the tool’s description, making it easy to integrate with an agent.

---

## Parameters

#### **1. func**
- **What it does**: The Python function to wrap as a `FunctionTool`.
- **Why it’s used**: Defines the actual code the tool will run.
- **Simple Example**: A function like `get_weather` that fetches weather data.
- **Type**: `ToolFunction[...] | None` (optional, used when the decorator is called with parentheses).
- **Default**: `None` (for `@function_tool(...)` usage).

#### **2. name_override**
- **What it does**: Sets a custom name for the tool instead of using the function’s name.
- **Why it’s used**: Lets you give the tool a different name for the LLM to see.
- **Simple Example**: Rename `get_weather` to “weather_check” for clarity.
- **Type**: `str | None`
- **Default**: `None`

#### **3. description_override**
- **What it does**: Sets a custom description for the tool instead of using the function’s docstring.
- **Why it’s used**: Allows you to provide a specific description for the LLM.
- **Simple Example**: Describe `get_weather` as “Gets current weather for a city” instead of the docstring.
- **Type**: `str | None`
- **Default**: `None`

#### **4. docstring_style**
- **What it does**: Specifies the style of the function’s docstring (e.g., Google, NumPy).
- **Why it’s used**: Helps parse the docstring correctly to extract descriptions.
- **Simple Example**: Set to “Google” if your docstring follows Google’s format.
- **Type**: `DocstringStyle | None`
- **Default**: `None` (auto-detects the style).

#### **5. use_docstring_info**
- **What it does**: Decides whether to use the function’s docstring for the tool’s description and parameter details.
- **Why it’s used**: Automatically fills in the tool’s description and parameter info from the docstring.
- **Simple Example**: If `True`, uses `get_weather`’s docstring to describe the tool.
- **Type**: `bool`
- **Default**: `True`

#### **6. failure_error_function**
- **What it does**: A function to handle errors when the tool fails, returning a string message for the LLM.
- **Why it’s used**: Lets you customize error messages or raise an exception if set to `None`.
- **Simple Example**: If `get_weather` fails, return “Couldn’t fetch weather” instead of crashing.
- **Type**: `ToolErrorFunction | None`
- **Default**: `default_tool_error_function`

#### **7. strict_mode**
- **What it does**: Enables strict JSON schema validation for the tool’s inputs.
- **Why it’s used**: Ensures the LLM sends correct input formats, reducing errors.
- **Simple Example**: If `True`, requires a valid city name for `get_weather`.
- **Type**: `bool`
- **Default**: `True` (strongly recommended).

#### **8. is_enabled**
- **What it does**: Determines if the tool is available, either as a boolean or a function.
- **Why it’s used**: Lets you enable or disable the tool based on conditions, like user permissions.
- **Simple Example**: Disable `get_weather` if the user isn’t premium.
- **Type**: `bool | Callable[[RunContextWrapper[Any], Agent[Any]], MaybeAwaitable[bool]]`
- **Default**: `True`

---

## How It Works
The `@function_tool` decorator takes a Python function and turns it into a `FunctionTool` by:
1. **Parsing the function signature**: Creates a JSON schema for the tool’s parameters (e.g., a `city` string for `get_weather`).
2. **Using the docstring**: Extracts the tool’s description and parameter details (unless overridden).
3. **Handling invocation**: Wraps the function in an `on_invoke_tool` method that validates inputs and runs the function.
4. **Managing errors**: Uses `failure_error_function` to handle errors gracefully or raise exceptions.
5. **Controlling availability**: Uses `is_enabled` to decide if the tool is visible to the LLM.

It supports two usage styles:
- **Without parentheses** (`@function_tool`): Uses default settings and the function’s name/docstring.
- **With parentheses** (`@function_tool(name_override="custom_name")`): Allows customization of name, description, etc.

The decorator ensures the function works with the agent’s context (e.g., `RunContextWrapper`) if it takes one as its first argument.

### **Simple Example**
Imagine you’re building a chatbot that fetches weather data for a city.

```python
from dataclasses import dataclass
from agents import Agent, Runner, RunContextWrapper, function_tool
import json

# Define a context for user data
@dataclass
class UserInfo:
    city: str

# Create a weather tool with the function_tool decorator
@function_tool(description_override="Gets current weather for a city")
async def get_weather(wrapper: RunContextWrapper[UserInfo], params: str) -> str:
    """Fetch weather for a city.
    
    Args:
        city (str): The city to get weather for.
    """
    city = json.loads(params).get("city", wrapper.context.city)
    # Simulate fetching weather (replace with real API call)
    return f"It's sunny in {city}!"

# Main function to run the agent
async def main():
    # Create context with user info
    user_info = UserInfo(city="London")
    
    # Create an agent with the weather tool
    agent = Agent[UserInfo](name="WeatherBot", tools=[get_weather])
    
    # Run the agent with input
    result = await Runner.run(agent, "What's the weather in London?", context=user_info)
    
    # Print the final output
    print(result.final_output)  # Output: It's sunny in London!

# Run the example
import asyncio
asyncio.run(main())
```

**Explanation**:
- The `@function_tool` decorator wraps `get_weather`, creating a `FunctionTool` with:
  - `name`: “get_weather” (from the function name).
  - `description`: “Gets current weather for a city” (from `description_override`).
  - `params_json_schema`: Generated from the function’s signature and docstring, expecting a `city` parameter.
- The `on_invoke_tool` function:
  - Parses the JSON input (e.g., `{"city": "London"}`) or uses the context’s city.
  - Runs `get_weather` with the `RunContextWrapper` and parameters.
  - Returns the result (“It’s sunny in London!”).
- `strict_mode=True` ensures the LLM sends valid JSON (e.g., a proper city name).
- `is_enabled=True` makes the tool always available.

**Error Handling**:
- If the LLM sends invalid JSON, a `ModelBehaviorError` is raised.
- If the function fails and `failure_error_function` is set, it returns an error message to the LLM; otherwise, it raises an exception.

---
### InputGuardrail Dataclass and @input_guardrail Decorator Notes 

The `InputGuardrail` dataclass and `@input_guardrail` decorator are part of the OpenAI Agents SDK. They help you check or control the input an agent receives before it processes it. Think of `InputGuardrail` as a **gatekeeper** who inspects incoming messages to ensure they’re appropriate, and `@input_guardrail` as a tool to easily create one.

---

# InputGuardrail Class Notes

### **What It Is**
The `InputGuardrail` dataclass defines a check that runs alongside an agent’s execution to validate or control input (e.g., user messages). It’s like a **security guard** who checks if a visitor’s request is safe before letting it through.

### **Based On**
Uses `Generic[TContext]` to work with any context type (e.g., dataclass, Pydantic model, or `None`).

### **Source**
Defined in the OpenAI Agents SDK (likely in a guardrail-related module, e.g., `src/agents/guardrails.py`).

### **Note**
If the guardrail’s `tripwire_triggered` is `True`, the agent stops immediately, and an `InputGuardrailTripwireTriggered` exception is raised.

---

### **Attributes**

#### **1. guardrail_function**
- **What it does**: A function that checks the input and returns a `GuardrailResult`.
- **Why it’s used**: Runs the logic to validate or act on the input, deciding if it’s allowed.
- **Simple Example**: Checks if a message is off-topic (e.g., “Buy shoes” for a weather bot) and blocks it.
- **Type**: `Callable[[RunContextWrapper[TContext], Agent[Any], str | list[TResponseInputItem]], MaybeAwaitable[GuardrailFunctionOutput]]`
- ```python
  guardrail_function: Callable[[RunContextWrapper[TContext], Agent[Any], str | list[TResponseInputItem]], MaybeAwaitable[GuardrailFunctionOutput]]
  ```

#### **2. name**
- **What it does**: The name of the guardrail, used for tracing.
- **Why it’s used**: Identifies the guardrail in logs or debugging.
- **Simple Example**: Name it “topic_check” to track a guardrail that checks for off-topic inputs.
- **Type**: `str | None` (defaults to the function’s name if `None`).
- ```python
  name: str | None = None
  ```

---

### **Methods**

#### **1. get_name**
- **What it does**: Returns the guardrail’s name, using the provided `name` or the function’s name.
- **Why it’s used**: Ensures a name is available for tracing or logging.
- **Simple Example**: Returns “topic_check” if set, or “check_topic” from the function name.
- **Schema**: Returns a `str`.
- ```python
  def get_name(self) -> str
  ```

#### **2. run**
- **What it does**: Runs the guardrail function on the input and returns an `InputGuardrailResult`.
- **Why it’s used**: Executes the guardrail check and handles sync or async functions.
- **Simple Example**: Checks if “Buy shoes” is valid for a weather bot and returns a result.
- **Schema**: Takes an agent, input, and context, returning an `InputGuardrailResult`.
- ```python
  async def run(
      self,
      agent: Agent[Any],
      input: str | list[TResponseInputItem],
      context: RunContextWrapper[TContext]
  ) -> InputGuardrailResult
  ```

---

# input guardrail decorator

### **What It Is**
The `@input_guardrail` decorator turns a sync or async function into an `InputGuardrail`. It’s like a **shortcut** to create a guardrail by wrapping a function that checks inputs.

### **Based On**
A Python decorator with three overloads: for sync functions, async functions, and usage with keyword arguments (e.g., `@input_guardrail(name="custom_name")`).

### **Source**
Defined in the OpenAI Agents SDK (likely in `src/agents/guardrails.py`).

### **Note**
Can be used without parentheses (`@input_guardrail`) or with customization (`@input_guardrail(name="custom_name")`).

---

### **Parameters**

#### **1. func**
- **What it does**: The function to turn into an `InputGuardrail`.
- **Why it’s used**: Defines the logic for checking inputs.
- **Simple Example**: A function that checks if a message is about weather.
- **Type**: `_InputGuardrailFuncSync[TContext_co] | _InputGuardrailFuncAsync[TContext_co] | None`
- **Default**: `None` (for `@input_guardrail(name="...")` usage).

#### **2. name**
- **What it does**: Sets a custom name for the guardrail.
- **Why it’s used**: Overrides the function’s name for tracing or logging.
- **Simple Example**: Name the guardrail “topic_check” instead of the function’s name.
- **Type**: `str | None`
- **Default**: `None`

---

### **How It Works**
The `@input_guardrail` decorator wraps a function to create an `InputGuardrail`. The function receives:
- A `RunContextWrapper[TContext]` (context data, e.g., user info).
- An `Agent[Any]` (the agent running the task).
- Input as a `str` or `list[TResponseInputItem]` (the user’s message).

It returns a `GuardrailFunctionOutput`, which indicates if the `tripwire_triggered` is `True` (stop the agent) or `False` (allow it to continue). The decorator supports both sync and async functions and handles them appropriately.

### **Simple Example**
Imagine a weather bot that should only respond to weather-related questions.

```python
from dataclasses import dataclass
from agents import Agent, Runner, RunContextWrapper, input_guardrail, GuardrailFunctionOutput

# Define a context
@dataclass
class UserInfo:
    user_id: str

# Create an input guardrail to check for weather-related input
@input_guardrail(name="weather_topic_check")
async def check_topic(
    context: RunContextWrapper[UserInfo],
    agent: Agent[Any],
    input: str | list
) -> GuardrailFunctionOutput:
    if isinstance(input, str) and "weather" not in input.lower():
        return GuardrailFunctionOutput(tripwire_triggered=True, message="Input must be about weather")
    return GuardrailFunctionOutput(tripwire_triggered=False)

# Main function to run the agent
async def main():
    # Create context
    user_info = UserInfo(user_id="123")
    
    # Create an agent with the guardrail
    agent = Agent[UserInfo](name="WeatherBot", input_guardrails=[check_topic])
    
    # Try an off-topic input
    try:
        result = await Runner.run(agent, "Buy shoes", context=user_info)
    except InputGuardrailTripwireTriggered as e:
        print(f"Guardrail stopped execution: {e}")  # Output: Guardrail stopped execution: Input must be about weather
    
    # Try a valid input
    result = await Runner.run(agent, "What's the weather?", context=user_info)
    print(result.final_output)  # Output: [weather response]

# Run the example
import asyncio
asyncio.run(main())
```

**Explanation**:
- The `@input_guardrail` decorator wraps `check_topic` to create an `InputGuardrail` named “weather_topic_check”.
- The `check_topic` function checks if “weather” is in the input string. If not, it triggers the tripwire, stopping the agent.
- The `InputGuardrailTripwireTriggered` exception is raised for “Buy shoes”, but “What’s the weather?” passes.

---

# OutputGuardrail Class Notes

### **What It Is**
The `OutputGuardrail` dataclass defines a check that runs on an agent’s final output to validate it. It’s like a **quality inspector** who checks the agent’s response before it’s sent back to the user.

### **Based On**
Uses `Generic[TContext]` to work with any context type.

### **Source**
Defined in the OpenAI Agents SDK (likely in `src/agents/guardrails.py`).

### **Note**
If the guardrail’s `tripwire_triggered` is `True`, an `OutputGuardrailTripwireTriggered` exception is raised, stopping the response from being returned.

---

### **Attributes**

#### **1. guardrail_function**
- **What it does**: A function that checks the agent’s output and returns a `GuardrailResult`.
- **Why it’s used**: Validates the final output, ensuring it meets criteria (e.g., no profanity).
- **Simple Example**: Checks if the output contains inappropriate words and blocks it.
- **Type**: `Callable[[RunContextWrapper[TContext], Agent[Any], Any], MaybeAwaitable[GuardrailFunctionOutput]]`
- ```python
  guardrail_function: Callable[[RunContextWrapper[TContext], Agent[Any], Any], MaybeAwaitable[GuardrailFunctionOutput]]
  ```

#### **2. name**
- **What it does**: The name of the guardrail, used for tracing.
- **Why it’s used**: Identifies the guardrail in logs or debugging.
- **Simple Example**: Name it “profanity_check” for a guardrail that checks output language.
- **Type**: `str | None` (defaults to the function’s name if `None`).
- ```python
  name: str | None = None
  ```

---

### **Methods**

#### **1. get_name**
- **What it does**: Returns the guardrail’s name, using the provided `name` or the function’s name.
- **Why it’s used**: Ensures a name is available for tracing or logging.
- **Simple Example**: Returns “profanity_check” if set, or “check_profanity” from the function name.
- **Schema**: Returns a `str`.
- ```python
  def get_name(self) -> str
  ```

#### **2. run**
- **What it does**: Runs the guardrail function on the agent’s output and returns an `OutputGuardrailResult`.
- **Why it’s used**: Executes the output validation and handles sync or async functions.
- **Simple Example**: Checks if the output “It’s sunny!” is appropriate and allows it.
- **Schema**: Takes a context, agent, and output, returning an `OutputGuardrailResult`.
- ```python
  async def run(
      self,
      context: RunContextWrapper[TContext],
      agent: Agent[Any],
      agent_output: Any
  ) -> OutputGuardrailResult
  ```

---

# output guardrail decorator

### **What It Is**
The `@output_guardrail` decorator turns a sync or async function into an `OutputGuardrail`. It’s like a **shortcut** to create a guardrail that validates an agent’s output.

### **Based On**
A Python decorator with three overloads: for sync functions, async functions, and usage with keyword arguments (e.g., `@output_guardrail(name="custom_name")`).

### **Source**
Defined in the OpenAI Agents SDK (likely in `src/agents/guardrails.py`).

### **Note**
Can be used without parentheses (`@output_guardrail`) or with customization (`@output_guardrail(name="custom_name")`).

---

### **Parameters**

#### **1. func**
- **What it does**: The function to turn into an `OutputGuardrail`.
- **Why it’s used**: Defines the logic for checking outputs.
- **Simple Example**: A function that checks for inappropriate words in the output.
- **Type**: `_OutputGuardrailFuncSync[TContext_co] | _OutputGuardrailFuncAsync[TContext_co] | None`
- **Default**: `None` (for `@output_guardrail(name="...")` usage).

#### **2. name**
- **What it does**: Sets a custom name for the guardrail.
- **Why it’s used**: Overrides the function’s name for tracing or logging.
- **Simple Example**: Name the guardrail “profanity_check” instead of the function’s name.
- **Type**: `str | None`
- **Default**: `None`

---

### **How It Works**
The `@output_guardrail` decorator wraps a function to create an `OutputGuardrail`. The function receives:
- A `RunContextWrapper[TContext]` (context data, e.g., user info).
- An `Agent[Any]` (the agent that produced the output).
- The agent’s output as `Any` (the final response).

It returns a `GuardrailFunctionOutput`, which indicates if the `tripwire_triggered` is `True` (block the output) or `False` (allow it). The decorator supports both sync and async functions.

### **Simple Example**
Imagine a chatbot that shouldn’t use inappropriate words in its responses.

```python
from dataclasses import dataclass
from agents import Agent, Runner, RunContextWrapper, output_guardrail, GuardrailFunctionOutput

# Define a context
@dataclass
class UserInfo:
    user_id: str

# Create an output guardrail to check for inappropriate words
@output_guardrail(name="profanity_check")
async def check_profanity(
    context: RunContextWrapper[UserInfo],
    agent: Agent[Any],
    output: Any
) -> GuardrailFunctionOutput:
    inappropriate_words = ["bad", "rude"]
    if isinstance(output, str) and any(word in output.lower() for word in inappropriate_words):
        return GuardrailFunctionOutput(tripwire_triggered=True, message="Inappropriate words detected")
    return GuardrailFunctionOutput(tripwire_triggered=False)

# Main function to run the agent
async def main():
    # Create context
    user_info = UserInfo(user_id="123")
    
    # Create an agent with the guardrail
    agent = Agent[UserInfo](name="ChatBot", output_guardrails=[check_profanity])
    
    # Try an inappropriate output (simulated)
    try:
        result = await Runner.run(agent, "Say something bad", context=user_info)
    except OutputGuardrailTripwireTriggered as e:
        print(f"Guardrail stopped execution: {e}")  # Output: Guardrail stopped execution: Inappropriate words detected
    
    # Try a valid input
    result = await Runner.run(agent, "Say something nice", context=user_info)
    print(result.final_output)  # Output: [nice response]

# Run the example
import asyncio
asyncio.run(main())
```

**Explanation**:
- The `@output_guardrail` decorator wraps `check_profanity` to create an `OutputGuardrail` named “profanity_check”.
- The `check_profanity` function checks if the output contains words like “bad”. If it does, it triggers the tripwire, stopping the response.
- The `OutputGuardrailTripwireTriggered` exception is raised for “Say something bad”, but “Say something nice” passes.

---
