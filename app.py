from textwrap import dedent

import streamlit as st
from icecream import ic

from launchr.interview import generate_interview
from launchr.personas import generate_personas
from launchr.summarize import generate_idea_hypothesis, generate_overall_summary
from launchr.utils import strip_markdown_tags


def main():
    st.title("Idea Analysis Tool")

    placeholder_idea = dedent("""
        App that helps people learn how to code.
        """).strip()
    idea = st.text_area("Enter your idea:", height=150, placeholder=placeholder_idea)

    ic(idea)

    if "hypothesis" not in st.session_state:
        st.session_state.hypothesis = ""
        hypothesis = ""
    else:
        hypothesis = st.session_state.hypothesis

    if st.button("Generate Idea Hypothesis"):
        if idea:
            st.session_state.hypothesis = generate_idea_hypothesis(idea)
            hypothesis = st.session_state.hypothesis
        else:
            hypothesis = ""

    st.write(hypothesis)

    idea_hypothesis = idea + "\n\n" + hypothesis

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

    if hypothesis:
        if st.button("Analyze"):
            if idea:
                personas_result = generate_personas(idea, sample_personas)
                ic(personas_result)

                with st.expander("Generated Personas"):
                    st.json(personas_result)

                # TODO: make an answers generator
                # questions_result = generate_questions(personas_result)
                # ic(questions_result)

                interviews = []
                for persona in personas_result.personas:
                    interview = generate_interview(idea, persona)
                    interviews.append(interview)

                with st.expander("Generated Personas and Pain Points"):
                    st.json(interviews)

                summary = generate_overall_summary(idea, interviews)
                ic(summary)
                st.subheader("Generated Personas and Pain Points")

                st.markdown(strip_markdown_tags(summary).strip())
            else:
                st.warning("Please enter some business context first.")


if __name__ == "__main__":
    main()
