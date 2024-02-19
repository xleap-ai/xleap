from dataclasses import dataclass

from openai import OpenAI as DefaultOpenAI


@dataclass
class XLeapLLM:
    model: str
    _client: DefaultOpenAI = DefaultOpenAI()


def llm_factory(model="gpt-3.5-turbo-16k") -> XLeapLLM:
    return XLeapLLM(model=model)
