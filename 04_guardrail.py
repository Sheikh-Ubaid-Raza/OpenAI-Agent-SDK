from agents import (
    Agent, 
    GuardrailFunctionOutput, 
    RunContextWrapper, 
    Runner, 
    InputGuardrailTripwireTriggered, 
    enable_verbose_stdout_logging, 
    TResponseInputItem, 
    input_guardrail
)

from pydantic import BaseModel
from config import my_config, gemini_model

# enable_verbose_stdout_logging()

class HomeworkCheatDetectionOutput(BaseModel):
    attempting_cheat: bool
    explanation: str

homework_cheat_guardrail_agent = Agent(
    name="Homework Cheat Detector",
    instructions=(
        "Determine if the user's query resembles a typical homework assignment or exam question, indicating an attempt to cheat. General questions about concepts are acceptable. "
        " Cheating: 'Fill in the blank: The capital of France is ____.',"
        " 'Which of the following best describes photosynthesis? A) Cellular respiration B) Conversion of light energy C) Evaporation D) Fermentation.'"
        " Not-Cheating: 'What is the capital of France?', 'Explain photosynthesis.'"
    ),
    output_type=HomeworkCheatDetectionOutput,
    model=gemini_model
)

@input_guardrail
async def cheat_detection_guardrail(
        ctx: RunContextWrapper[None], agent: Agent, input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput :
    
    detection_result = await Runner.run(homework_cheat_guardrail_agent, input)

    return GuardrailFunctionOutput(
        tripwire_triggered=detection_result.final_output.attempting_cheat,
        output_info=detection_result.final_output
    )

study_helper_agent = Agent(
    name="Study Helper Agent",
    instructions="You assist users in studying by explaining concepts or providing guidance, without directly solving homework or test questions.",
    model=gemini_model,
    input_guardrails=[cheat_detection_guardrail]
)

# This should trigger the cheat detection guardrail

try:
    response = Runner.run_sync(study_helper_agent, "Father of Zoology is ____ .", run_config=my_config)
    print("Guardrail didn't trigger")
    print("Response: ", response.final_output)

except InputGuardrailTripwireTriggered as e:
    print("Homework cheat guardrail triggered")
    print("Exception details:", str(e))

