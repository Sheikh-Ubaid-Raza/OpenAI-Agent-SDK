from agents import Agent, Runner, RunContextWrapper, function_tool, enable_verbose_stdout_logging
from config import my_config
from pydantic import BaseModel

# enable_verbose_stdout_logging()

class UserDetails(BaseModel):
    name: str
    age:int
    password:int

    def dispdlay_user_info(self):
        print(f"User nanme is {self.name}, age is {self.age}, and password is {self.password}")

user = UserDetails(name="Ubaid",age=17, password=2468)   # Object


# ctx: RunContextWrapper[UserDetails] = RunContextWrapper(
#     context=user
# )
# print(ctx.context)

@function_tool
def get_name(wrapper:RunContextWrapper[UserDetails]) -> str:
    """Fetch the name of the user"""
    return f"The User name is {wrapper.context.name} and age is {wrapper.context.age}"

@function_tool
def get_age(wrapper:RunContextWrapper[UserDetails]) -> int:
    """Fetch the age of the user"""
    return f"The User age is {wrapper.context.age}."

@function_tool
def display_user_details(wrapper:RunContextWrapper[UserDetails]) -> str:
    """Fetch the user details"""
    return wrapper.context.dispdlay_user_info()


agent = Agent[UserDetails](
    name="Personal Assistant", 
    instructions="You are a helpful personal assistant",
    tools=[get_name,get_age, display_user_details]
)

response = Runner.run_sync(
    starting_agent=agent, 
    input="What is age of user?", 
    run_config=my_config,
    context=user
)

print(response.final_output)