<<<<<<< HEAD
# launchr

Run streamlit locally:

Install dependencies with pdm (`brew install pdm` to install pdm on mac):

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
=======
# launchr AI App

What is it? Synthetic user validation by digitally simulating users and how they value functionality.
Why is this useful? Helps to speed up obtaining user feedback to validate the value of an idea.
Who are the users? The developers of AI app and similar products.
How does it work? input user case > generate AI persona's > syntheise pain points for each persona > generate summary
>>>>>>> f98d305c55e255a7787c521cd127e135b5eeea5b
