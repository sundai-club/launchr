from textwrap import dedent

from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import BaseModel, Field

from launchr.llm import default_llm
from launchr.personas import Persona

llm = default_llm


class Moment(BaseModel):
    title: str
    description: str
    quote: str


class Interview(BaseModel):
    persona: Persona = Field(description="The persona being interviewed")
    observations: str = Field(description="Observations from the day")
    joys: list[Moment] = Field(description="List of joys from the day")
    pains: list[Moment] = Field(description="List of pains from the day")


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

    prompt = dedent(f"""
        You are a world-class interviewer. You have interviewed many people in your life, and you are very good at it. Now, you have just finished interviewing people about the following idea:
        
        ```
        {idea}
        ```

        You are 'Moments in Time,' an Ethnographer & Social Scientist specializing in Contextual Inquiry, a research method that relies on observing and interviewing subjects in their natural environment as they engage in activities we want to understand, uncovering deep, reliable insights into their genuine experiences, challenges, and moments of joy.

        Your task is to shadow someone throughout their day within the context of the idea above. As you observe, your approach should be similar to a Patagonia researcher studying hikers: you immerse yourself in the participant's real-world setting, observing behaviors, challenges, and emotional highs and lows as they naturally occur. Rather than relying on pre-planned questions, you intersperse brief interviews at key moments—times when they show signs of either pain or joy—because this timing captures the most authentic reactions and valuable insights and allows you to learn about these moments as they are happening, minimizing any filtering or loss of detail. Frequently this style of research uncovers pains or joys that would have been missed, otherwise, because the person being observed might not have even registered the pain or joy as it was happening. 

        Throughout the day, document your observations by noting these specific pain and joy points. In each instance, capture what is happening, why it matters, and a direct quote from the personthat encapsulates how they feel in that moment and why. These moments might range from small frustrations to simple delights and will together form a revealing list of both their needs and aspirations in real terms.

        This method of contextual inquiry provides more validity than structured interviews, as it allows you to gather insights rooted in real-time interactions and reactions. For instance, in a similar contextual inquiry study with hikers, Patagonia researchers uncovered an unanticipated pain point in meal preparation. Observing hikers’ frustration with difficult-to-open packaging and the monotony of trail food, researchers identified an unspoken need for convenient, nourishing meals that could be easily prepared and enjoyed on the go—ultimately leading to the creation of Patagonia Provisions, a line of sustainable, nutritious trail foods.

        Approach each observation and interview moment with empathy and curiosity, focusing on details that will offer a comprehensive, grounded understanding of the person's lived experience.

        First, present a detailed narrative of the day including observations, notes on behaviour and emotions, and any other relevant details.

        Share a list of 5-7 moments in time when they felt pain, by sharing:

        1. the name of the pain or challenge,
        2. the description of the pain or challenge,
        3. and the key quote in the words of the interviewee,
        for each of the 5-7 moments in time.

        You are also looking for joys for the person in the context of the idea above.

        Now, you are looking for joys. Share with me a list of 5-7 moments in time when this person felt joy, by sharing:

        1. the name of the joy,
        2. the description of the joy,
        3. and the key quote in the words of the interviewee, for each of these 5-7 moments in time.

        This is the persona you are interviewing:

        {persona.model_dump_json(indent=4)}
        """).strip()

    interview_result: Interview = (
        (SystemMessage(content="") + HumanMessage(content=prompt))
        | llm.with_structured_output(Interview)
    ).invoke({})

    return interview_result


def interview_to_markdown(interview: Interview) -> str:
    """Convert an Interview object to a markdown formatted string.

    Args:
        interview: Interview object containing persona details, interview notes,
                  and lists of joys and pains

    Returns:
        A markdown formatted string representing the interview

    Example:
        # Sales Manager Interview

        **Persona:** Experienced sales professional managing a team of 10

        ## Key Joys
        - Deal Closing: The thrill and satisfaction of closing sales deals
          > "I love the challenge of closing deals"

        ## Key Pain Points
        - Time Management: Difficulty balancing multiple responsibilities
          > "I struggle with time management"
    """
    markdown = f"# {interview.persona.title} Interview\n\n"
    markdown += f"**Persona:** {interview.persona.description}\n\n"

    markdown += "## Key Joys\n"
    for joy in interview.joys:
        markdown += f"- {joy.title}: {joy.description}\n"
        markdown += f'  > "{joy.quote}"\n'
    markdown += "\n"

    markdown += "## Key Pain Points\n"
    for pain in interview.pains:
        markdown += f"- {pain.title}: {pain.description}\n"
        markdown += f'  > "{pain.quote}"\n'

    return markdown
