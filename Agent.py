from agents import Agent, Runner, RunContextWrapper, enable_verbose_stdout_logging
from config import my_config, gemini_model
from dataclasses import dataclass
# enable_verbose_stdout_logging()

@dataclass
class UserDetails:
    name: str
    interest: str

user = UserDetails(name="Ubaid", interest="BSN")

async def custom_instruction(wrapper: RunContextWrapper[UserDetails], agent:Agent) -> str:
    return f"You are {wrapper.context.name} assistant, guide him according to his {wrapper.context.interest}"

agent = Agent[UserDetails](
    name="AI Assistant",
    instructions=custom_instruction
)

response = Runner.run_sync(
    starting_agent=agent,
    input="Whose assistant are you?",
    run_config=my_config,
    context=user
)

print(response.final_output)