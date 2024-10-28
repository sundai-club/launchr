from textwrap import dedent

from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import BaseModel

from launchr.llm import default_llm

llm = default_llm


class Persona(BaseModel):
    title: str
    description: str


class PersonaList(BaseModel):
    idea: str
    personas: list[Persona]


def generate_personas(
    idea: str, initial_personas: str, num_personas: int = 5
) -> PersonaList:
    """Generate personas from input text.

    Args:
        idea: The business idea or context to generate personas from.
        sample_personas: A string of sample personas to use as a starting point.

    Returns:
        A PersonaList object containing the business idea and a list of Persona objects.

        Example:
            PersonaList(
                idea="CRM software for small businesses",
                personas=[
                    Persona(title="Sales Manager", description="Experienced sales professional managing a team of 10"),
                    Persona(title="Sales Representative", description="Entry-level sales person focused on outbound calls"),
                ]
            )
    """

    prompt = dedent(f"""
        You are generating personas for the following business idea:

        ```
        {idea}
        ```

        You are also given the following sample personas:

        ```
        {initial_personas}
        ```

        Consider the following types of personalities, but only if it makes sense: 

        - Modern Bourgeoisie
        - Upwardly Mobile
        - Post-Materialists
        - New Conservatives
        - Traditional Bourgeoisie
        - Cosmopolitans
        - Postmodern Hedonists
        - Convenience-Oriented

        Generate an additional {num_personas} personas that are relevant to the business idea. Make them full personal profiles with a name, age, gender, location, and a description of their role and interests, as well as any other details relevant to the business idea. Add details on their incentives and career goals, as well as their approach to proplem solving and their approach to adopting new technologies and solutions. For new personals, include the types of information that are present in the sample personas. Return the new personas in addition to the original ones. Add information to the initial personas if needed to make them more specific to the business idea.
        """).strip()

    personas_list: PersonaList = (
        (SystemMessage(content="") + HumanMessage(content=prompt))
        | llm.with_structured_output(PersonaList)
    ).invoke({})

    return personas_list
