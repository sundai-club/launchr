from pydantic import BaseModel


class Persona(BaseModel):
    title: str
    description: str


class PersonaList(BaseModel):
    idea: str
    personas: list[Persona]


def generate_personas(idea: str) -> PersonaList:
    """Generate personas from input text.

    Args:
        idea: The business idea or context to generate personas from.

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
    dummy_return = PersonaList(
        idea="Dummy Idea",
        personas=[
            Persona(
                title="Sales Manager",
                description="Experienced sales professional managing a team of 10",
            ),
            Persona(
                title="Sales Representative",
                description="Entry-level sales person focused on outbound calls",
            ),
        ],
    )
    return dummy_return
