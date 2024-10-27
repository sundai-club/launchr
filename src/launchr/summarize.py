from pydantic import BaseModel

from launchr.interview import Interview


class Summary(BaseModel):
    idea: str
    hypotheses: list[str]
    summary: str


def generate_summary(idea: str, interviews: list[Interview]) -> Summary:
    """Generate a summary of the interviews.

    Args:
        idea: The business idea or context to generate a summary for.
        interviews: The interviews to generate a summary for.

        Example:
            [
                Interview(
                    persona=Persona(
                        title="Sales Manager",
                        description="Experienced sales professional managing a team of 10",
                    ),
                    interview="What are the main challenges you face in your role?",
                    joys=[
                        Moment(
                            title="Deal Closing",
                            description="The thrill and satisfaction of closing sales deals",
                            quote="I love the challenge of closing deals",
                        )
                    ],
                    pains=[Moment(title="Time Management", description="Difficulty balancing multiple responsibilities and priorities", quote="I struggle with time management")],
                ),
                Interview(
                    persona=Persona(
                        title="Sales Representative",
                        description="Entry-level sales person focused on outbound calls",
                    ),
                    interview="What are the main challenges you face in your role?",
                    joys=[
                        Moment(
                            title="Deal Closing",
                            description="The thrill and satisfaction of closing sales deals",
                            quote="I love the challenge of closing deals",
                        )
                    ],
                    pains=[Moment(title="Time Management", description="Difficulty balancing multiple responsibilities and priorities", quote="I struggle with time management")],
                ),
            ]

    Returns:
        A Summary object containing the idea, hypotheses, and summary.

        Example:
            Summary(
                idea="CRM software for small businesses",
                hypotheses=[
                    "CRM software will help sales teams manage their pipeline and close deals faster",
                    "CRM software will help sales teams understand their customers and close deals faster",
                ],
                summary="The interviews revealed that sales teams face challenges in time management and pipeline tracking. The proposed solution is a CRM software that automates lead capture and pipeline management, freeing up time for salespeople to focus on closing deals."
            )
    """
    dummy_return = Summary(
        idea="CRM software for small businesses",
        hypotheses=[
            "CRM software will help sales teams manage their pipeline and close deals faster",
            "CRM software will help sales teams understand their customers and close deals faster",
        ],
        summary="The interviews revealed that sales teams face challenges in time management and pipeline tracking. The proposed solution is a CRM software that automates lead capture and pipeline management, freeing up time for salespeople to focus on closing deals.",
    )
    return dummy_return
