from textwrap import dedent

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel

from launchr.interview import Interview
from launchr.llm import GPT4o

llm = GPT4o()


class Summary(BaseModel):
    idea: str
    hypotheses: list[str]
    summary: str


def generate_overall_summary(idea: str, interviews: list[Interview]) -> Summary:
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


def generate_idea_hypothesis(idea: str) -> str:
    """Generate a summary of the idea."""

    prompt = dedent(f"""
    You are given a brief description of a business idea:

    {idea}

    Turn this into a hypothesis statement in the form "We assume that <people> have a problem with <problem>. We beliece that by building <details_of_solution> will solve this problem by <solution_steps>.
    """).strip()

    idea_summary = (
        (SystemMessage(content="") + HumanMessage(content=prompt))
        | llm
        | StrOutputParser()
    ).invoke({})

    return idea_summary
