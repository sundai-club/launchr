# launchr

What is it? Synthetic user validation by digitally simulating users and how they value functionality.
Why is this useful? Helps to speed up obtaining user feedback to validate the value of an idea.
Who are the users? The developers of AI app and similar products.
How does it work? input user case > generate AI persona's > syntheise pain points for each persona > generate summary

## Run Locally

Run streamlit locally:

Install dependencies with pdm (`brew install pdm` to install pdm on mac, `pip install --user pdm` on windows):

```bash
pdm install
```

Run streamlit:

```bash
pdm run streamlit run app.py
```

## Draft Analysis State

I'm (Sean) thinking something like this:

```json
[
    0:{
        "title": "Sales Manager",
        "persona": "Experienced sales professional managing a team of 10",
        "pain_points":[
            0: "Challenge understanding customer needs",
            1: "Difficulty tracking sales pipeline"
        ]
    },
    1:{
        "title": "Sales Representative",
        "persona": "Entry-level sales person focused on outbound calls",
        "pain_points":[
            0: "Challenge understanding customer needs",
            1: "Difficulty tracking sales pipeline"
        ]
    }
]
```

## Password for on Streamlit

Age suggesting password:

Adapt the below code so that it is outcommented:

### SET PASSWORD

def check_password():
"""Returns True if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the passward is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Wachtwoord", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False

if not check_password():
st.stop() # Do not continue if check_password is not True.
