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
