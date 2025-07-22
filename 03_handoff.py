from agents import Agent, Runner, enable_verbose_stdout_logging
from config import my_config

enable_verbose_stdout_logging()

botany_tutor = Agent(
    name="Botany Tutor",
    instructions="You are a botany tutor agent.",
    handoff_description="Specialist agent for botany questions"
)

zoology_tutor = Agent(
    name="Zoology Tutor",
    instructions="You are a zoology tutor agent.",
    handoff_description="Specialist agent for zoology questions"
)

biology_agent = Agent(
    name="Tutor Assistant", 
    instructions="You are a helpful tutor assistant.",
    handoffs=[botany_tutor, zoology_tutor]
)
response = Runner.run_sync(
    biology_agent, 
    "Write some examples of carnivorous plants?", 
    run_config=my_config
)

print(response.final_output)