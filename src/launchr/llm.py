import os

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")


class GPT4o(ChatOpenAI):
    def __init__(self, *args, **kwargs):
        kwargs["model"] = "gpt-4o-2024-08-06"
        kwargs["api_key"] = OPENAI_API_KEY
        super().__init__(*args, **kwargs)


class Claude(ChatAnthropic):
    def __init__(self, *args, **kwargs):
        kwargs["model"] = "claude-3-5-sonnet-20240620"
        kwargs["api_key"] = ANTHROPIC_API_KEY
        super().__init__(*args, **kwargs)


default_llm = GPT4o()
