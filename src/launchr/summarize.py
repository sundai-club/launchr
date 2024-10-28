from textwrap import dedent

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

from launchr.interview import Interview
from launchr.llm import default_llm

llm = default_llm


def generate_overall_summary(idea: str, interviews: list[Interview]) -> str:
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
    prompt = dedent(f"""
        Imagine you are a seasoned synthesis expert with extensive experience in user insights and cross-functional collaboration. Your background in qualitative analysis and strategy allows you to distill complex information into clear, actionable insights tailored for a product development team. You are collaborating with a cross-functional team that includes go-to-market specialists, product managers, and full-stack engineers. They've conducted a series of interviews to uncover user needs and challenges in a specific market. Your task is to synthesize these insights, focusing on the most relevant findings to help the team refine and iterate on product solutions effectively.
                    
        This is the idea you are synthesizing for:

        ```
        {idea}
        ```

        This is the list of interviews you are synthesizing:

        ```
        {interviews}
        ```
                    
        Please organize the synthesis according to the following categories. Be concise in your analysis and focus on delivering meaningful insights in a quick, digestible format. Please pull quotes where it seems appropriate to supplement our understanding. Do not provide any introduction to this text or conclusion after this text - please just fill out the relevant section below according to the instructions provided.

        Summary: Provide a high-level overview of the major insights drawn from the interviews, focusing on the critical themes, patterns, and observations that most significantly impact user experience. This should frame the team's understanding of the problems and allow them to think through this lens to build a solution.

        Process Overview: Outline the typical user journey or workflow described in the interviews, with attention to any key steps or decision points. Use a numerical format for each step. Do not use titles - just provide a description of the process at each step, so that it's an easy to read list.

        Pain Points: List and elaborate on specific pain points that users encounter. Include context where applicable, noting any recurring patterns, strong reactions, or frustrations that emerged consistently across interviews. Highlight which step each of these pain points corresponds to in the process above.

        Likes: Identify the aspects of the current product or process that users found valuable or enjoyable. Highlight these positive elements as potential strengths for future iterations or as features to maintain. We need to design our product to allow users to continue to do what they really enjoy. Highlight which step each of these likes corresponds to in the process above.

        Hypotheses for Product Solutions: Based on user feedback, propose hypotheses on themes to explore or initial concepts for product solutions that could address the key pain points. Ensure these ideas are clear, practical, and aligned with current resources, providing actionable starting points for the product team to test and refine. Explain why each was chosen and how it relates to the pain points we've found.
                    
        Format the response as Markdown.
    """).strip()

    summary = (
        (SystemMessage(content="") + HumanMessage(content=prompt))
        | llm
        | StrOutputParser()
    ).invoke({})

    return summary


def generate_idea_hypothesis(idea: str) -> str:
    """Generate a summary of the idea."""

    prompt = dedent(f"""
    You are given a brief description of a business idea:

    {idea}

    Turn this into a hypothesis statement in the form "We hypothesize that <people> have a problem with <problem>. We believe that by building <details_of_solution> will solve this problem by <solution_steps>.
    """).strip()

    idea_summary = (
        (SystemMessage(content="") + HumanMessage(content=prompt))
        | llm
        | StrOutputParser()
    ).invoke({})

    return idea_summary
