from pydantic import BaseModel


class Persona(BaseModel):
    title: str
    persona: str


def generate_personas(input_text: str) -> list[Persona]:
    """Generate personas from input text.

    Args:
        input_text: The input text to generate personas from.

    Returns:
        A list of Persona objects.
        Example:
            [
                Persona(title="Sales Manager", persona="Experienced sales professional managing a team of 10"),
                Persona(title="Sales Representative", persona="Entry-level sales person focused on outbound calls"),
            ]
    """
    dummy_return = [
        Persona(
            title="Sales Manager",
            persona="Experienced sales professional managing a team of 10",
        ),
        Persona(
            title="Sales Representative",
            persona="Entry-level sales person focused on outbound calls",
        ),
    ]
    return dummy_return
