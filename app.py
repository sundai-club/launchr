from textwrap import dedent

import streamlit as st
from icecream import ic

from launchr.interview import generate_interview
from launchr.personas import generate_personas
from launchr.questions import generate_questions
from launchr.summarize import generate_idea_hypothesis, generate_overall_summary


def main():
    st.title("Idea Analysis Tool")

    placeholder_idea = dedent("""
        App that helps people learn how to code.
        """).strip()
    idea = st.text_area("Enter your idea:", height=150, placeholder=placeholder_idea)

    ic(idea)

    if "hypothesis" not in locals():
        hypothesis = ""

    if st.button("Generate Idea Hypothesis"):
        if idea:
            hypothesis = generate_idea_hypothesis(idea)
            st.write(hypothesis)

    idea += "\n\n" + hypothesis

    if hypothesis:
        placeholder_personas = dedent("""
            - Sales Agent, 35, Male, New York, Loves the challenge of closing deals, Enjoys travel, Enjoys golf, Enjoys skiing
            - Marketing Agent, 28, Female, San Francisco, Loves the challenge of creating engaging content, Enjoys yoga, Enjoys hiking, Enjoys meditation
            - Customer Support Agent, 42, Male, Chicago, Loves the challenge of helping customers, Enjoys reading, Enjoys biking, Enjoys cooking
            """).strip()
        sample_personas = st.text_area(
            "(Optional) Enter some sample personas:",
            height=150,
            placeholder=placeholder_personas,
        )

        if st.button("Analyze"):
            if idea:
                personas_result = generate_personas(idea, sample_personas)
                st.write(personas_result)

                questions_result = generate_questions(personas_result)
                st.write(questions_result)

                interviews = []
                for persona in personas_result.personas:
                    interview = generate_interview(idea, persona)
                    interviews.append(interview)

                summary = generate_overall_summary(idea, interviews)

                st.subheader("Generated Personas and Pain Points")
                st.json(interviews)

                st.subheader("Summary")
                st.write(summary)
            else:
                st.warning("Please enter some business context first.")


if __name__ == "__main__":
    main()
