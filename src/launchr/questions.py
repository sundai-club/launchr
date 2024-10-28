from textwrap import dedent

from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import BaseModel, Field

from launchr.llm import default_llm
from launchr.personas import PersonaList


class QuestionsList(BaseModel):
    questions: list[str] = Field(description="A list of questions")


llm = default_llm

def generate_questions(personas: PersonaList, num_questions: int = 10) -> list[str]:
    """Generate questions for a given idea and sample personas.

    Args:
        personas: A PersonaList object containing the business idea and a list of Persona objects.
            Example:
            PersonaList(
                idea="CRM software for small businesses",
                personas=[
                    Persona(title="Sales Manager", description="Experienced sales professional managing a team of 10"),
                ]
            )

    Returns:
        A list of 10 questions.

        Example:
        [
            "What are the biggest pain points you face in your current role?", # augment the questions into: "When was this a problem for you? Tell me more about that." ACTION
            "What are the biggest pain points you face in your current role?",
            "What are the biggest pain points you face in your current role?",
        ]
    """
    personas_json = personas.model_dump_json(indent=4)

    prompt = dedent(f"""
        You are a world-class product manager.

        You are given a business idea and a list of sample personas:
        
        ```
        {personas_json}
        ```

        Generate {num_questions} questions that you would ask to validate the business idea with the personas. Keep the questions concise and to the point, and relevant to the business idea and personas.
        """).strip()

    questions_result: QuestionsList = (
        (SystemMessage(content="") + HumanMessage(content=prompt))
        | llm.with_structured_output(QuestionsList)
    ).invoke({})

    return questions_result.questions
