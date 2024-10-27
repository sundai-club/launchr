from pydantic import BaseModel

from launchr.personas import Persona


class Moment(BaseModel):
    title: str
    description: str
    quote: str


class Interview(BaseModel):
    persona: Persona
    interview: str
    joys: list[Moment]
    pains: list[Moment]


def generate_interview(idea: str, persona: Persona) -> Interview:
    """Generate an interview for a persona.

    Args:
        idea: The business idea or context to generate an interview for.

        persona: The persona to generate an interview for.

            Example:
                Persona(
                    title="Sales Manager",
                    description="Experienced sales professional managing a team of 10",
                )

    Returns:
        An Interview object containing the persona, interview, joys, and pains.

        Example:
            Interview(
                persona=Persona(title="Sales Manager", description="Experienced sales professional managing a team of 10"),
                interview="What are the main challenges you face in your role?",
                joys=[
                    Moment(
                        title="Deal Closing",
                        description="The thrill and satisfaction of closing sales deals",
                        quote="I love the challenge of closing deals"
                    ),
                    Moment(
                        title="Team Leadership",
                        description="Satisfaction from leading and developing team members",
                        quote="I enjoy leading a team"
                    )
                ],
                pains=[
                    Moment(
                        title="Time Management",
                        description="Difficulty balancing multiple responsibilities and priorities",
                        quote="I struggle with time management"
                    ),
                    Moment(
                        title="Pipeline Tracking",
                        description="Challenges in maintaining visibility of sales opportunities",
                        quote="I find it difficult to keep track of my sales pipeline"
                    )
                ]
            )
    """

    dummy_return = Interview(
        persona=persona,
        interview="What are the main challenges you face in your role?",
        joys=[
            Moment(
                title="Deal Closing",
                description="The thrill and satisfaction of closing sales deals",
                quote="I love the challenge of closing deals",
            ),
            Moment(
                title="Team Leadership",
                description="Satisfaction from leading and developing team members",
                quote="I enjoy leading a team",
            ),
        ],
        pains=[
            Moment(
                title="Time Management",
                description="Difficulty balancing multiple responsibilities and priorities",
                quote="I struggle with time management",
            ),
            Moment(
                title="Pipeline Tracking",
                description="Challenges in maintaining visibility of sales opportunities",
                quote="I find it difficult to keep track of my sales pipeline",
            ),
        ],
    )
    return dummy_return
