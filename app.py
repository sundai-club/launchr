import streamlit as st

from launchr.interview import generate_interview
from launchr.personas import generate_personas
from launchr.summarize import generate_summary


def main():
    st.title("Idea Analysis Tool")

    idea = st.text_area("Enter your idea:", height=150)

    if st.button("Analyze"):
        if idea:
            personas_result = generate_personas(idea)

            interviews = []
            for persona in personas_result.personas:
                interview = generate_interview(idea, persona)
                interviews.append(interview)

            summary = generate_summary(idea, interviews)

            st.subheader("Generated Personas and Pain Points")
            st.json(interviews)

            st.subheader("Summary")
            st.write(summary)
        else:
            st.warning("Please enter some business context first.")


if __name__ == "__main__":
    main()
