from agents import Agent, GuardrailFunctionOutput, Runner,InputGuardrailTripwireTriggered, input_guardrail, enable_verbose_stdout_logging
from pydantic import BaseModel
import asyncio
from config import my_config, gemini_model

enable_verbose_stdout_logging()

class HomeworkOutput(BaseModel):
    is_homework: bool
    reasoning: str

guardrail_agent = Agent(
    name="Guardrail check",
    instructions="Check if the user is asking about homework.",
    output_type=HomeworkOutput,
    model=gemini_model
)

math_tutor_agent = Agent(
    name="Math Tutor",
    handoff_description="Specialist agent for math questions",
    instructions="You provide help with math problems. Explain your reasoning at each step and include examples",
)

history_tutor_agent = Agent(
    name="History Tutor",
    handoff_description="Specialist agent for historical questions",
    instructions="You provide assistance with historical queries. Explain important events and context clearly.",
)

@input_guardrail
async def homework_guardrail(ctx, agent, input_data) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrail_agent, input_data, context=ctx.context)
    final_output = result.final_output_as(HomeworkOutput)
    return GuardrailFunctionOutput(
        output_info=final_output,
        tripwire_triggered=not final_output.is_homework,
    )

triage_agent = Agent(
    name="Triage Agent",
    instructions="You determine which agent to use based on the user's homework question",
    handoffs=[history_tutor_agent, math_tutor_agent],
    input_guardrails=[homework_guardrail],
    model=gemini_model
)

async def main():

    try:
        result = await Runner.run(triage_agent, "Who was the first president of USA?", run_config=my_config)
        print("\nGuardrail Did Not Trigger")
        print(result.final_output)
    except InputGuardrailTripwireTriggered as e:
        print("\nGuardrail Trigger")
        print("Exception details:", str(e))


if __name__ == "__main__":
    asyncio.run(main())